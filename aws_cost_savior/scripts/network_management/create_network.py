#AWS Cost Saver
##Contact vanquish.security@gmail.com
##https://github.com/vanquishsecurity/aws-cost-savior
##GNU General Public License v3.0
#
#
#
#Python script using AWS CLI v2 to create a subnet
#
#
import subprocess
#
#Get EC2 host information
#https://docs.aws.amazon.com/cli/latest/reference/ec2/create-subnet.html
#
#You must specify an IPv4 CIDR block for the subnet. After you create a subnet, you can't change its CIDR block.
# The allowed block size is between a /16 netmask (65,536 IP addresses) and /28 netmask (16 IP addresses). The CIDR
# block must not overlap with the CIDR block of an existing subnet in the VPC. Warning
# Amazon Web Services reserves both the first four and the last IPv4 address in each subnet's CIDR block.
# They're not available for use.
# If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle.
# When you stop an instance in a subnet, it retains its private IPv4 address. It's therefore possible to have a subnet
# with no running instances (they're all stopped), but no remaining IP addresses available.
#
#Output text
subprocess.run(['aws', 'ec2', 'create-subnet', '--vpc-id', 'vpc-08448d6c7b3f823fe', '--cidr-block', '10.0.69.0/24'])

#Note: The resource tag parsing is broken from cli output.
#aws ec2 create-subnet --vpc-id vpc-08448d6c7b3f823fe --cidr-block 10.0.69.0/24 --tag-specifications
# ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv4-only-subnet}]