# Passing an arbitrary number of arguments
def make_pizza(*toppings):
    print(toppings)  # print list of arguments
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Preventing a function from modifying original List
num_list = [0, 1, 2, 3, 4]


def change_list(my_list):
    my_list.append("new element")
    print("list from function: "+str(my_list))
change_list(num_list[:])  # passing the copy of the list

print("original list: "+str(num_list))


def build_profile(first, last, **user_info):  # double asterisks create an empty dictionary called user_info
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value  # explicitly adding properties to my dictionary
    return profile
user_profile = build_profile('hammad', 'tariq', location='karachi', field='computer science')
print(user_profile)



