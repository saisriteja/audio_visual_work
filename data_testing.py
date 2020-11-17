import pickle
import numpy as np

def load_obj(name ):
    with open(name , 'rb') as f:
        return pickle.load(f)


f = 'D:\\projects\\my_works\\facial emotion recognition\\savee-database_working\\data\\DC_a1'

data = load_obj(f)
print(data.shape)