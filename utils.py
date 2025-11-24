def validate_string(value, *, name, min_len=1, max_len=None):
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a string")

    value = value.strip()
    if len(value) < min_len:
        raise ValueError(f"{name} must be at least {min_len} character(s) long")

    if max_len is not None and len(value) > max_len:
        raise ValueError(f"{name} must be at most {max_len} character(s) long")

    return value


def validate_price(value, *, name="price", minimum=1.0, maximum=10.0):
    try:
        price = float(value)
    except Exception:
        raise TypeError(f"{name} must be a number")

    if price < minimum or price > maximum:
        raise ValueError(f"{name} must be between {minimum} and {maximum}")

    return price
