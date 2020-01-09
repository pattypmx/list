# 当字符串过多，不方便提取时，可使用列表
# 列表格式：列表名=[元素1，元素2，...]

my_str = "applebanana"
apple = my_str[:5]
print("字符串输出：% s" % apple)

my_list = ["apple", "banana"]
apple1 = my_list[0]
print("列表输出：% s" % apple1)

# 元素类型为任意类型：字符串，数字，布尔，列表
my_list2 = [12, 3.14, "hello", True, [1, 2]]
list2 = my_list2[2]
print(list2)
list22 = my_list2[-3]
print(list22)

# 空列表格式：①列表名=[]   ②list()
my_list3 = []
l = len(my_list3)
print(l)

# print(type(my_list3))

my_list4 = list()
ll = len(my_list4)
print(ll)