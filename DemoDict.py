# DemoDict.py 

colors = {"apple":"red", "banana":"yellow"}
print(colors)
print(type(colors))
print(len(colors))
#추가
colors["kiwi"] = "green"
print(colors)
#삭제
del colors["apple"]
print(colors)

for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k, v)
    

