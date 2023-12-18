from Config.Config.config import config
import boto3

class BaseFile:

    aws_access_key_id = config.aws_access_key_id
    aws_secret_access_key = config.aws_secret_access_key


    def get_asg_describe(asgname):
        asg_client = boto3.client('autoscaling', aws_access_key_id=config.aws_access_key_id,
                                  aws_secret_access_key=config.aws_secret_access_key, region_name='ap-south-1')
        asg_response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asgname])
        return asg_response

