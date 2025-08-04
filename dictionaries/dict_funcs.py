MY_DICT = {"pizza": 45,
           "pasta": 50,
           "cola": 10}

print(MY_DICT) # Display dictionary

# create, update
def create_dict(key, value):
    data = MY_DICT[key] = value
    return f"{key} {value} has been added"

# search
def search_dict(key):
    if key in MY_DICT:
        return f"{key} is in dictionary and value is {MY_DICT[key]}"
    else:
        return f"key: {key} not found"

# x = create_dict("coffee", 5)
# print(x)
#
# y = search_dict("cola")
# print(y)

def replace_dict(key, value):
    if key in MY_DICT:
        MY_DICT[key] = value
        return f"{key}'s value is {value}"
    else:
        return f"key: {key} not found"


def delete_element(key):
    if key in MY_DICT:
        del MY_DICT[key]
        return f"{key} has been deleted"
    else:
        return f"{key} not found"