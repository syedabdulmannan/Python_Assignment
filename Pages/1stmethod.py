import boto3

# Replace these values with your AWS credentials and Auto Scaling Group details
#aws_access_key_id = "your-access-key-id"
#aws_secret_access_key = "your-secret-access-key"
#region_name = "your-region"
#auto_scaling_group_name = "your-auto-scaling-group-name"
aws_access_key_id = "AKIATM3ZJ4VEZOW5RH5D"
aws_secret_access_key = "irfiO8LZyfC11IdsyMDEVNNjqSO2ee1QFA63Zg8Y"
region_name = "ap-south-1"
auto_scaling_group_name = "lv-test-cpu"


# Create an Auto Scaling client
asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Describe the Auto Scaling Group
response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])

# Extract running count and desired capacity
asg_details = response['AutoScalingGroups'][0]
running_count = asg_details['Instances']
desired_capacity = asg_details['DesiredCapacity']

# Check if there is a mismatch
if running_count != desired_capacity:
    print("Mismatch detected! Automation failed.")
else:
    print("Running count matches desired capacity.")