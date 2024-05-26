#!/usr/bin/env python3
num_list = [0, 1, 3, 5, 7, 8, 9]
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

print(return_evens(num_list))
    
sentence_list = ["Hello", "I'm doing great", "Python is fun"]
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]    

print(make_exclamation(sentence_list))    
