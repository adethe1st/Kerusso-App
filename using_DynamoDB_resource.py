import json
import boto3
import os


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('dynamodb-table-name')

sns = boto3.client('sns')


def lambda_handler(event, context):
    dicto = event['body']
    print(dicto)

    #Writes the thanksgiver's info to the Notifer Table
    table.put_item(
        Item = dicto
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
