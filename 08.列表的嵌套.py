my_list = [["浙江", "杭州", "宁波"], ["江苏", "南京", "苏州"], ["江西", "南昌", "赣州", ["哈哈"]]]
# 1.取值：苏州
list1 = my_list[1]
print(list1)
list2 = list1[2]
print(list2)
# 简单合并写法
list3 = my_list[1][2]
print(list3)


# 2.取值：哈哈
list4 = my_list[2][3]
list5 = list4[0]
print(list5)
