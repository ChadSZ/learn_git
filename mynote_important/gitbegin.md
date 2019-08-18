## git 学习

1. git init 

2. git config --global user.name 'xxx' ;git config --global user.email 'xxx' 

3. 关于拉去远程库到本地错误： 拉取远程仓库到本地错误The authenticity of host 'github.com (13.229.188.59)' can't be established.

    [可以通过这里找到方法](https://www.cnblogs.com/yuanchaoyong/p/9976895.html)

    步骤：

        使用命令： ls -al ~/.ssh → 
        使用命令： ssh-keygen -t rsa -C "github用户名"，按三次回车 → 
        查看生成的key：cat ~/.ssh/id_rsa.pub → 
        登陆github,点击头像-settings-new SSH,复制新生成的SSH配置到服务器，记住拷贝是4步骤下面的秘钥信息以ssh-rsa开始邮箱结束的。 → 
        正常克隆跟同步代码到github。

4. 上传文件夹到仓库
   
   * 注意：
    1. 文件夹内必须有文件，
    2. 文件夹在add的时候必须包含 xxx/ 的正斜杠。

5. 拒绝上传到远程库：
   ! [rejected]        master -> master (fetch first)
    error: failed to push some refs to 'git@github.com:ChadSZ/learn_git.git'

    原因：远程库有文件，但是本地没有这个文件，提交上去会覆盖之前的文件。

    解决方法：
    1. 强制提交： git push -u origin master -f (会覆盖掉原有的文件)
    2. 重新建立分支

6. 升级pip版本
   * python -m pip install --upgrade pip

7. you-get 下载
   * you-get -o F:/AA -O cc "https://www.bilibili.com/video/av6778814/?from=search&seid=14154322691319558545"：下载到指定目录下