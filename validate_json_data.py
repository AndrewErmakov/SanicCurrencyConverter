from jsonschema import validate
from parser_currency_rate import get_list_letters_code_currency
from jsonschema.exceptions import ValidationError


async def validate_json_data_post_request(json_data):
    try:
        list_letters_code_currency = await get_list_letters_code_currency()
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

        validate(json_data, schema_POST_request)
        return True
    except ValidationError:
        return False


async def validate_get_request(currency):
    list_letters_code_currency = await get_list_letters_code_currency()
    if currency in list_letters_code_currency:
        return True
    return False


