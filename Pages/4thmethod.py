import boto3
from datetime import datetime
# Replace these values with your AWS credentials and Auto Scaling Group details
#aws_access_key_id = "your-access-key-id"
#aws_secret_access_key = "your-secret-access-key"
#region_name = "your-region"
#auto_scaling_group_name = "your-auto-scaling-group-name"
aws_access_key_id = "AKIATM3ZJ4VEZOW5RH5D"
aws_secret_access_key = "irfiO8LZyfC11IdsyMDEVNNjqSO2ee1QFA63Zg8Y"
#aws_access_key_id = "AKIATYPGQNVEU4JUXDRO"
#aws_secret_access_key = "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"
region_name = "ap-south-1"
auto_scaling_group_name = "lv-test-cpu"

# Create an Auto Scaling client
asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Describe the Auto Scaling Group
response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])

# Extract instances and their details
asg_details = response['AutoScalingGroups'][0]
instances = asg_details['Instances']

# Get instance creation times and calculate uptime
instance_uptime = []

for instance in instances:
    instance_id = instance['InstanceId']
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    launch_time = response['Reservations'][0]['Instances'][0]['LaunchTime']
    uptime = datetime.now(launch_time.tzinfo) - launch_time
    instance_uptime.append((instance_id, uptime))

# Find the instance with the longest uptime
longest_running_instance = max(instance_uptime, key=lambda x: x[1])

print(f"Longest running instance: {longest_running_instance[0]}, Uptime: {longest_running_instance[1]}")