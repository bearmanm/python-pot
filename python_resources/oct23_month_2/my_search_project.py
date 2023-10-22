# I'm challenging myself to create a program that can search for good know working terraform code for projects to speed up a deploy process. 
# this is work in progress..  

def get_sentence_with_word(sentences, target_word):
    matching_sentences = [sentence for sentence in sentences if target_word in sentence]
    return matching_sentences

# Define a list of sentences and their corresponding outputs
sentences_1 = [
    "zixi.",
    "variable.",
    "zixi_project.",
    "zixi variable.tf."
]
output_1 = '''
variable "region" {
  #default = "eu-west-2"
  default = "eu-west-2"
}
variable "Environment" {
  description = "Current working environment dev"
  type        = string
  default     = "dev"
}

variable "AccountNumber" {
  description = "AWS account number"
  type        = string
  default     = "5876xxxxxx46"
}
variable "workflow" {
  description = "Workflow under which resources reside"
  type        = string
  default     = "grpctb"
}
variable "resourcetags" {
  description = "Tags to apply to all resources"
  default = {
    territory      = "uk"
    billing_team   = "cti"
    department     = "cbp"
    sub_department = "ctb"
    environment    = "dev"
    cost_centre    = "200092xxxxx"
    workflow       = "grxxtb"
    
  }
  type = map(string)
}

variable "ami" {
  description = "our ec2 ami"
  type        = string
  default     = "ami-0ca9cbxxxxxxxxxxxx"
}

variable "instance_type" {
  description = "this is the instance type for the choosen ec2 instance"
  type        = string
  default     = "c6g.medium"
}

variable "subnet_id" {
  description = "this is our subnet"
  type        = string
  default     = "subnet-072aexxxxxxxxxxx"

}

variable "bucket_name" {
  description = "this is our s3 for our software"
  type        = string
  default     = "dev-grxxxx-zixi-s3"

}

variable "key_name" {
  description = "The key name to use for the instance"
  type        = string
  default     = "AWS_EC2_zixi_xx_xx"

}

variable "security_group_id" {
  type    = string
  default = "sg-0f4fxxxxxxxxxxx"
}
'''

sentences_2 = [
    "zixi main.ft.",
    "zixi.",
    "display zixi main.tf."
]
output_2 = '''
module "ec2" {
  source            = "../../modules/ec2"
  ami               = var.ami
  instance_type     = var.instance_type
  subnet_id         = var.subnet_id
  security_group_id = var.security_group_id
  key_name          = var.key_name
  resourcetags = var.resourcetags
name ="dev-grxxxxx-zixi-ec2"
}

module "s3" {
  source = "../../modules/s3"
  bucket_name = var.bucket_name
}
'''

# Get user input for the target word
target_word = input("Enter the word you want to search for: ")

# Find sentences containing the target word
matching_sentences_1 = get_sentence_with_word(sentences_1, target_word)
matching_sentences_2 = get_sentence_with_word(sentences_2, target_word)


# Print the matching URL once
if matching_sentences_1:
    print(f"The following sentences contain the word '{target_word}':")
    print(output_1)
# Print the matching words multiple times
elif matching_sentences_2:
    print(f"The following sentences contain the word '{target_word}':")
    print(output_2)
else:
    print(f"No sentences contain the word '{target_word}'.")