import boto3
from botocore.exceptions import ClientError


def exception_aws_cognito(function):
    """
    Decorator to handle exceptions for AWS Cognito functions.
    """

    def wrapper(self, *args, **kwargs):
        try:
            result = function(self, *args, **kwargs)
            status_code = result.get('ResponseMetadata', {}).get(
                'HTTPStatusCode', '')
            return {'statusCode': status_code, 'data': result}

        except ClientError as e:
            return {'statusCode': 400, 'data': str(e)}

    return wrapper


class AwsCognito:

    def __init__(self):
        self.client_cognito = boto3.client(
            'cognito-idp', region_name='us-east-2'
        )

    @exception_aws_cognito
    def create_user(self, data: dict) -> dict:

        result = self.client_cognito.sign_up(
            ClientId=data['client_id'],
            Username=data['username'],
            Password=data['password'],
            UserAttributes=[
                {'Name': 'email', 'Value': data['email']},
            ]
        )

        return result

    @exception_aws_cognito
    def authenticate_user(self, data: dict) -> dict:

        result = self.client_cognito.confirm_sign_up(
            ClientId=data['client_id'],
            Username=data['username'],
            ConfirmationCode=data['code']
        )

        return result

    @exception_aws_cognito
    def get_token_by_user(self, data: dict) -> dict:

        result = self.client_cognito.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            ClientId=data['client_id'],
            AuthParameters={
                'USERNAME': data['username'],
                'PASSWORD': data['password']
            }
        )

        result = result.get('AuthenticationResult', '')
        return result
