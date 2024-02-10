def decode(
    encoded_str: str,
    base: str = "abcdefghijklmnopqrstuvwxyz234567",
    *args,
    **kwargs
) -> int:
    return sum(
        base.index(constant) * (len(base) ** index)
        for index, constant in enumerate(
            reversed(encoded_str)
        )
    )


def encode(
    decoded_int: int,
    base: str = "abcdefghijklmnopqrstuvwxyz234567",
    *args,
    **kwargs
) -> str:
    base_length = len(base)
    if decoded_int < base_length:
        return base.index(decoded_int)
    encoded = ""
    while decoded_int:
        decoded_int, remainder = divmod(decoded_int, base_length)
        encoded = base[remainder] + encoded
    return encoded




class Base:

    def __init__(
        self,
        base: str = "",
        *args,
        **kwargs
    ) -> None:
        self.base = base or "abcdefghijklmnopqrstuvwxyz234567"

    def decode(
        self,
        encoded_str: str,
        *args,
        **kwargs
    ) -> int:
        return decode(
            encoded_str=encoded_str,
            base=self.base,
            *args,
            **kwargs
        )

    def encode(
        self,
        decoded_int: int,
        *args,
        **kwargs
    ) -> str:
        return encode(
            decoded_int=decoded_int,
            base=self.base,
            *args,
            **kwargs
        )
