# 查找元素
my_list = [1, 20, 300, 'hello']

# 1.in：判断一个元素是否存在列表中
if 300 in my_list:
    print("存在")
else:
    print("不存在")

# 2.not in：判断一个元素不存在列表中
if 300 not in my_list:
    print("不存在")
else:
    print("存在")

# 3.index：通过index获取某个元素在列表中的下标索引，有索引，即存在
# 列表.index(元素)
index = my_list.index(20)
print(index)

# 4.count：查找某个元素在列表中出现的次数，0为不存在
# 列表.count(元素)
count = my_list.count(200)
print(count)

# 查询300，如果有标示出下标索引
if 300 in my_list:
    index = my_list.index(300)
    print(index)

# 或者
count2 = my_list.count(300)
if count2 > 0:
    index2 = my_list.index(300)
    print(index2)

