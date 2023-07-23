def get_sum(num):
    if len(num) == 1:
        return num[0]
    else:
        return num[0] + get_sum(num[1:])

print(get_sum([1,2,3,4]))