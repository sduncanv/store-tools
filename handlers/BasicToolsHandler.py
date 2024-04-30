# from Classes.BasicTools import BasicTools
from Classes.AwsCognito import AwsCognito


def tools(event, context):

    tools_class = AwsCognito()

    methods = {
        "GET": tools_class.create_user,
    }

    # event['client_id'] = ""
    # event['username'] = "user_prueba_4"
    # event['password'] = "User_prueba_2"
    # event['user_id'] = 2
    # event['created_at'] = "2024-04-29 11:59:08"
    # event['email'] = "correonuevo171201@gmail.com"

    executed = methods.get(event['httpMethod'])
    return executed(event)
