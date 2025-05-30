import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])
    instances_to_terminate = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_terminate.append(instance['InstanceId'])

    if instances_to_terminate:
        print(f"Encerrando instâncias: {instances_to_terminate}")
        ec2.terminate_instances(InstanceIds=instances_to_terminate)
    else:
        print("Nenhuma instância para encerrar.")
