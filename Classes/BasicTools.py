class BasicTools:

    def __init__(self) -> None:
        pass

    def validate_input_data(self, input_data: list) -> dict:

        errors = []

        for i_data in input_data:

            name, expected_type, value = (
                i_data['name'], i_data['type'], i_data['value']
            )

            if not isinstance(value, expected_type):
                errors.append(
                    f"Type of {name} is invalid. "
                    f"Expected {expected_type.__name__}."
                )

            if isinstance(value, str) and not value.strip():
                errors.append(f"{i_data['name']} can't be empty.")

        return {
            'is_valid': not errors,
            'errors': errors
        }

    def params(self, name, type, value) -> dict:

        return {
            "name": name,
            "type": type,
            "value": value
        }
