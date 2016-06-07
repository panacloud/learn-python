# Importing an entire module
import file1

print(file1.user_name('hammad'))
print(file1.user_dob(day=22, year=1993, month='April'))


# Using as to give a Module an Alias
import file1 as my_user

print(my_user.user_name('hammad'))
print(my_user.user_dob(day=22, year=1993, month='April'))


# Importing specific functions
from file1 import user_name, user_dob

print(user_name('hammad'))
print(user_dob(day=22, year=1993, month='April'))


# Using as to give a Function an Alias
from file1 import user_name as u_name, user_dob as u_dob

print(u_name('hammad'))
print(u_dob(day=22, year=1993, month='April'))


# importing all functions
from file1 import *

print(file1.user_name('hammad'))
print(file1.user_dob(day=22, year=1993, month='April'))
