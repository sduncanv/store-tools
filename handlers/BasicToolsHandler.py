# from Classes.BasicTools import BasicTools
from Classes.AwsCognito import AwsCognito


def tools(event, context):

    tools_class = AwsCognito()

    methods = {
        "GET": tools_class.create_user,
    }

    executed = methods.get(event['httpMethod'])
    return executed(event)
