terraform {
  backend "remote" {
     organization = "dinesh_learning"
     workspaces {
       name = "Example-Savingstate"
     }
   }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
}
 
provider aws {
  profile = "default"
  region  = "us-west-2"
}
 
resource "aws_instance" "app_server" {
  ami           = "ami-08d70e59c07c61a3a"
  instance_type = "t2.micro"
 
  tags = {
    Name = var.instance_name
  }
}
