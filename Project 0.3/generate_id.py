import api

def generate_new_id():
    res = api.get_all_expenses()
    if res[0]:
        max_id = 0
        if any(res[1]):
            for i in res[1]:
                max_id = max(max_id, int(i[0]))
    return max_id + 1