import math
from itertools import permutations

letters = 'abcdefghijklmnoqrstuwxy'
letters = list(letters)

# set data path
data_path = r'data\Abdalla_Mansuur_Dictionary'

# this function grap all data
def get_all_words():
    all_words = []
    for letter in letters:
        path = data_path+f'\\letter_{letter.upper()}_.txt'
        with open(path) as file:
            contents = file.readlines()
            for word in contents:
                all_words.append(word.strip("\n"))
    return all_words
        
#print("Original len:", len(get_all_words()))

# Step 2 Data Reduction (1) By word len
def reduce_words_by_len(data, word):
    print("In reduce_words_by_len", len(data))
    reduced_by_word_len = []
    for word1 in data:
        if len(word1) == len(word):
            reduced_by_word_len.append(word1)
    #print("After reduce_words_by_len:", len(reduced_by_word_len))
    # Now the data is the same len
    return reduced_by_word_len

# this function return true if all elements in str1 are found in str2
def count_chars(str1, str2):
    str1_chars_freq = {}
    str2_chars_freq = {}
    for str1_char, str2_char in zip(str1, str2):
        #print("str1: ",str1_char, "str2: ", str2_char )
        str1_chars_freq[str1_char] = str1.count(str1_char)
        str2_chars_freq[str2_char] = str2.count(str2_char)
    #print(str1_chars_freq)
    #print(str2_chars_freq)
    return str2_chars_freq == str1_chars_freq

# Step 3 Reduction (1) By word chars
# We need chars in searched str at the same time in word list
def reduce_word_by_chars(data, word):
    print("In reduce_word_by_chars:", len(data))
    reduced_by_chars = []
    # Regardles lower or uppercase
    for word1 in data:
        #if minSubStr(word, word1):
        if count_chars(word1, word):
            reduced_by_chars.append(word1)
    #print("After reduce_word_by_chars:", len(reduced_by_chars))
    #print("After reduce_word_by_chars:", reduced_by_chars)
    return set(reduced_by_chars)

''' TEST PHASE'''
# 1 get data
data = get_all_words()



# Step 5: Find the similarities
def arrange_word(word, data):
    #print(f"1----------{len(data)}")
    # 2 sort by len
    #sorted_data = sort_by_len(data)
    #print(f"2----------{len(sorted_data)}")
    # 3 reduction 1
    len_reduction = reduce_words_by_len(data, word)
    #print(f"3----------{len(len_reduction)}")
    # 4 reduction 2
    result = reduce_word_by_chars(len_reduction, word)
    #print(f"4----------{len(char_reduction)}")
    # find intersection
    #auto_gen_words = [''.join(p) for p in permutations(word)]
    # print(f"Posible words {math.factorial(len(word))}")
    #result = set(auto_gen_words) & set(data)
    return result


#print(sort_by_len(["a", "fdsfd", "33", "ddew", "f", "cvf", "xc", "v", "a"]))
#print(sort_by_len(["dsfgd", "refgdftgdfg", "6", "v", "ddes", "ggxdsdgdrtg", "uyrrfesrfdresew", "v", "bg"]))
# [a, f, v, a, 33, xv, cvf, ddew, fdsfd]



#print(arrange_letters("nuyan", data)) # aynuu
#print(arrange_letters("ayoa", data)) # aynuu
#print(arrange_letters("irosoa", data)) # aroosi
#print(arrange_letters("fara", data))  # afar
#print(arrange_letters("riksha", data)) # akhris
#print(arrange_letters("a", data)) # afayso
#print(arrange_letters("muasa", data)) # afayso
#print(arrange_letters("yawaa", data)) # afayso
#print(arrange_letters("dayaa", data)) # afayso
#print(arrange_letters("yasaa", data)) # afayso
# while True:
#     word = input("Geli erey: ")
#     #print(len(data))
#     print(arrange_letters(word, data)) # afayso
#arrange_letters(contents2, "nuyan")
#arrange_letters(contents2, "aroosi")

