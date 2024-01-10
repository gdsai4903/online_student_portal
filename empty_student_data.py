import os
from functions import *

# Getting the path to the current working directory.
CURRENT_PATH = os.getcwd()

student_dict = read_data(CURRENT_PATH, 'data/student_data.pickle')

student_dict[569228]['status'] = 'Candidate'

save_data(student_dict, CURRENT_PATH, 'data/student_data.pickle')