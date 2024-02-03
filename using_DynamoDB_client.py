
import json
import boto3
import os
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer


dynamodb = boto3.client('dynamodb')
sns = boto3.client('sns')
eventbridge = boto3.client('events')
serializer = TypeSerializer()
deserializer = TypeDeserializer()


def lambda_handler(event, context):
    #TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Working')
    # }
    dicto = event['body']
    print(event['body'])
    
    def serialize(dicto):
        serialized_item = serializer.serialize(vars(dicto) if hasattr(dicto, '__dict__') else dicto)
        return dicto if 'M' not in serialized_item else serialized_item['M']

    print(serialize(dicto))
    final_json = serialize(dicto)
    
    #Writes the thanksgiver's info to the Notifer Table
    dynamodb.put_item(
        TableName = 'dynamodb-table-name',
        Item = final_json
    )
    
    #Configure the message to send one time once someone fills the form. Eventbridge will handle it from here

