# Kerusso
Created this solution becuase of a problem I recently observed in my church. Built from mostly serverless technologies. Also, has some of the failed architecture patterns I decided to adjust due to reasons provide

The details for the different architecture patterns would be seen in my blog writeup on the App's development process: https://hashnode.com/post/clrzfpiyu00000al0b0sa4fo2


![Kerusso-Page-3 drawio](https://github.com/adethe1st/Notifier-App/assets/116035386/c20bd7ba-148d-4534-9b3a-85ad0cefbc12)

The basic gist is

- The Choir needed to be informed when a church member intended to celebrate at church

- The Choir would need specific details of the person celebrating, especially their names, as it would determine the direction of the music

The code files needed are:
- thanksGiver-appsScript.js
- thanksGiver-lambda.py
- choir-appsScript.js
- choir-lambda.py

When Lmabda is triggered via its function URL, a specific JSON body is generated, with your own data in that JSON data within it. As described in the docs here: https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads

- urlRequestBody.json
  
