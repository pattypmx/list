# 一个学校，三个办公室，8个老师随机分配到办公室
# 随机分配，导入random
import random
# 定义一个学校，存放三个办公室
school = [[], [], []]
# 定义8个老师
teacher = "ABCDEFGH"
for x in teacher:
    t = random.randint(0, 2)
    school[t].append(x)
print(school)

