# Feedyard

A set of evolving, example infrastructure-as-code patterns and reference architectures for developing and operating an
infrastructure platform product designed to be resilient, secure, and capable of  change at scale in order to enable
the continuous delivery of custom applications.

## Table of Contents
 
### IaaS:AWS  

[Account Structure](account-structure.md)  
  
[bootstrap]  
Starting with only a newly created AWS Account, a minimal bootstrap configuration must occur to support an IaC proocess
for managing aws state.

#### Identity:iam  
  
[baseline-aws-profile-acct]  
[baseline-aws-resource-accts]  

[baseline-platform-networks]  
[baseline-platform-clusters]  
[baseline-platform-obs]  

### Services

#### pipeline-as-a-service

##### container images

[circleci-remote-docker](https://github.com/feedyard/circleci-remote-docker.git)  
[circleci-infra-agent](https://github.com/feedyard/circleci-infra-agent.git)  
