from jsonschema import validate
from jsonschema.exceptions import ValidationError

from parser_currency_rate import get_list_letters_code_currency

list_letters_code_currency = get_list_letters_code_currency()
schema_POST_request = {
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


async def validate_json_data_post_request(json_data):
    try:
        validate(json_data, schema_POST_request)
        return True
    except ValidationError:
        return False


async def validate_get_request(currency):
    if currency in list_letters_code_currency:
        return True
    return False
