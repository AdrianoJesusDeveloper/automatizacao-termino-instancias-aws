import boto3

def terminator():
    # Apenas regiões dos EUA e América do Sul
    ec2_client = boto3.client('ec2')
    regions = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'sa-east-1']

    # Realiza um loop nas regiões da variável acima
    for region in regions:
        print(f"Terminating instances in {region}")

        # Cria uma variável para cada região
        ec2 = boto3.resource('ec2', region_name=region)

        # Com a variável anterior, filtra as instâncias que estão RUNNING, STOPPING, STOPPED
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped', 'stopping']}])

        # Termina as instâncias
        for instance in instances:
            try:
                instance.terminate()
                print(f'{instance.id} terminated')
            except:
                print(f'Erro ao terminar {instance.id}')

def lambda_handler(event, context):
    terminator()
