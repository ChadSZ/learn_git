## android
* 页面跳转功能实现：
通过建立一个Intent,startActivity 调用完成界面跳转

首选的进入页面：
将
<intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

加入 新创建的activity 的java文件内容中。

* 改变主题：
<activity android:name=".DialogActivity"
            android:theme="@style/Theme.AppCompat.Dialog"/>

* 七大生命周期的认识

* fragment 的理解