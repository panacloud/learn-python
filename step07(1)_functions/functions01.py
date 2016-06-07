def greet_user(user):
    print("Hello "+str(user)+"!")
greet_user("Hammad")


# arrangement of arguments matter so don't mix them up
def greet_user_fullname(firstname,lastname):
    print("Hello "+firstname+" "+lastname)
greet_user_fullname("Hammad","Tariq")


# arrangement of params doesn't matter if value assign explicitly
def user_dob(day, month, year):
    return str(day)+':'+str(month)+":"+str(year)
birthday = user_dob(day=22, year=1993, month='April')
print(birthday)  # prints 22:April:1993


# explicitly assigning values to function argument
def greet_user_fullname2(firstname,lastname):
    print("Hello "+firstname+" "+lastname)
greet_user_fullname2(firstname="Hammad", lastname="Tariq")  # use same names of parameters in the function’s definition.


# add optional param by assigning it an empty string.
# optional param can only be listed last in the definition.
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
fullname = get_formatted_name('hammad', 'tariq')
print(fullname)


