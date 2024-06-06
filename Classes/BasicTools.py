class BasicTools:

    def __init__(self) -> None:
        pass

    def validate_input_data(self, input_data: list) -> dict:

        is_valid = True
        reason = ""
        data = []

        for i_data in input_data:

            if not type(i_data['value']) is i_data['type']:
                is_valid = False
                reason = f"invalid-{i_data['name']}"
                data.append(f"Type of {i_data['name']} is invalid.")

            if i_data["value"] == "":
                is_valid = False
                reason = f"empty-{i_data["name"]}"
                data.append(f"{i_data["name"]} can't be empty.")

        return {
            'is_valid': is_valid,
            'reason': reason,
            'data': data
        }

    def params(self, name, type, value) -> dict:

        return {
            "name": name,
            "type": type,
            "value": value
        }
