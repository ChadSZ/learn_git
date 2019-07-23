## 暑期web培训01
### 内容1
```html
1. http-equiv=http响应头

2. http-equiv和content属性名称/值对,当服务器向浏览器发送文档时,会先发送这些名称/值对

3. <meta http-equiv="名" content="值">
   <!--1.禁止浏览器从本地机的缓存中调阅页面内容,设定后一旦离开网页就无法从Cache中再调出 -->

     <meta http-equiv="pragma" content="no-cache">

   <!--2.清除缓存(再访问这个网站要重新下载！)-->

     <meta http-equiv="cache-control" content="no-cache">

   <!--3.设定网页的到期时间,一旦网页过期,必须到服务器上重新传输。-->

     <meta http-equiv="expires" content="0">   

   <!--4.关键字,搜索引擎用-->

     <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">

   <!--5.页面描述-->

     <meta http-equiv="description" content="This is my page">

   <!--6.html+utf-8-->

     <meta http-equiv="content-type" content="text/html;charset=utf-8">

     <!--7.几秒后页面自动跳转-->

   <meta http-equiv="Refresh" content="2；URL=http://www.net.cn/">

     <!--8.Set-Cookie如果网页过期,那么存盘的cookie将被删除-->

     <meta http-equiv="Set-Cookie" content="cookievalue=xxx;expires=Wednesday, 20-Jun-200722:33:00 GMT； path=/">
     
```

### 内容2
```html
1. div块和span两者的区别：
    div直接占据整快内容，直接打到整个屏幕宽度的区域；
    span达到该区域内容的宽度大小。

2. input标签，password等标签。另外加入了'asp'的特有标签

3. src和href的区别和特点
* src 是指向物件的来源地址，是引入。在 img、script、iframe 等元素上使用。
* href 是超文本引用，指向需要连结的地方，是与该页面有关联的，是引用。在 link和a 等元素上使用。
使用区别：
src通常用作“拿取”（引入），href 用作 "连结前往"（引用）。
```
<div class="center">
  <img src="href&src.png">
</div>

### 内容3
```html
HTML 字符实体 &lt; &gt: &amp;等
```
*   空格 &nbsp;&#160;
* < 小于号 &lt;&#60;
* > 大于号 &gt;&#62;
* & 和号 &amp;&#38;
* " 引号 &quot;&#34;
* ' 撇号 &apos; (IE不支持)&#39;
* ￠ 分（cent）&cent;&#162;
* £ 镑（pound）&pound;&#163;
* ¥ 元（yen）&yen;&#165;
* € 欧元（euro）&euro;&#8364;
* § 小节&sect;&#167;
* © 版权（copyright）&copy;&#169;
* ® 注册商标&reg;&#174;
* ™ 商标&trade;&#8482;
* × 乘号&times;&#215;
* ÷ 除号&divide;&#247; 



