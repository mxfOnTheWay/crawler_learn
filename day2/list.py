import copy

names =["LiLi","WangWang","MengMeng","HuaHua","DongDong","ChenChen"]
names2 =["LexFeng","YuanYuan","MoMo","FeiFei"]
print(names)
names.append("JiaJia")


names.insert(2,"LongLong")

names.append(names2)

names.insert(2,names2)
print(names)
print("---pop----")
print(names.pop())
print("---pop---lise---")
print(names)
del names[4]
print("----del----%s"%names)

names.remove("HuaHua")
print("remove:--",names)

names[1]="wangfeifei"
print("---new---",names)
names.extend(names2)
print("--extend---",names)
print(names.count("MoMo"))
print(names.index("DongDong"))

print(names)
name_copy =names.copy()
print(name_copy)
names[1]="eee"
names[2][0]="ffff"
print(names)
print(name_copy)
print("="*30)
name_copy2 = copy.deepcopy(names)
print(names)
print(name_copy2)
names[1]="EEE"
names[2][0]="FFFFFF"
print(names)
print(name_copy2)
'''
names3=["fng","1","2","3","dong","cao","#0"]
print(names3)
names3.reverse()
print(names3)
names3.sort()
print(names3)
names3.sort(reverse=True)
print(names3)

names.insert(1,names)
print("----insert---self-----")
print(names)
'''