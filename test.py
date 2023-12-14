import os
import pickle
from functions import *

CURRENT_PATH = os.getcwd()

# username = 'gdsai4903'
# password = 'Gdsai@123'
# student_id = '123456'
# user_data = {username: {'password': password,
#                         'student id': 0}}

user_data = read_data(CURRENT_PATH, 'data/user_data.pickle')
# # idd = {'student id': student_id}

# user_data[502156]['status'] = 'Candidate'

# # data[username].update(idd)
# user_data = {}

print(user_data)
# # with open(os.path.join(CURRENT_PATH, 'user_data.pickle'), 'wb') as f:
# #     pickle.dump(user_data, f)

save_data(user_data, CURRENT_PATH, 'data/user_data.pickle')

# class parent():
#     def print_hello(self):
#         print("hello I'm parent")

# class child(parent):
#     def __init__(self):   
#         super().print_hello()

# child()
# print_long_message("WARNING", 'please choose a stronger password, it must contain: an uppercase, a lowercase, a number and, a special character and must be atleast 8 characters long', 55)
