import boto3

client_cognito = boto3.client('cognito-idp')

userpool = 'us-east-1_tQ9bXGlsg'
clientid = '1pmns354aqurskq5mj7n381qur'

username = "user_prueba_4"
password = "User_prueba_2"
email = "correonuevo171201@gmail.com"

# res = client_cognito.sign_up(
#     ClientId=clientid,
#     Username=username,
#     Password=password,
#     UserAttributes=[
#         {"Name": "email", "Value": email}
#     ]
# )

res = client_cognito.confirm_sign_up(
    ClientId=clientid,
    Username=username,
    ConfirmationCode="894482"
)

# print(res)

# response = client_cognito.admin_initiate_auth(
#     UserPoolId=userpool,
#     ClientId=clientid,
#     AuthFlow='REFRESH_TOKEN_AUTH',
#     AuthParameters={
#         'REFRESH_TOKEN': access_token
#     }
# )

# res = client_cognito.initiate_auth(
#     AuthFlow='USER_PASSWORD_AUTH',
#     ClientId=clientid,
#     AuthParameters={
#         'USERNAME': username,
#         'PASSWORD': password
#     }
# )


# res = client_cognito.initiate_auth(
#     ClientId=clientid,
#     AuthFlow='USER_PASSWORD_AUTH',
#     AuthParameters={
#         'USERNAME': username,
#         'PASSWORD': password
#     }
# )

print(res)
