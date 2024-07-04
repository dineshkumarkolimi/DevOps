Terraform

* Terraform is a Infra as a code tool to build, change, manage infra in a safe, consistent and repeatable manner
* It tracks configuration with state files
* Collaborates with the Terraform Cloud or any other cloud provider
* Steps involved in creating a Terraform lifecycle:
  1. Scope: Identify the infrastructure for the project
  2. Author: Write configurations to define the infrastructure (.tf files)
  3. Initialize: Install the required terraform providers
  4. Plan: Preview the changes terraform will make to the project
  5. Apply: Make changes to the infrastructure


Installation commands:
1. `brew install terraform`
2. `terraform -help`
3. `brew install hashicorp/tap/terraform`
4. `brew install hashicorp/tap/terraform`
5. `brew install hashicorp/tap/terraform`
7. `terraform -install-autocomplete`
8. `terraform login`


Resource creation/deletion:
1. `terraform init`
2. `terraform init` -migrate-state
3. `terraform plan`
4. `terraform apply`
5. `terraform apply -refresh-only`  ——> To refresh state as per updated changes in AWS
6. `terraform apply -migrate-state` ——> To refresh state as per updated changes
7.  `terraform destroy` ——> To destroy resources
8. `terraform apply -replace aws_instance.mtc_ec2` —> used to replace a resource and the instance name is fetched from `terraform state list`
9. `terraform apply -var "instance_name=YetAnotherName"` ex: terraform apply -var "aws_instance_name=Dinesh-test" this will apply the value of the variable as Dinesh-test.

State commands:
1. `terraform state list` ——> To show the list of available states in state file
2. `terraform show` ——> To show the configuration of state file
3. `terraform show -json` ——> will give config in json format
4. `terraform state show <state name>` ——> To see the config of a state
5. `terraform init -migrate-state`


General commands:
1. `terraform output` ——> command is used to extract the value of an output variable from the state file.
2. `-json` - If specified, the outputs are formatted as a JSON object, with a key per output
3. `terraform output instance_id`
4. `terraform fmt` ——> it will format the  tf files
5. `terraform console` ——> This helps us to play with functions, variables and experiment with them before we deploy
6. `terraform console -var=“host_os=unix”` ——> This will pick up value of a variable named host_os as unix but not the tfvars value or default value
7. `terraform console -var-file=“<variablefilename>.tfvars”`

Variables:
* Anywhere we want to use variables then we use `${var.<variable_nme>}`


  
 
