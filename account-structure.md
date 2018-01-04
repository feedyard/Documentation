# Account Structure

## Security Model

Four AWS accounts for the following uses:  

Account 1: production  
Account 2: nonproduction  
Account 3: sandbox  
  
Account 4: IAM User auth integration and group membership*  

IAM Groups are defined within the IAM or 'profile' account with policy that permits members of the groups to assume
various roles in the other ('resource') accounts. In this way, AWS resources in general are maintained separate from
the identity and authorization necessary to define such resources.
  
 ![Account Structure](images/aws_account_structure.png)

*This general pattern follows the security principles outlined by [Moritz Heiber](https://www.thoughtworks.com/insights/blog/using-aws-security-first-class-citizen).