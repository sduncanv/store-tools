import boto3
from botocore.exceptions import ClientError
from Tools.Utils.Helpers import exception_decorator
from Tools.Classes.CustomError import CustomError


class AwsTools:

    def __init__(self):
        pass

    @exception_decorator
    def create_user(self, data) -> dict:

        s3_client = boto3.client('s3')

        try:
            response = s3_client.put_object(
                Body=data['file'],
                Bucket=data['bucket_name'],
                Key=['filename']
            )

            print(f'{response} ....')

        except ClientError as e:
            raise CustomError(f'Error: {e}')

        status_code = response['ResponseMetadata']['HTTPStatusCode']
        data = response

        return {'statusCode': status_code, 'data': data}
