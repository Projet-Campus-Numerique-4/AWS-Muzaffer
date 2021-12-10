import boto3
import json
import logging
import os

# Logger
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

TABLE_NAME = os.environ["TABLE_NAME"]
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def get_devices(context, event):
  logger.info(TABLE_NAME)
  data = table.scan()["Items"]
  return {
    "statusCode": 400,
    "body": json.dumps(data),
    "headers": {'Access-Control-Allow-Origin': '*'}
  }
