variable "aws_instance_name" {
    description = "name of the ec2 instance"
    type = string
    validation {
        condition = length(var.aws_instance_name) <= 20
        error_message = "The aws_instance_name must be less than 15 characters."
    }
    validation {
        condition = startswith(var.aws_instance_name, "Dinesh")
        error_message = "The aws_instance_name must be Dinesh followed by a string."
    }
}

variable "Security_Groups" {
    description = "security groups for the ec2 instance"
    type = list
    default = ["sg-24076", "sg-90890", "sg-456789"]
}

variable "region" {
    type = string
}

variable "AMIServer"{
    type = map
    default = {
        us-west-2 = "ami-08d70e59c07c61a3a"
    }
}