from Classes.Login import Login


def login(event, context):

    login_class = Login()

    methods = {
        "POST": login_class.login,
    }

    executed = methods.get(event['httpMethod'])
    return executed(event)
