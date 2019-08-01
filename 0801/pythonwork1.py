# 导入csv 模块
import csv

with open("H:\\java\\VS\\workspaces\\test0801\\pythonwork.csv","r+",newline='',encoding="utf-8") as f:
    # print(type(f.read())
    
    # 使用reader方式读取
    csv_read = csv.reader(f)

    # 打印每行的数据
    for std in csv_read:
        print(std,type(std))

    # 设置需要输入的数据内容
    stu1 = ['d','12','女']
    stu2 = ['e','31','男']

    # 写入数据，并使打开方式为excel格式
    csv_write = csv.writer(f,dialect='excel')
    
    # writerow 是行写入的方法
    csv_write.writerow(stu1)
    csv_write.writerow(stu2)

    # 关闭打开的文件
    f.close()