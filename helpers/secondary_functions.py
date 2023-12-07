def validate_attribute(attribute: int, min_val: int, max_val: int or float, message: str) -> None:
    bool_val = min_val <= attribute <= max_val
    if bool_val is False:
        raise ValueError(message)