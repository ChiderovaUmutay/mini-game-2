def validate_attribute(attribute: int or list, min_val: int, max_val: int or float, message: str) -> None:
    validate_data = len(attribute) if isinstance(attribute, list) else attribute
    bool_val = min_val <= validate_data <= max_val
    if bool_val is False:
        raise ValueError(message)


def display(message: str) -> None:
    print(message)