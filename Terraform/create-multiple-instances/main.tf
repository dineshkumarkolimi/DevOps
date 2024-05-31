#Command to execute this code is `terraform apply -var "aws_instance_name=<give name here>` "
terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.0"
        }
    }
}

resource "aws_instance" "app_server2" {
    ami = lookup(var.AMIServer, var.region)
    instance_type = "t2.micro"
    count = 3

    tags = {
        Name = format("%s-%s", var.aws_instance_name, "${count.index+1}")
    }

    # security_groups = var.Security_Groups
}