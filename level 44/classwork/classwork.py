# 1)
def swap_values(args):
    return args.reverse()


# 2)
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
        

#3)

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# 4)
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
        