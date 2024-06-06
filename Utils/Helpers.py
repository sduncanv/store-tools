import json
import traceback
import sys
from copy import copy
from typing import Union, Tuple
from sqlalchemy.exc import OperationalError
from botocore.exceptions import ClientError
from Tools.Classes.CustomError import CustomError


def response_format(statusCode, message='Ok', data=[]):

    body = {
        'statusCode': statusCode,
        'message': message
    }

    if data:

        body['data'] = data['data']
        body['statusCode'] = data['statusCode']

    response = {
        'statusCode': statusCode,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        },
        'body': json.dumps(body)
    }

    return response


def exception_decorator(function):

    def validations(*args, **kwargs):

        result = []
        statusCode = 200
        message = 'Ok'

        try:
            result = function(*args, **kwargs)

        except TypeError as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = 'Internal server error'

        except AssertionError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except KeyError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except AttributeError as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = e.args[0]

        except ValueError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except ClientError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = e.args[0]

        except CustomError as e:

            print(e)
            read_exception_message()

            statusCode = 400
            message = str(e)

        except OperationalError as e:

            print(e)
            print(type(e))
            read_exception_message()

            statusCode = 400
            print(e.args[0])
            message = str(e)

        except Exception as e:

            print(e)
            read_exception_message()

            statusCode = 500
            message = 'Internal server error'

        return response_format(statusCode, message, result)

    return validations


def read_exception_message():

    exception_type, exception_object, exception_stack = sys.exc_info()

    filename, line, function, code = traceback.extract_tb(
        exception_stack
    )[-1]

    path = filename.split("\\")[-2::]

    print(f"""
        path: {path},
        line: {line},
        function: {function},
        code: {code}
    """)


def get_input_data(
    event: dict, default_http_method: str = 'POST'
) -> Union[dict, any]:

    input_method = {
        'POST': get_post_data,
        'GET': get_querystringparameters_data,
        'PUT': get_post_data,
        'DELETE': get_querystringparameters_data,
    }

    path, http_method = get_path(event)
    method = http_method or default_http_method
    assert method.upper() in input_method.keys(), "Invalid HTTP method."

    return input_method[method.upper()](event)


def _get_input_data(event: dict, key: str) -> Union[dict, any]:

    data = {}
    if type(event) is dict and key in event.keys():
        data = copy(event[key])
        if not type(data) is dict:
            try:
                data = json.loads(data)
            except Exception:
                data = {}
    return data


def get_post_data(event: dict) -> Union[dict, any]:

    return _get_input_data(event, 'body')


def get_querystringparameters_data(event: dict) -> Union[dict, any]:

    return _get_input_data(event, 'queryStringParameters')


def get_path(event: dict) -> Tuple[str, str]:

    if type(event) is dict:
        return event.get('path', ''), event.get('httpMethod', '')

    return None, None
