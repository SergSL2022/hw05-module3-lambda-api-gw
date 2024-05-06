import boto3

def lambda_handler(event, context):
    # Ініціалізуємо клієнта EC2
    ec2 = boto3.client('ec2')
    
    # Отримуємо список EC2-інстансів
    response = ec2.describe_instances()
    
    # Створюємо список для зберігання ідентифікаторів запущених інстансів
    started_instances = []
    
    # Перевіряємо кожен інстанс
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Перевіряємо, чи інстанс є зупиненим
            if instance['State']['Name'] == 'stopped':
                # Перевіряємо, чи є тег "Owner=slipchuk"
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                if tags.get('Owner') == 'slipchuk':
                    # Запускаємо інстанс
                    ec2.start_instances(InstanceIds=[instance['InstanceId']])
                    print('Starting instance with tag slipchuk')
                    started_instances.append(instance['InstanceId'])
                else:
                    print('Skip starting instance with tag slipchuk')
    
    # Повертаємо список ідентифікаторів запущених інстансів
    return started_instances