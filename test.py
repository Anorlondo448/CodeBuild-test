import boto3
from time import sleep
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# S3
BUCKET_NAME = "anorlondo-test"
TARGET_DIR = "batch"
FILE_CONTENTS = ""

# Time
MAX_TIMER = 5
SEC = 1


def PutS3(i):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    filename = str(i+1) + "番目"

    obj = bucket.put_object(ACL='private', Body=FILE_CONTENTS, Key=TARGET_DIR + "/" + filename, ContentType='test/plain')
    return str(obj)

def count(count):
    print("{}秒経過しました".format((count+1)*SEC))

for i in range(MAX_TIMER):
    sleep(SEC)
    count(i)
    PutS3(i)
    
    