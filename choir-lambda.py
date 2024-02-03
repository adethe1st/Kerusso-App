import json
import boto3
import os


dynamodb = boto3.client('dynamodb')
sns = boto3.client('sns')
phoneNumber = event[body]['Phone number (Do not add +1)']

def lambda_handler(event, context):
    
    #As Choir members add their numbers, this function, subscribes them to an SNS Topic, we already created. Simple
    subscribeNumbers = sns.subscribe(
            TopicArn='your-topic-arn',
            Protocol='sms',
            Endpoint= phoneNumber
    )
