import boto3

ecr_client = boto3.client('ecr')

repository_name = "cloud-monitoring-app"
response = ecr_client.create_respository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)