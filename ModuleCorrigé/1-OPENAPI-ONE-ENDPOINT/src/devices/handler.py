import json

def get_devices(context, event):
  print("Ok")
  return {
    "statusCode": 400,
    "body": json.dumps([{"id": "a", "devType": "co2"}]),
    "headers": {'Access-Control-Allow-Origin': '*'}
  }