# Feedyard

A set of evolving, example infrastructure-as-code patterns and reference architectures for developing and operating an
infrastructure platform product designed to be resilient, secure, and capable of change at scale, in order to enable
the continuous delivery of distribute computing architectures on IaaS providers.

## Table of Contents
 
### IaaS:AWS  

[Account Structure](account-structure.md)  
  
[bootstrap-aws](https://github.com/feedyard/bootstrap-aws)  
Starting with only a newly created AWS Account, a minimal bootstrap configuration must occur to support an IaC proocess
for managing aws state.

#### Identity:iam  
  
[baseline-aws-auth-iam-only]  
[baseline-aws-auth-idp]   

[platform-aws-vpc]  

[platform-aws-eks]  
[platform-aws-kops]  

[platform-k8-core]  

### Services

#### pipeline-as-a-service

##### container images

[circleci-remote-docker](https://github.com/feedyard/circleci-remote-docker.git)  
[circleci-base-image](https://github.com/feedyard/circleci-base-image.git)
[circleci-infra-agent](https://github.com/feedyard/circleci-infra-agent.git)  
[circleci-platform-agent](https://github.com/feedyard/circleci-platform-agent.git)  
[circleci-orb-agent](https://github.com/feedyard/circleci-orb-agent.git)  
