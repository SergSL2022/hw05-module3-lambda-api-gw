import boto3
import json

def lambda_handler(event, context):
    # Ініціалізуємо клієнта EC2
    ec2 = boto3.client('ec2')
    
    # Отримуємо параметри з об'єкта події
    instance_id = event['pathParameters']['instance_id']
    action = event['pathParameters']['action']
    
    # Отримуємо список EC2-інстансів
    response = ec2.describe_instances()
    
    # Шукаємо інстанс з вказаним ID
    found_instance = None
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['InstanceId'] == instance_id:
                found_instance = instance
                break
        if found_instance:
            break
    
    if found_instance:
        # Виконуємо дію відповідно до параметру
        if action == 'start':
            # Запускаємо інстанс
            ec2.start_instances(InstanceIds=[instance_id])
            response_body = {'message': f'Starting instance with ID {instance_id}'}
        elif action == 'stop':
            # Зупиняємо інстанс
            ec2.stop_instances(InstanceIds=[instance_id])
            response_body = {'message': f'Stopping instance with ID {instance_id}'}
        else:
            response_body = {'error': 'Invalid action specified. Please use "start" or "stop".'}
    else:
        response_body = {'error': f'Instance with ID {instance_id} not found.'}
    
    # Створюємо відповідь API Gateway
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body)
    }
    
    return response
