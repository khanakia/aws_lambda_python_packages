import json
from web3 import Web3

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': Web3.toText(0x636f776dc3b6),
        'body': json.dumps('Hello from Lambda!')
    }