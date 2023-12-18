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

# Extract instances and their availability zones
asg_details = response['AutoScalingGroups'][0]
instances = asg_details['Instances']

# Check the number of running instances
running_instances_count = len(instances)
print(running_instances_count)
if running_instances_count > 1:
    # Check if instances are distributed across multiple availability zones
    unique_az_count = len(set(instance['AvailabilityZone'] for instance in instances))

    if unique_az_count < running_instances_count:
        print("Instances are distributed across multiple availability zones.")
    else:
        print("Instances are not distributed across multiple availability zones.")
else:
    print("There is only one running instance or no instance to show, no distribution check needed.")