import boto3
import json
import logging
import os
import numpy as np
import time

from boto3.dynamodb.conditions import Key

# Logger
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEVICES_TABLE_NAME = os.environ["DEVICES_TABLE_NAME"]
LOGS_TABLE_NAME = os.environ["LOGS_TABLE_NAME"]

dynamodb = boto3.resource('dynamodb')
devices_table = dynamodb.Table(DEVICES_TABLE_NAME)
logs_table = dynamodb.Table(LOGS_TABLE_NAME)

def aggregate(context, event):
  """
  Handler function
  """
  logger.info(event)  
  devices = devices_table.scan()["Items"]
  current_ts = int(time.time())
  # Get the data of all devices for the last 10 minutes
  log = {"pk": "AGGREGATED_DEVICE", "sk": current_ts, "ttl": current_ts + 90*31*24*3600}
  for device in devices:
    print(device)
    logs_device = logs_table.query(
      KeyConditionExpression = Key("pk").eq(device["pk"]) and Key("sk").between(current_ts - 10*60, current_ts) 
    )["Items"] 
    data = [float(l['value']) for l in logs_device]
    if data: #There are new logs  
      log[f'{device["type"]}_value'] = str(np.round(np.array(data).mean(), 2))
    else:
      log[f'{device["type"]}_value'] = "No data"
  logs_table.put_item(Item=log)
    

  