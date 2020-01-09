# 随机取6个值，范围在[-10，50]之间，进行排列
# 分解：1.随机取值，导入random
import random

# 定义一个列表，存放值
my_list = []    # my_list放在循环外面，不然的话就是得到循环6次的6个列表

# 取值为在范围内循环取值
for x in range(6):
    value = random.randint(-10, 50)
    # print(value)   # 得出随机取的值

# 把随机取得数存放在列表中
    my_list.append(value)
print(my_list)

# 把得到的列表升序排列：sort
# my_list.sort()
# print(my_list)

# # 2.reverse：可定义升序=False，降序=True
# my_list.sort(reverse=False)
# print(my_list)
my_list.sort(reverse=True)
print(my_list)

