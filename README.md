# store-tools

Repository of common tools and utilities used by the main application's microservices. This code isn't executed directly, but is consumed as a dependency by:

- [`store-users`](https://github.com/sduncanv/store-users)
- [`store-products`](https://github.com/sduncanv/store-products)

### Repository-specific technologies

- SQLAlchemy
- PyMySQL
- setuptools
- boto3
- cloudinary
- python-dotenv

### Project structure

```
.
├── Classes
│   ├── __init__.py
│   ├── AwsCognito.py
│   ├── AwsTools.py
│   ├── BasicTools.py
│   ├── CustomError.py
├── Database
│   ├── __init__.py
│   ├── Conn.py
├── Models
│   ├── __init__.py
├── Utils
│   ├── __init__.py
│   ├── Helpers.py
│   ├── QueryTools.py
├── .env
├── .gitignore
├── locked-requirements.txt
├── pyproject.toml
├── README.md
├── script.py
├── serverless.yml
├── setup.py
```


### Classes
### AwsCognito

| Methods | Description | Params | Return |
|---|---|---|---|
| `create_user` | Create a new user in Cognito Aws  | `data: dict`  | `dict`: state of creation |
| `authenticate_user` | Confirm user with code sent by AWS | `data: dict` | `dict`: result |
| `get_token_by_user` | Authenticates user in Cognito and returns tokens | `data: dict`| `dict`: tokens |

### AwsTools

| Methods | Description | Params | Return |
|---|---|---|---|
| `upload_file` | Upload a file to S3 Aws | `data: dict` | `dict`: uploading status |

### BasicTools

| Methods | Description | Params | Return |
|---|---|---|---|
| `params` | Returns the input data in a dict | `data: dict` | `dict`: dict key:value |
| `validate_input_data` | Validate the list of dictionaries built in the **params** method | `input_data: list` | `dict`: is_valid: True means that the data is correct |
