# AWS CloudFormation Deep Dive
Instructor [Richard Jones](https://www.linkedin.com/in/richard-jones-aws/)

More training

- [Amazon Web Services Fundamentals](https://www.safaribooksonline.com/library/view/amazon-web-services/9780134702186/)
- [Automation in AWS with CloudFormation, CLI, and SDKs](https://www.safaribooksonline.com/library/view/automation-in-aws/9780134818313/)
- [Networking in AWS](https://www.safaribooksonline.com/library/view/networking-in-amazon/9780134850849/)
- [AWS Certified Cloud Practitioner Complete Video Course](https://www.safaribooksonline.com/library/view/aws-certified-cloud/9780135175507/)
- [More live classes by Richard](https://www.safaribooksonline.com/search/?query=author%3A%22Richard%20A.%20Jones%22&extended_publisher_data=true&highlight=true&is_academic_institution_account=false&source=user&include_assessments=false&include_case_studies=true&include_courses=true&include_orioles=true&include_playlists=true&formats=live%20online%20training&sort=relevance)
- [Also check out training from my friend and colleague Chad Smith](https://www.safaribooksonline.com/search/?query=author%3A%22Chad%20Smith%22&extended_publisher_data=true&highlight=true&is_academic_institution_account=false&source=user&include_assessments=false&include_case_studies=true&include_courses=true&include_orioles=true&include_playlists=true&sort=relevance)

## A Note About This Class
This class is intended for those who have _AWS experience_ or have _previously attended other training_.

This class assumes you have a working knowledge of
- AWS global infrastructure
- AWS core services (VPC, EC2, S3, RDS)
- Scripting or programming (YAML, JSON, Python, etc)


This class covers
- Deep technical details of AWS CloudFormation
- How to write and deploy templates
- How CloudFormation fits into CI/CD

This class **does not** cover

- Fundamentals
- Other AWS services
- Continuous Integration and Deployment
- Every CloudFormation feature

## Agenda

### CloudFormation Overview

- Documentation
- Syntax
- CloudFormations place in CI/CD

### Creating Resources

- Using aws cli
- using Management console


### Updating Resources

- Change sets
- deploy command

### Stack Variables

- Pseudo-parameters
- Parameters
- Mappings
- References


### Organizing Templates and Stacks

- Nested Stacks
- cross-stack references


### Conditions

- conditional resources
- conditional resource options

### Wait Conditions and Helper Scripts

- Wait handles
- Cloud init

### Intrinsic Functions

- explore intrinsic functions
