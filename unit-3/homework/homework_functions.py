def reverse_list(lists):
    return lists[::-1]



def encode_string(string):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    results = ""
    for character in string:
        for idx in range(len(letters)):
            if character == letters[idx]:
                results += str(idx + 1)
    return results 


def pivot_split(my_list, my_num):
    left = []
    right = []
    for num in my_list:
        if num < my_num:
            left.append(num)
        else:
            right.append(num)
    return [left, right]

'''
def is_isogram(string):
'''

