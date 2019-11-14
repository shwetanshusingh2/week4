import boto3


s3_client = boto3.resource('s3')
SOURCE_BUCKET = "data-shwet"
TEMPLATE_NAME = "template.yaml"

LAMBDA_PYTHON_FILE = "lambda_trigger.py"
LAMBDA_ZIP_FILE = "lambda_trigger.zip"
STACK_NAME = "demo"
lambda_version = ""
CLIENT = boto3.client('cloudformation')
UPLOAD_OBJECT_BUCKET = "shwet23"
TEMPLATE_URL = 'https://data-shwet.s3.ap-south-1.amazonaws.com/template.yaml'
GLUE_CLIENT = boto3.client('glue')
ATHENA_CLIENT = boto3.client('athena')
S3_OUTPUT = 's3://shwet2/output'
DATABASE = 'dbcrawler'
QUERY = 'SELECT * FROM "dbcrawler"."csv" limit 10'