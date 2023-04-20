'''
author:lance.lan
date:2023/4/20
project:demo.py.txt
'''
def find_max_sum_method(list_test):
    list_test.sort(reverse=True)
    return list_test[0]+list_test[1]

print(find_max_sum_method([1,2,3]))