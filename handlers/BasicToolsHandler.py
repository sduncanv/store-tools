from Classes.BasicTools import BasicTools
# from Classes.AwsCognito import AwsCognito


def tools(event, context):

    # tools_class = AwsCognito()
    tools_class = BasicTools()

    methods = {
        "GET": tools_class.tool,
        "POST": tools_class.tool,
    }

    executed = methods.get(event['httpMethod'])
    return executed(event)
