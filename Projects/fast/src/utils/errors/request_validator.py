from pydantic import ValidationError
from src.utils.errors.error_decorator import ErrorDecorator
from src.utils.constants.constants import Constants

class RequestValidator:
    def __init__(self, schema, body):
        try:
            schema(**body)
        except ValidationError as e:
            raise ErrorDecorator(name=f"Validation Error: {e.errors()}", status=Constants.StatusCodes.BAD_REQUEST)