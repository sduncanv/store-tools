from Classes.BasicTools import BasicTools


def tools(event, context):

    tools_class = BasicTools()

    methods = {
        "GET": tools_class.tool,
    }

    executed = methods.get(event['httpMethod'])
    return executed(event)
