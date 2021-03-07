import boto3

regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1','ap-southeast-1','ap-southeast-2','ap-northeast-1']

for region in regions:

  client = boto3.client('ec2',region_name=region,)

  dex_dict = client.describe_tags()

  for dexy_dict in dex_dict['Tags']:

    if dexy_dict['ResourceType'] == 'instance':

        if dexy_dict['Key'] == 'Name':

          print dexy_dict

          print dexy_dict['Value']

          print ' '

    # print dexy_dict['ResourceType']

    # print dexy_dict['Value']

    # print ' '