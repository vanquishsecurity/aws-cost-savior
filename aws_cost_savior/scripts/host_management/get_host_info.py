#AWS Cost Saver
##Contact vanquish.security@gmail.com
##https://github.com/vanquishsecurity/aws-cost-savior
##GNU General Public License v3.0
#
#
#
#Python script using AWS CLI v2 to get host information from an AWS EC2 enviroment
#
#
import subprocess
#
#Get EC2 host information
#https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html
#
#Describes the specified instances or all instances
#
#Output text
subprocess.run(['aws', 'ec2', 'describe-instances', '--filters', '--output', 'text'])
#
#Output to table
subprocess.run(['aws', 'ec2', 'describe-instances', '--output', 'table'])
#