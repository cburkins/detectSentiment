import json
import boto3
import logging


# Standard python module for logging.  This seems to also send message to AWS CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    

    if (('queryStringParameters' in event.keys()) and (event['queryStringParameters'] != None)):
        

        logger.info(event)

        params = event["queryStringParameters"]
        
        logger.info(params);
        logger.info(type(params))
        
        if "statement" in params:
    
            userStatement = params["statement"];
            comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
            # compResult = comprehend.detect_sentiment(Text = "This makes me very unhappy", LanguageCode='en')
            compResult = comprehend.detect_sentiment(Text = userStatement, LanguageCode='en')
    
            # dataPkg = { 'username': 'El Roberto', 'id': 42 };
            dataPkg = { 'results': compResult };
            dataPkg = { 'userStatement': userStatement, 'results': compResult };
            # Original CORS: "http://ec2-54-210-100-224.compute-1.amazonaws.com"
            return {
                'statusCode': 200,
                'headers': { 'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "http://awsafjnva1004.jnj.com",
                    "Access-Control-Allow-Credentials": "true"
                 },
                'body': json.dumps(dataPkg)
            }
        else:
            return {
                'statusCode': 422,
                'headers': { 'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "http://amazonaws.com",
                    "Access-Control-Allow-Credentials": "true"
                },
                'body': json.dumps({ 'error': 'missing parameters'})
            }
    else:
        return {
                'statusCode': 422,
                'headers': { 'Content-Type': 'application/json',
                    "Access-Control-Allow-Origin": "http://amazonaws.com",
                    "Access-Control-Allow-Credentials": "true"
                },
                'body': json.dumps({ 'error': 'Zero parameters sent'})
            }
