def do(nums, bases):
    sizes = _max_size_for_each_base(nums, bases)
    nums_in_all_bases = [_in_each_base(n, bases, sizes)
                         for n in nums]
    return [" ".join(num) for num in nums_in_all_bases]


def _max_size_for_each_base(nums, bases):
    m = max(nums)
    return [b.size(m) for b in bases]


def _in_each_base(n, bases, sizes):
    return [b.to_str(n, sz) for b, sz in zip(bases, sizes)]
