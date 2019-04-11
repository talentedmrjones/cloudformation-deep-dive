import boto3
import urllib2
import json

class RequestWithMethod(urllib2.Request):
    def __init__(self, *args, **kwargs):
        self._method = kwargs.pop('method', None)
        urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self):
        return self._method if self._method else super(RequestWithMethod, self).get_method()


def lambda_handler(event, context):

    print(event)

    TableName=event['ResourceProperties']['TableARN'].split('table/')[-1]

    client = boto3.client('dynamodb')

    cities = {
        '80014':'Denver',
        '80304':'Boulder',
        '32601':'Gainesville',
        '81601':'Glenwood Springs'
    }

    print('Populating table')

    for zip in cities:

        response = client.put_item(
            TableName=TableName,
            Item={
                'zip': {
                    'S': zip
                },
                'city':{
                    'S': cities[zip]
                }
            }
        )

    customResponse = {
       "Status" : "SUCCESS",
       "PhysicalResourceId" : "None",
       "StackId" : event['StackId'],
       "RequestId" : event['RequestId'],
       "LogicalResourceId" : event['LogicalResourceId']
    }
    opener = urllib2.build_opener(urllib2.HTTPHandler)

    request = RequestWithMethod(event['ResponseURL'], method='PUT', data=json.dumps(customResponse))
    opener.open(request)

    return {}
