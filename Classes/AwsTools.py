import boto3
from botocore.exceptions import ClientError
from Tools.Classes.CustomError import CustomError


class AwsTools:

    def __init__(self):
        pass

    # @exception_decorator
    def upload_file(self, data: dict) -> dict:

        try:
            s3_client = boto3.client('s3')

            response = s3_client.put_object(
                Body=data['file'],
                Bucket=data['bucket_name'],
                Key=data['filename']
            )

        except ClientError as e:
            raise CustomError(f'Error: {e}')

        status_code = response['ResponseMetadata']['HTTPStatusCode']

        return {'statusCode': status_code, 'data': response}
