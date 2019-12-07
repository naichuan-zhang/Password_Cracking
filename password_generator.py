import itertools as its
# 迭代器模块

words = "1234567890"
r = its.product(words, repeat=5)

# a 为文件追加 append
doc = open("passwords.txt", "a")

for i in r:
    doc.write("".join(i))
    doc.write("".join("\n"))

doc.close()
