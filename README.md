# saas-identity-cognito
## SaaS Identity and Isolation with Amazon Cognito on the AWS Cloud


This Quick Start implements a high availability solution for identity and isolation in multi-tenant software as a service (SaaS) environments, using Amazon Cognito as the identity provider.

The Quick Start sets up the AWS environment and provides a lightweight SaaS order management system that illustrates different aspects of identity and isolation, spanning the roles in a multi-tenant environment. The Quick Start deployment includes AWS services such as Amazon Cognito, AWS Lambda, Amazon API Gateway, and Amazon EC2 Container Service (Amazon ECS).

This Quick Start deploys the SaaS architecture into a virtual private cloud (VPC) that spans two Availability Zones in your AWS account. The deployment and configuration tasks are automated by AWS CloudFormation templates that you can customize during launch. The deployment guide explains core SaaS identity and isolation concepts and implementation details, and includes a walkthrough.

The Quick Start offers two deployment options:

- Deploying the SaaS environment into a new virtual private cloud (VPC) on AWS
- Deploying the SaaS environment into an existing VPC on AWS

You can also use the AWS CloudFormation templates as a starting point for your own implementation.

![Quick Start architecture for SaaS identity and isolation on AWS](https://d0.awsstatic.com/partner-network/QuickStart/saas/saas-identity-with-cognito-architecture-on-aws.png)

For architectural details, best practices, step-by-step instructions, and customization options, see the [deployment guide](https://s3.amazonaws.com/quickstart-reference/saas/identity/cognito/latest/doc/saas-identity-and-isolation-with-cognito-on-the-aws-cloud.pdf).

To post feedback, submit feature ideas, or report bugs, use the **Issues** section of this GitHub repo.
If you'd like to submit code for this Quick Start, please review the [AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/). 
