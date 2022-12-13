#AWS Cost Saver
##Contact vanquish.security@gmail.com
##https://github.com/vanquishsecurity/aws-cost-savior
##GNU General Public License v3.0
#
#
#
#Python script using AWS CLI v2 to get network information from an AWS VPC enviroment
#
#
import subprocess
#
#Get EC2 Elastic IP addresses
#https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-addresses.html
#
#Returns PublicIp, AllcationID, Domain, PublicIpv4Pool, and NetworkBorderGroup
#
#Output text
subprocess.run(['aws', 'ec2', 'describe-addresses', '--filters', 'Name=domain,Values=vpc', '--output', 'text'])
#
#Output to table
subprocess.run(['aws', 'ec2', 'describe-addresses', '--output', 'table'])
#
