def to_bases(n, bases):
    in_base_form = [b.to_str(n) for b in bases]
    return " ".join(in_base_form)
