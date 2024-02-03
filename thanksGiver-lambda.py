import json
import boto3
import os

#Define variables that will be reusable
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    '''   
    Whatever you define to trigger your function will have a JSON template (since basically everything runs on API's)
    If you want this function to run the code here, everytime certain actions occured to a storage location, that use-case will have its own template format
    In our case, this function is triggered via the URL. We'll call this trigger an event. 

    When the lambda function is triggered through its url, or in any other trigger case as I mentioned before,
    it passes the JSON to the 'event' argument in our function above. We can work with what the JSON body will lookl like
    and manipulate it to our needs. 

    For example, the 'urlEvent' variable below is trying to get the 'body' field in the 'event' JSON....
    
    '''
    
    firstName = event['body']['First Name']
    lastName = event['body']['Last Name']
    dateOfEvent = event['body']['Please select the Sunday that you would like to have your Thanksgiving']
    thanksgivingReason = event['body']['What event are you celebrating??']
    
    #It's best practice to put print statements in Lambda functions, as they will help you debug
    urlEvent = event['body']
    print(urlEvent)
    
    
    #Configure the message to send one time once someone fills the form
    #Use an f-string, so you can simply put the variables defined above, into the string
    notificationMessage = sns.publish(
            TopicArn='your-sns-topic-arn',
            Message=f"Hey team. {firstName} {lastName} just indicated an upcoming Thanksgiving celebration, for {dateOfEvent}"
    )
