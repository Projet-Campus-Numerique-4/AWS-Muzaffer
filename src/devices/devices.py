import boto3
import json
import os

TABLE_NAME = os.environ["TABLE_NAME"]

def get_devices(context, event):
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table(TABLE_NAME)
  try:
    data = table.scan()
  except Exception as e:
      return {
        "statusCode": 418,
        "body": json.dumps(e),
        "headers": {'Access-Control-Allow-Origin': '*'}}
  else:
    result=data["Items"]
    return {
      "statusCode": 200,
      "body": json.dumps(result),
      "headers": {'Access-Control-Allow-Origin': '*'}
    }