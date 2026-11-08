# sentence = """
# this is the program to find the longest word in the program
# """

# splitted = sentence.split()

# max_letter=" "
# for i in range(len(splitted)):
#     for j in range(len(splitted)):
#         if len(splitted[i]) > len(splitted[j]):
#             if len(splitted[i])>len(max_letter):
#                 max_letter=splitted[i]

# print(max_letter)

# sentence = """
# this is the program to find the duplicate word in the program without changing the order
# """
# splitted = sentence.split()

# rm_sentence = []
# for split in splitted:
#     if split not in rm_sentence:
#         rm_sentence.append(split)

# result = ' '.join(rm_sentence)
# print(sentence)
# print(result)

#program to shift all zero to end without changing the order
# list = [1,0,2,0,3,0,4,0,5]
# count =0
# for el in list:
#     if el == 0:
#         list.remove(0)
#         count += 1

# for i in range(count):
#     list.append(0)
                
# print(list)

# tar = 10
# list = [1,4,5,3,5,3,6,3]

# dict ={}

# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i]+list[j] == 10:
#             dict[list[i]] = list[j]
# print(dict)

# list = [1,2,3,4,5,6]
# k = 4
# for i in range(k):
#     store=list.pop()
#     list.insert(0,store)

# print(list)

list = [1,2,3,5,6,8,9,10,14,15]

unavailable = []
for i in range(len(list)-1):
        if list[i]+1 == list[i+1]:  #CLOSE BUT NO CIGAR
            continue
        else:
            unavailable.append(list[i]+1)

print(unavailable)
