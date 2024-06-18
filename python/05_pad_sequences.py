import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.system("clear")



import numpy as np
import pprint as pp
from tensorflow.keras.preprocessing.sequence import pad_sequences

comment1 = [1, 2, 3, 4]
comment2 = [1, 2, 3, 4, 5, 6, 7]
comment3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_train = np.array([comment1, comment2, comment3], dtype = object)
print(), pp.pprint(x_train)

#unsert 0 to left of array to make array have same length
x_test =  pad_sequences(x_train)
print(), pp.pprint(x_test)

#insert specific Value to array to make array have same length
x_test =  pad_sequences(x_train, value = 255)
print(), pp.pprint(x_test)

#insert 0 to right of array to make array have same length
x_test =  pad_sequences(x_train, padding = "post")
print(), pp.pprint(x_test)

#Cut the array, only remain last 3 element
x_test =  pad_sequences(x_train, maxlen = 3)
print(), pp.pprint(x_test)


#Cut the array, only reamin head of 3 element
x_test =  pad_sequences(x_train, maxlen = 3, truncating = "post")
print(), pp.pprint(x_test)