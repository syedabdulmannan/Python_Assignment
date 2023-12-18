import boto3
from datetime import datetime, timedelta

# Replace these values with your AWS credentials and Auto Scaling Group details
aws_access_key_id = "AKIATYPGQNVEU4JUXDRO"
aws_secret_access_key = "CRGOk600Epz9Fllei7M6LCJWNHxsVWMTbSoTKA37"
region_name = "ap-south-1"
auto_scaling_group_name = "lv-test-cpu"

# Create an Auto Scaling client
asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Describe the Auto Scaling Group
response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])

# Extract scheduled actions and their details
asg_details = response['AutoScalingGroups'][0]
scheduled_actions = asg_details['ScheduledActions']

# Find the next scheduled action
now = datetime.utcnow()
next_scheduled_action = None

for action in scheduled_actions:
    if action['StartTime'] > now:
        next_scheduled_action = action
        break

# Calculate elapsed time until the next scheduled action
if next_scheduled_action:
    time_until_next_action = next_scheduled_action['StartTime'] - now
    elapsed_time = str(time_until_next_action).split(".")[0]  # Remove microseconds
    print(f"Next scheduled action '{next_scheduled_action['ScheduledActionName']}' will run in: {elapsed_time}")
else:
    print("No upcoming scheduled actions.")
