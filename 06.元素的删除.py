# 删除元素：
my_list = [1, 2, "hello", 3.14]
my_list2 = [1, 2, "hello", 3.14]
my_list3 = [1, 2, "hello", 3.14]
my_list4 = [1, 2, "hello", 3.14]

# 1.del：通过元素的下标索引删除---属于python的一个方法
del my_list[2]
print(my_list)

# 2.pop：删除列表的最后一个元素，.pop会返回一个值，告知删除元素的值。pop是属于列表的一个方法
my_list2.pop()
print(my_list2)

# 3.remove：通过指定的对象来删除列表中的元素
my_list3.remove(1)
print(my_list3)

# 4.del 列表名：提前删除对象，释放内存（游戏）
del my_list

# 5.情况列表：列表名.clear()
my_list4.clear()

