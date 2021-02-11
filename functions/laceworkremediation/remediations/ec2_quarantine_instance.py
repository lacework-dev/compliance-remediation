# -*- coding: utf-8 -*-
"""
Lacework Remediation: ec2_block_all_sg.py

This function will block all traffic to/from an EC2 instance.
"""

import logging

from botocore.exceptions import ClientError

logger = logging.getLogger()


def run_action(boto_session, entity, response):
    logger.info("Initiating blocking of traffic to/from EC2 instance.")

    # Get the region for the resource
    region = entity.split(":")[3]

    # Get the instance ID (https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
    instance = entity.split(":")[5].replace("instance/", "")

    # Create an EC2 client / resource
    ec2_client = boto_session.client("ec2", region_name=region)
    ec2_resource = boto_session.resource("ec2", region_name=region)

    # Get the Instance VPC
    try:
        result = ec2_client.describe_instances(
            InstanceIds=[instance]
        )

        if result["Reservations"]:
            if result["Reservations"][0]["Instances"]:
                vpc_id = result["Reservations"][0]["Instances"][0]["VpcId"]

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
        return

    # Create a Quarantine Security Group
    try:
        result = ec2_client.describe_security_groups(
            Filters=[
                {
                    "Name": "group-name",
                    "Values": ["lacework-quarantine"]
                },
                {
                    "Name": "vpc-id",
                    "Values": [vpc_id]
                }
            ]
        )

        if result["SecurityGroups"]:
            quarantine_sg_id = result["SecurityGroups"][0]["GroupId"]

            # Log the returned Security Group
            message = f"Existing quarantine Security Group: {quarantine_sg_id}"
            logger.info(message)
            response["messages"].append(message)

        else:
            result = ec2_client.create_security_group(
                Description="Lacework quarantine Security Group (Block All)",
                GroupName="lacework-quarantine",
                VpcId=vpc_id
            )

            quarantine_sg_id = result["GroupId"]

            # Remove default outbound rule
            quarantine_sg = ec2_resource.SecurityGroup(quarantine_sg_id)
            quarantine_sg.revoke_egress(
                GroupId=quarantine_sg_id,
                IpPermissions=[
                    {
                        "IpProtocol": "-1",
                        "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
                    }
                ]
            )

            # Log the created Security Group
            message = f"Created quarantine Security Group: {quarantine_sg_id}"
            logger.info(message)
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
        return

    # Attach Security Group to Instance
    try:
        result = ec2_resource.Instance(instance).modify_attribute(Groups=[quarantine_sg_id])

        response_code = result["ResponseMetadata"]["HTTPStatusCode"]

        if response_code >= 400:
            # Log the returned error
            message = f"Unexpected error: {result}"
            logger.info(message)
            response["messages"].append(message)
        else:
            # Log the successful stop
            message = f"Instance '{instance}' was successfully quarantined."
            logger.info(message)
            response["status"] = "ok"
            response["messages"].append(message)

    except ClientError as e:
        message = f"Unexpected error: {e}"
        logger.error(message)
        response["messages"].append(message)
