terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 4.6"
        }
    }
}

providers "aws" {
    region = "us-west-2"
    profile = "default"
}

resource "aws_instance" "sample_instance" {
    ami = "ami-0c2b8ca1dad447f8a"
    instance_type = "t2.micro"
    tags = {
        Name = "SampleInstance"
    }
}