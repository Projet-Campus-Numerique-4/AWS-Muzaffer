import json
import os
import boto3

myDeviceTable = os.environ['DeviceTable']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(myDeviceTable)


def get_devices(context, event): 
    print(myDeviceTable)
    data = table.scan()
    result = data["Items"]
    return {
    "statusCode": 400,
    "body": json.dumps(result),
    "headers": {'Access-Control-Allow-Origin': '*'}
  }