# aws-cost-savior
A scripting tool to save money on running AWS services and products. Turn-key creation/delete, power on/off, etc.


User Project Requirements

* Your own AWS account  (console.aws.amazon.com/console)
* AWS CLIv2 Tookkit for PyCharm (https://aws.amazon.com/cli/) or AWS Toolkit for Visual Studio Code (https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html)
* Your own root SSH key maanged by you (not responable for lost/stolen SSH root keys)
* Your favorite SDK tool if any (Example: Visiual Studio or PyCharm)
* Git SCM (https://git-scm.com/downloads) 
* AWS IAM profiles (TBD)


Project Structure

* Networking Services
  * VPC
  * IPAM
* DNS
  * Route 53
* Security Services
  * Firewall
  * ACLs
* Compute Services
  * EC2 
* Application Services
  * HTTPd

Types of Scripts

Note: More scripts types will be added in the future

Describe/Get Information/Status

A script to pull information about a gateway, host, network, volumes, vpc.

Gateway Management

* Create gateway
* Attach gateway
* Delete gatway

Host Management

* Create virtual machine
* Power on
* Power off
* Delete virtual machine

Volume Management

* Create volume
* Attach volume
* Detach volume
* Modify volume
* Delete volume

Network Management

* Create network
* Delete network
* Create network interface
* Delete network interface
* Create ACL
* Modify ACL
* Delete ACL

VPC (Cloud) Management

* Create VPC
* Delete VPC
* Modify VPC
* Start VPC


AWS Doc References

Allways Free Services List

https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all

Setup Enviroment

* Install PyCharm 
* Or Install Microsoft Viusal Studio
* Install PayCharm AWS Toolkit (https://www.jetbrains.com/pycharm/guide/tutorials/intro-aws/setup/)
  * To install the plugin follow the below steps.
  * Go to Settings -> Plugins
   * Search AWS Toolkit
    * Click on Install
* Or Install AWS Toolkit for Visual Studio Code https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/setup-toolkit.html


