

def one_to_one(any_lst=None):
    if any_lst is None:
        any_lst = []
    return any_lst == any_lst[::-1]

