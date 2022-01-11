import re

key_rule = r"[\[\]]"
key_val = "[10001,1],[10002,21],[10003,41]"
re_key_group = re.split(key_rule, key_val)
# print(re_key_group)
# for i in range(len(re_key_group)):
#     print(i,re_key_group[i],len(re_key_group))
vallist = []
i = 1
while i < len(re_key_group):
    vallist.append(re_key_group[i])
    i+=2
print(vallist)

def reshape_list (exlist,a):
    if len(exlist)//a <=1:
        return exlist
    result = []
    for n in range(len(exlist)//a):
        for i in range(a):
            if i == 0:
                result.append([])
            result[n].append(exlist[i+n*a])
    return result
a = reshape_list([1,2,3],4)
print (a)