import boto3
from datetime import datetime, timedelta

# Replace these values with your AWS credentials and Auto Scaling Group details
aws_access_key_id = "AKIATYPGQNVEU4JUXDRO"
aws_secret_access_key = "CRGOk600Epz9Fllei7M6LCJWNHxsVWMTbSoTKA37"
region_name = "ap-south-1"
auto_scaling_group_name = "lv-test-cpu"

# Create an Auto Scaling client and EC2 client
asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key, region_name=region_name)
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

# Get the current date in UTC
current_date_utc = datetime.utcnow()

# Describe the Auto Scaling Group
response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])

# Extract instances and their details
asg_details = response['AutoScalingGroups'][0]
instances = asg_details['Instances']

# Initialize counters for launched and terminated instances
launched_instances = 0
terminated_instances = 0

# Check each instance's launch and termination times
for instance in instances:
    instance_id = instance['InstanceId']

    # Describe the instance to get launch and termination time
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    launch_time = response['Reservations'][0]['Instances'][0].get('LaunchTime')
    termination_time = response['Reservations'][0]['Instances'][0].get('TerminationTime')

    if launch_time and launch_time.date() == current_date_utc.date():
        launched_instances += 1

    if termination_time and termination_time.date() == current_date_utc.date():
        terminated_instances += 1

# Print the results
print(f"Total instances launched today: {launched_instances}")
print(f"Total instances terminated today: {terminated_instances}")