import boto3

from Tools.Database.Database import Database


class AwsCognito:

    def __init__(self) -> None:
        self.db = Database()

    def create_user(self, **kwargs) -> dict:

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.sign_up(
            ClientId=kwargs['client_id'],
            Username=kwargs['username'],
            Password=kwargs['password'],
            UserAttributes=[
                {"Name": "user_id", "Value": kwargs['user_id']},
                {"Name": "created_at", "Value": kwargs['created_at']}
            ]
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')

        return {'statusCode': status_code, 'data': result}

    def authenticate_user(self, **kwargs) -> dict:

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.confirm_sign_up(
            ClientId=kwargs['client_id'],
            Username=kwargs['username'],
            ConfirmationCode=kwargs['code']
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')

        return {'statusCode': status_code, 'data': result}

    def get_token_by_user(self, **kwargs) -> dict:

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            ClientId=kwargs['client_id'],
            AuthParameters={
                'USERNAME': kwargs['username'],
                'PASSWORD': kwargs['password']
            }
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')
        result = result.get('AuthenticationResult', '')

        return {'statusCode': status_code, 'data': result}
