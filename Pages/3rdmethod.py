import boto3

# Replace these values with your AWS credentials and Auto Scaling Group details
#aws_access_key_id = "your-access-key-id"
#aws_secret_access_key = "your-secret-access-key"
#region_name = "your-region"
#auto_scaling_group_name = "your-auto-scaling-group-name"
#aws_access_key_id = "AKIATM3ZJ4VEZOW5RH5D"
#aws_secret_access_key = "irfiO8LZyfC11IdsyMDEVNNjqSO2ee1QFA63Zg8Y"
aws_access_key_id = "AKIATYPGQNVEU4JUXDRO"
aws_secret_access_key = "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"
region_name = "ap-south-1"
auto_scaling_group_name = "lv-test-cpu"


# Create an Auto Scaling client
asg_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Describe the Auto Scaling Group
response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[auto_scaling_group_name])

# Extract instances and their details
asg_details = response['AutoScalingGroups'][0]
instances = asg_details['Instances']

# Extract SecurityGroup, ImageID, and VPCID of the first instance (assuming they are the same for all instances)
first_instance = instances[0]
sg_id = first_instance['SecurityGroups'][0]['GroupId']
image_id = first_instance['ImageId']
vpc_id = first_instance['VpcId']

# Check if all instances have the same SecurityGroup, ImageID, and VPCID
for instance in instances[1:]:
    if (
        instance['SecurityGroups'][0]['GroupId'] != sg_id
        or instance['ImageId'] != image_id
        or instance['VpcId'] != vpc_id
    ):
        print("SecurityGroup, ImageID, or VPCID mismatch detected on instances.")
        break
else:
    print("SecurityGroup, ImageID, and VPCID are the same on all instances.")