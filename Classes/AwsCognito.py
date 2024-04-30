import boto3

from Tools.Utils.Helpers import exception_decorator


class AwsCognito:

    def __init__(self):
        pass

    @exception_decorator
    def create_user(self, data) -> dict:

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.sign_up(
            ClientId=data['client_id'],
            Username=data['username'],
            Password=data['password'],
            UserAttributes=[
                {"Name": "email", "Value": data['email']}
            ]
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')

        return {'statusCode': status_code, 'data': result}

    @exception_decorator
    def authenticate_user(self, data) -> dict:

        print(data)

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.confirm_sign_up(
            ClientId=data['client_id'],
            Username=data['username'],
            ConfirmationCode=data['code']
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')

        return {'statusCode': status_code, 'data': result}

    @exception_decorator
    def get_token_by_user(self, data) -> dict:

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            ClientId=data['client_id'],
            AuthParameters={
                'USERNAME': data['username'],
                'PASSWORD': data['password']
            }
        )

        status_code = result.get('ResponseMetadata', '').get('HTTPStatusCode', '')
        result = result.get('AuthenticationResult', '')

        return {'statusCode': status_code, 'data': result}
