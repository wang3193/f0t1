'''
给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，
输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表
'''
attributes = ['name', 'dob', 'gendor']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],          
['nancy', '2001-02-01', 'female']]

_dic = [dict(zip(attributes, z))  for z in values]

print(_dic)

# 按值大小排列
d = {'mike': 10, 'lucy': 2, 'ben': 30}

f = sorted(d.items(), key= lambda x : x[1], reverse= True )
print(f)