listA = [5, 10, 15, 20, 25]


def make_new_list(param):
    new_list = []
    list_length = len(param)
    first_in_list = param[0]
    last_in_list = param[list_length - 1]
    new_list.append(first_in_list)
    new_list.append(last_in_list)
    print(list_length)
    print(first_in_list)
    print(last_in_list)
    print(new_list)


make_new_list(listA)


def list_ends(param_a):
    return [param_a[0], param_a[len(param_a) - 1]]


print(list_ends(listA))
