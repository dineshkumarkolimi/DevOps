output "instance_id" {
  description = "Outputs the id of ec2 instance created"
  value = aws_instance.app_server.id
}


output "instance_public_ip" {
  description = "Outputs the public ip address of ec2 instance created"
  value = aws_instance.app_server.public_ip
}
