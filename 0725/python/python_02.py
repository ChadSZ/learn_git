'''
#字符串

a = "aaa";
b = 'hello world';
c = '中国制造';
d = 110;
e = False;
print(a,b,c);

#type 函数，查看变量类型
print(type(a),type(d),type(e));

# 数字
a = 0b11;
b = 0xfe;
print(a,b);
print(type(a),type(b));

# 浮点型
a = 1.11;
print(a);
print(type(a));

# 进制转换
c = 15;
print(bin(c),type(bin(c)));
print(hex(c),type(hex(c)));
'''


# int()
d = "10";
d = int(d);
print(d,type(d));

e = "10"; # 0x10的0x可以不写
e = int(e,16);
print(e,type(e));

f = 0.1111;
f = int(f);
print(f,type(f));

# 获取用户输入十进制数
'''
dec1 = int(input("输入数字："));
print("十进制数：",dec1);
print("转二进制数：",bin(dec1));
print("转八进制数：",oct(dec1));
print("转十六进制数：",hex(dec1));

input_data = input("输入数字");
print(input_data,type(input_data));
'''

'''
# 任务1
h = int(input("输入的是字符串"),2);
print(int(h),type(int(h)),type(h));
'''
'''
# 任务2
i = int(input("输入的是10进制的字符串"),10);
i = bin(i); #将i转成二进制字符串类型
print(i,type(i));

i = int(i,2)+5; #将二进制数字型进行运算
print(i,type(i)); #将该数字输出
'''

#bool类型
abc = True;
cba = False;
print(abc,cba);
print(type(abc),type(cba));
