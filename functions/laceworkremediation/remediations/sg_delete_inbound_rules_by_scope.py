# -*- coding: utf-8 -*-
"""
Lacework Remediation: sg_delete_inbound_rules_by_scope.py

This function will delete all rules on a security group with a scope(cidr)
containing or equal to a given scope, port and protocol are optional.

Parameters:
    scope: a.b.c.d/e
    port: number/ *
    protocol: TCP/ UDP/ *

Examples:
    sg_rules_delete_by_scope 0.0.0.0/0 22 tcp

"""
import ipaddress
import logging

logger = logging.getLogger()

PORT_TO = "ToPort"
PORT_FROM = "FromPort"
PROTOCOL = "IpProtocol"
PARAMETERS = {"port", "protocol", "scope"}


def is_scope_contained_by_other_ipv4(scope, other):
    n1 = ipaddress.IPv4Network(scope)
    n2 = ipaddress.IPv4Network(other)
    scope_len = n1.prefixlen
    other_len = n2.prefixlen
    return scope_len >= other_len and n1.supernet(scope_len - other_len) == n2


def run_action(boto_session, entity, response, **params):
    logger.info("Initiating rule removal from Security Group by IP scope.")

    # Verify parameters
    params_set = set(params.keys())
    if PARAMETERS.issubset(params_set):
        for parameter in PARAMETERS:
            logger.info(f"Parameter '{parameter}': {params[parameter]}")

    else:
        message = f"Required parameters {PARAMETERS} weren't provided: {params}"
        logger.error(message)
        response["messages"].append(message)
        return

    # Get Security Group ID
    security_group_id = entity.split(":")[5].split("/")[-1:][0]

    logger.info(f"Security Group: {security_group_id}")

    # Create an ec2 resource
    ec2_resource = boto_session.resource("ec2")

    # Get the Security Group
    security_group = ec2_resource.SecurityGroup(security_group_id)

    # Retrieve params
    port = params["port"]
    protocol = str(params["protocol"])
    scope = str(params["scope"])

    # Iterate through directional rules
    for rule in security_group.ip_permissions:

        logger.info(rule)

        # Verify desired port in rule's range
        if port == "*" or rule[PORT_FROM] <= int(port) <= rule[PORT_TO]:

            # Verify protocol match
            if protocol == "*" or protocol.lower() == rule[PROTOCOL].lower() or rule[PROTOCOL] == "-1":

                for ip_range in rule["IpRanges"]:
                    if is_scope_contained_by_other_ipv4(scope, ip_range["CidrIp"]):

                        try:
                            security_group.revoke_ingress(
                                CidrIp=ip_range["CidrIp"],
                                FromPort=rule[PORT_FROM],
                                ToPort=rule[PORT_TO],
                                IpProtocol=rule[PROTOCOL].lower()
                            )

                            # Log the successful removal
                            message = f"Security Group '{security_group_id}' was successfully modified."
                            logger.info(message)
                            response["status"] = "ok"
                            response["messages"].append(message)

                        except Exception as e:
                            message = f"Unexpected error: {e}"
                            logger.error(message)
                            response["messages"].append(message)
