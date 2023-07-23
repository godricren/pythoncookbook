# def compare_letters(string1, string2):
#     string2_list = list(string2)
#     pos1 = 0
#     keep_comparing = True
#     while pos1<len(string1) and keep_comparing:
#         pos2 = 0
#         found = False
#         while pos2 < len(string2_list) and not found:
#             if string1[pos1] == string2_list[pos2]:
#                 found = True
#             else:
#                 pos2 += 1
#         if found:
#             string2_list[pos2] = None
#         else:
#             keep_comparing = False
#         pos1 += 1
#     return keep_comparing

def compare_letters(string1, string2):
    string2 = list(string2)
    index1 = 0
    is_same = True
    while index1<len(string1) and is_same:
        index2 = 0
        found = False
        while index2<len(string2) and not found:
            if string1[index1] == string2[index2]:
                found = True
            else:
                index2 += 1
        if found:
            string2[index2] = None
        else:
            is_same = False
        index1 +=1
    return is_same

print(compare_letters('python','typhon'))



def sort_compare(letters1, letters2):
    letters1 = list(letters1)
    letters2 = list(letters2)

    letters1.sort()
    letters2.sort()
    if letters1 == letters2:
        return True
    return False

print(sort_compare('abdc','cdba'))

def count_compare(s1, s2):
    counter1 = [0] * 26
    counter2 = [0] * 26
    is_same = True
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        counter1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2) - ord('a')
        counter2[pos] +=1
    j = 0
    while j<26 and is_same:
        if counter1[j] == counter2[j]:
            j +=1
        else:
            is_same = False
    return is_same

print(sort_compare('apple','pleap'))
