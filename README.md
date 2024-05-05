# hw05-module3-lambda-api-gw

## Lambda

### 1. Create Lambda function using python and boto3
#### 1.1. The function should get list of EC2 instances
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 21-32-44.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 21-34-07.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 21-38-23.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 23-39-17.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 23-40-01.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 23-40-09.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 23-40-29.png>)
![alt text](<screenshots/1/Знімок екрана з 2024-05-05 23-40-54.png>)
#### 1.2. Check if it is running and has the "Owner=Your Name" tag
#### 1.3. Then stop it or skip otherwise
#### 1.4. Return the list of stopped instance IDs

### 2. Create Lambda function using python and boto3
#### 2.1. The function should get list of EC2 instances
#### 2.2. Check if it is stopped and has the "Owner=Your Name" tag
#### 2.3. Then start it or skip otherwise
#### 2.4. Return the list of started instance IDs

### 3. Run both lambda functions and confirm that they work




## API Gateway

### 1. Create API gateway with the following endpoints:
#### /instances/stop - triggers the 1st lambda
#### /instances/start - triggers the 2nd lambda


### 2. Confirm that it works as expected


## Advanced
### 1. Create lambda function which gets ID of instance and needed operation (stop/start)

### 2. Get list of instances and finds that record if exists

### 3. If record is found then perform the operation

### 4. Create endpoint in API GW /instance/{ID}/{operation} and point it to the new lambda

### 5. Find ID of any existing EC2 instance and use it you your requests to stop/start the VM via API GW



## Cleanup
### 1. Add code of lambda function to your project
### 2. Remove all lambdas and API GW from AWS