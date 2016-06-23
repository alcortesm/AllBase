def do(nums, bases):

    """ list of numbers, each of it a list of the number in different bases """
    nums_in_bases = [[b.to_str(n) for b in bases] for n in nums]
    """ for each number, join its representation in different bases """
    return [" ".join(num) for num in nums_in_bases]
