import boto3


class AwsCognito:

    def __init__(self):
        pass

    def create_user(self, **kwargs) -> dict:

        # kwargs = {
        #     'client_id': '3f7engqga332prsh099an7g1tk',
        #     'username': 'user_prueba_2',
        #     'password': 'User_prueba_2',
        #     'user_id': "2",
        #     'created_at': "2024-04-29 11:59:08",
        #     'email': "correonuevo171201@gmail.com8"
        # }

        client_cognito = boto3.client('cognito-idp', region_name='us-east-1')

        result = client_cognito.sign_up(
            ClientId=kwargs['client_id'],
            Username=kwargs['username'],
            Password=kwargs['password'],
            UserAttributes=[
                {"Name": "email", "Value": kwargs['email']}
            ]
        )

        print(result)

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
