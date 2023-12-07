def validate_attribute(attribute, min_val, max_val, message):
    bool_val = min_val <= attribute <= max_val
    if bool_val is False:
        raise ValueError(message)