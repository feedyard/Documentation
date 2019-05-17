# cloud native adoption resources 

For adopting cloud native approaches to the development and release of online services -  
  
A set of evolving reference architectures and infrastructure-as-code patterns of using cloud infrastructure providers  
to compose and maintain a _delivery platform_ designed to be resilient, secure, and capable of change at scale, in order  
to enable software product development teams in the the continuous delivery of loosely coupled, cloud native applications.  

## Table of Contents

### What is cloud native?

_from the cloud native computing foundation website_
> Cloud native technologies empower organizations to build and run scalable applications in modern, dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative APIs exemplify this approach.
>
> These techniques enable loosely coupled systems that are resilient, manageable, and observable. Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.  

### Attributes of a cloud native application

- principle architecture based on APIs for interaction among capabilities
- capability domains oriented around loosely coupled microservices
- intentional separation of stateful from stateless services, typically reflecting 12-factor-app priorities
- rapid release velocity enabled by continuous integration and delivery engineering
- each service developed using the languages or frameworks best suited to the task
- builds packaged as lightweight containers, without server or operating system dependencies
- deployed to self-service, cloud infrastructure that is resilient and secure to safely support continuous change at resulting scale (e.g., infrastructure platform characterized by these same attributes)
- Defined, policy-driven resource allocation and enterprise governance support the development team's effort to sustain these attributes over time 

### Resources

#### IaaS:AWS  

[Account Structure](account-structure.md)  
  
[bootstrap-aws](https://github.com/feedyard/bootstrap-aws)  
Minimal automation for alternative strategies when starting with only a newly created AWS Account to bootstrap the IaC  
pattern for managing aws state.

#### Identity:iam  
  
[baseline-aws-auth-iam-only]  
[baseline-aws-auth-idp]   

[platform-aws-vpc]  

[platform-aws-eks]  
[platform-aws-kops]  

[platform-k8-core]  

#### Custom services

#### SaaS Integrations

##### CircleCI

###### container images

[circleci-remote-docker](https://github.com/feedyard/circleci-remote-docker.git)  
[circleci-base-image](https://github.com/feedyard/circleci-base-image.git)
[circleci-infra-agent](https://github.com/feedyard/circleci-infra-agent.git)  
[circleci-platform-agent](https://github.com/feedyard/circleci-platform-agent.git)  
[circleci-orb-agent](https://github.com/feedyard/circleci-orb-agent.git)  


notes

