from jsonschema import validate
from jsonschema.exceptions import ValidationError

from parser_currency_rate import get_list_letters_code_currency

list_letters_code_currency = get_list_letters_code_currency()
schema = {
    "type": "object",
    "properties": {
        "from_currency": {
            "type": "string",
            "enum": list_letters_code_currency
        },
        "to_currency": {
            "type": "string",
            "enum": list_letters_code_currency
        },
        "amount": {
            "type": "number",
            "minimum": 0.0,
        }
    }
}


async def validate_json_data(json_data):
    try:
        validate(json_data, schema)
        return True
    except ValidationError:
        return False
