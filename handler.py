import subprocess
import json
import sys
sys.path.append("/mnt/efs/lib")
import numpy as np

def hello(event, context):
    subprocess.run(["ls", "-l", "/mnt/efs"])
    subprocess.run(["pwd"])

    arr = np.asarray([1,2,3])
    print(arr)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
