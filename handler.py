import json
import time

def hello(event, context):

    body = {
        "timestamp": time.time(),
        "event": event
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body, indent=2)
    }

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
