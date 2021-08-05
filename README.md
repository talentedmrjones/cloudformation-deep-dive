# AWS CloudFormation
Instructor [Richard Jones](https://www.linkedin.com/in/richard-jones-aws/)

More training
- [Amazon Web Services Fundamentals 2nd Edition](https://learning.oreilly.com/videos/amazon-web-services/9780135581247/)
- [AWS Certified Cloud Practitioner Complete Video Course](https://learning.oreilly.com/videos/aws-certified-cloud/9780135175507/)
- [More Videos by Richard](https://learning.oreilly.com/search/?query=richard%20jones&extended_publisher_data=true&highlight=true&include_assessments=false&include_case_studies=true&include_courses=true&include_playlists=true&include_collections=true&include_notebooks=true&include_sandboxes=true&include_scenarios=true&is_academic_institution_account=false&source=user&formats=video&sort=relevance&facet_json=true&json_facets=true&page=0&include_facets=false&include_practice_exams=true)
- [Also check out training from Chad Smith](https://learning.oreilly.com/search/?query=chad%20smith&extended_publisher_data=true&highlight=true&include_assessments=false&include_case_studies=true&include_courses=true&include_playlists=true&include_collections=true&include_notebooks=true&include_sandboxes=true&include_scenarios=true&is_academic_institution_account=false&source=user&sort=relevance&facet_json=true&json_facets=true&page=0&include_facets=false&include_practice_exams=true)

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

### Creating Stacks

- Using aws cli
- using Management console


### Updating Stacks

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

## Links
- [CloudFormation Docs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [Template Anatomy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html)
- [Resource and Property Types](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
- [Intrinsic Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html)
- [Cross-stack References](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-crossstackref.html)