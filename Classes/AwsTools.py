import boto3
from botocore.exceptions import ClientError
from Tools.Utils.Helpers import exception_decorator
from Tools.Classes.CustomError import CustomError


class AwsTools:

    def __init__(self):
        pass

    @exception_decorator
    def upload_file(self, data: dict) -> dict:

        s3_client = boto3.client('s3')

        try:
            response = s3_client.put_object(
                Body=data['file'],
                Bucket=data['bucket_name'],
                Key=data['filename']
            )

            print(f'{response} ....')

        except ClientError as e:
            raise CustomError(f'Error: {e}')

        status_code = response['ResponseMetadata']['HTTPStatusCode']
        data = response

        return {'statusCode': status_code, 'data': data}
