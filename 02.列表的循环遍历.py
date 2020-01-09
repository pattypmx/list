# 遍历循环
# for
value = [1, 2, 3, "hello"]
for x in value:
    print(x)

# while:定义变量记录索引
# 定义变量保存列表中的元素个数
index = 0
l = len(value)
while index < l:
    value2 = value[index]
    print(value2)
    index += 1
