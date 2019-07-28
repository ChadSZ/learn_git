# 用户身份验证用户名和密码，管理员(admin)、用户(user)、超级用户(vip)。
# 已知管理员身份的有以下：方开-123，刘晨-12345;
# 超级用户：张旭-123321、沈章-123456、许景-123456;
# 访客：其他(字母或者中文构成的用户名)-guest
# 输出：访问成功，访问失败

# 键入用户名和密码
a,b = map(str,input("请输入用户名和密码：").split(" "))

dic = {"admin":{"fangkai":"123","liuchen":"12345"},"vip":{"shenzhang":"123456","xujing":"123456"},"guest":{"guest":""}}

# 将字典转换为list
user = list(dic.values())
# print (user[0],type(user[0])) # user[0]仍然是dict

#获取user的长度
lenuser = len(user)
# print(lenuser,type(lenuser)) # len获取的是int类型
#len()方法用于获取长度
# print(len(user[0]),type(len(user[0])))

# print(type(user[lenuser-1]),user[lenuser-1])
while lenuser>0:
    lenuser = lenuser-1
    # print(user[lenuser])
    # 将用户名转换为list
    name = list(user[lenuser].keys())
    password = list(user[lenuser].values())
    # print(name,len(name))
    # print(password)
    i = len(name)-1

# 下面的 id 和 is 都是用来判断对象的
# if username[0] is a or username[1] is b:
# if id(username[0]) == id(a):
#     if id(userpass[0])==id('123'):

#判断是否登录成功  
    if a == name[i] and b == password[i] :
        print(a,"登陆成功")
        break
    elif a == name[i-1] and b == password[i-1] :
        print(a,"登陆成功")
        break
    elif lenuser > 0:
        continue
    else:
        print("用户不存在")  

 


# print(type(b))
# if a is user[0]
# print(1)
# if a==user[0] and b==dic.get("admin")["fangkai"]
#     print(1)

# if a == user.get("admin")["fangkai"]
#     print(1)
# if a == ["admin"][0] and b== or ["admin"][1]==a:
#     b = input("请输入密码")
#     if b == []
#         print("管理员登陆成功")
# elif a = ["vip"][0] or ["vip"][1]:
#     print("超级用户登陆成功")
# elif a = ["guest"] and ["guest"][0]=="":
#     print("游客访问成功")
