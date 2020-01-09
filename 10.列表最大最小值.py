# 求列表中的最大，最小值
# 定义一个列表
my_list = [1, 3, 56, 300, 900, 1000]
# print(max(my_list))
# print(min(my_list))

# 利用循环查找最大值最小值
# 定义一个变量存储最大值
# 在列表中找一个数作为最大值标准
my_max = my_list[0]
for value in my_list:  # 循环取列表中的值
    if value > my_max:  # 如果取到的值比最大值还要大
        my_max = value  # 把这个值赋予成为最大值
print(my_max)

# 最小值
my_min = my_list[0]
for value1 in my_list:  # 循环取列表中的值
    if value1 < my_min:  # 如果取到的值比最小值还要小
        my_min = value1  # 把这个值赋予成为最小值
print(my_min)



