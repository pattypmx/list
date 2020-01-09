value = [1, 3.14, "hello"]
# 修改3.14为哈哈
# 先得到下标索引
index = value.index(3.14)
print(index)
# 通过索引修改内容
# 格式：列表[修改元素的下标] = 修改的值
value[index] = "哈哈"
print(value)
