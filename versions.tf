terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = "~> 5.0"
    lacework = {
      source  = "lacework/lacework"
      version = "~> 1.16"
    }
  }
}
