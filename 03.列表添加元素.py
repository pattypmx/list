value = [1, 2, 3, 4, 5]
value2 = [1, 2, 3, 4, 5]
value3 = [1, 2, 3, 4, 5]

# append:直接添加在末尾,添加的是一个整体
# value.append(6)
# print(value)
# value2.append("abcd")
# print(value2)

# # insert:指定位置添加,添加的是一个整体
value.insert(2, 6)
print(value)
value2.insert(2, "abcd")
print(value2)
value3.insert(2, ["a", "b", "c"])
print(value3)

# extend:添加一个可遍历的对象
# value.extend("abc")
# print(value)
# value2.extend(["a", "b", "c"])
# print(value2)


