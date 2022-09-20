
provider "aws" {
	region = "us-west-2"
}

resource "aws_instance" "turma735" {
	ami = "ami-0021005f0cbcd6aaa"
	instance_type = "ts.micro"
}
