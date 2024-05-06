import boto3

def lambda_handler(event, context):
    # Ініціалізуємо клієнта EC2
    ec2 = boto3.client('ec2')
    
    # Отримуємо список EC2-інстансів
    response = ec2.describe_instances()
    
    # Створюємо список для зберігання ідентифікаторів зупинених інстансів
    stopped_instances = []
    
    # Перевіряємо кожен інстанс
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Перевіряємо, чи інстанс є запущеним
            if instance['State']['Name'] == 'running':
                # Перевіряємо, чи є тег "Owner=slipchuk"
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                if tags.get('Owner') == 'slipchuk':
                    # Зупиняємо інстанс
                    ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                    stopped_instances.append(instance['InstanceId'])
            else:
                stopped_instances.append(instance['InstanceId'])
                
    return stopped_instances