import boto3
import json
import os
import uuid

TABLE_NAME = os.environ["TABLE_NAME"]

def post_device(context, event):
    
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(TABLE_NAME)
  payload: json.loads(event['body'])

  response = table.put_item(
              Item={
              "pk": uuid.uuid4().hex,
              'deviceName': payload['deviceName'],
              'deviceType': payload['deviceType']
              }
    )
  try:  
    response
  except Exception as e:
      return {
        "statusCode": 500,
        "body": json.dumps(e),
        "headers": {'Access-Control-Allow-Origin': '*'}}
  else:
    return {
      "statusCode": 200,
      "body": json.dumps(response),
      "headers": {'Access-Control-Allow-Origin': '*'}
    }


def get_devices(context, event):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(TABLE_NAME)
  try:
    data = table.scan()
  except Exception as e:
      return {
        "statusCode": 500,
        "body": json.dumps(e),
        "headers": {'Access-Control-Allow-Origin': '*'}}
  else:
    result=data["Items"]
    return {
      "statusCode": 200,
      "body": json.dumps(result),
      "headers": {'Access-Control-Allow-Origin': '*'}
    }