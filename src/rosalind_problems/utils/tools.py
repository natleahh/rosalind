""""""

def apply_types(types: tuple[type], raw_data: tuple[str]):
    """"""
    return tuple(t(d) for t, d in zip(types, raw_data))

def join_lines(xs: list):
    """"""
    return "\n".join(map(str, xs))
