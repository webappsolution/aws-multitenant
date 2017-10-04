# -----------------------------------------------------------------------------------------
# MIT No Attribution
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# -----------------------------------------------------------------------------------------
import json
import boto3
import cfnresponse
import requests

s3 = boto3.resource('s3')

def create(properties, physical_id):
  #Example Code for Completeing a GET or POST JSON HTTP Request Using a Lambda Custom CloudFormation Resource
  domain = properties['Domain']
  print domain
  path = properties['Path']
  print path
  protocol = properties['Protocol']
  print protocol
  method = properties['Method']
  print method
  body = properties['Body']
  print body

  url = protocol + domain + path
  print url
  if method == 'POST':
    print 'POST'
    payload = json.loads(body)
    print type(payload)
    print payload

    r = requests.post(url, data=payload)
    print 'Response Status Code'
    print r.status_code
    if (r.status_code == 200) or (r.status_code == 504):
      print 'SUBMITTED POST REQUEST'
      return cfnresponse.SUCCESS, None
  elif method == 'GET':
    print 'GET'
    r = requests.get(url)
    print 'Response Status Code'
    print r.status_code
    if r.status_code == 200:
      print r.json()
      print 'GET REQUEST COMPLETED'
      return cfnresponse.SUCCESS, None
  elif method == 'DELETE':
    print 'DELETE'
    r = requests.delete(url)
    print 'Response Status Code'
    print r.status_code
    if r.status_code == 200:
      print 'DELETE REQUEST COMPLETED'
      return cfnresponse.SUCCESS, None
  else:
    print 'INVALID REQUEST METHOD'

def update(properties, physical_id):
  return create(properties, None)

def delete(properties, physical_id):
  print 'Deleting Stack'
  return cfnresponse.SUCCESS, None

def handler(event, context):
  print "Received event: %s" % json.dumps(event)

  status = cfnresponse.FAILED
  new_physical_id = None

  try:
    properties = event.get('ResourceProperties')
    physical_id = event.get('PhysicalResourceId')

    status, new_physical_id = {
      'Create': create,
      'Update': update,
      'Delete': delete
    }.get(event['RequestType'], lambda x, y: (cfnresponse.FAILED, None))(properties, physical_id)
  except Exception as e:
    print "Exception: %s" % e
    status = cfnresponse.FAILED
  finally:
    cfnresponse.send(event, context, status, {}, new_physical_id)
