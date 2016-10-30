import json
import time

import boto3

SNS_ALERTS_ARN = 'arn:aws:sns:us-east-1:383893927536:tamper-server-alerts'


def hello(event, context):
    body = {
        "timestamp": time.time(),
        "event": event
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body, indent=2)
    }


def event_box_opened(event, context):
    sns = boto3.client('sns')
    sns.publish(Message='Box opened at timestamp %i.' % time.time(),
                TopicArn=SNS_ALERTS_ARN)

    return {
        'statusCode': 200,
        'body': '{}'
    }
