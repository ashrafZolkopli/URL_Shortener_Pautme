from string import ascii_lowercase


def base_decode(encoded_str: str, base: str = ascii_lowercase + "234567", *args, **kwargs) -> int:
    return sum(
        base.index(constant) * (len(base) ** index)
        for index, constant in enumerate(
            reversed(encoded_str)
        )
    )


def base_encode(decoded_int: int, base: str = ascii_lowercase + "234567", *args, **kwargs) -> str:
    base_length = len(base)
    if decoded_int < base_length:
        return base.index(decoded_int)
    encoded = ""
    while decoded_int:
        decoded_int, remainder = divmod(decoded_int, base_length)
        encoded += base.index(remainder)

    return encoded


