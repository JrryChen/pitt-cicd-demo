import json
from googletrans import Translator

def GetMessage(lang):
    message = "Hello World"
    return message

def handler(event, context):
    if event['queryStringParameters']:
        lang = event['queryStringParameters']['lang']

        body = {}
        body['message'] = GetMessage(lang)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps(body),
        }
    else:
        return {
            'statusCode': 422
        }
