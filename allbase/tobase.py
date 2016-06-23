def do(nums, bases):

    nums_in_all_bases = [[b.to_str(n) for b in bases] for n in nums]
    """ for each number, join its representation in different bases
        in a single string using spaces """
    return [" ".join(num) for num in nums_in_all_bases]
