import json
from json import dumps, loads, JSONEncoder, JSONDecoder

t1_dict = {
    "name":"小强",
    "age":"12",
    "sex":"female"
}
name1,age1,sex1 = input("请依次输入姓名，年龄，性别").split(" ")

with open(r"H:\java\VS\workspaces\test0801\python_json.json","r+",encoding='utf-8') as f:
    
    # 刚开始获取的是'_io.TextIOWrapper'类型
    # print(type(f))

    # 读取后
    str_json = f.read()
    # 输出字符串类型的json文件
    print(str_json)

    # 使用 loads 将其变为 dict 类型
    dict_json = json.loads(str_json)
    # print(dict_json)

    # dict_json['name'].append('haha')
    # print(dict_json)
    # json.dump(dict_json,f)

    # 通过已有的dict字典数据添加到dict的list中
    # dict_json['name'].append(t1_dict['name'])  
    # dict_json['age'].append(t1_dict['age'])  
    # dict_json['sex'].append(t1_dict['sex'])  
    dict_json['name'].append(name1)
    dict_json['age'].append(age1) 
    dict_json['sex'].append(sex1) 

    # print(dict_json)

    f.write(json.dumps(dict_json))

    # 遍历dict中的name
    # for per in dict_json: 
    #     print(per)

    # 关闭已打开的文件
    f.close()


    # 使用dumps 将其转成str形式
    # json_str = json.dumps(dict_json)
    # print(json_str)
    # print(type(json_str))

    # 将写好的 dict类型数据写入json文件中
    # print(type(t1_dict))
    # json.dump(t1_dict,f)


    