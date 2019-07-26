### web学习
安装插件**open in browser**


#### 标签选择器：
对页面的标签采用统一样式

#### class选择器：
设定元素的class属性为样式的名称，还可以同时设定多个class。名称之间**加空格**

#### id选择器：
为指定id的元素设定样式，id前加 #

#### 关联选择器：
```html
        P strong{background-color:yellow}
        表示P标签内的strong标签内的内容使用的样式
        <strong>sadfasfasff</strong>
        <p>
            <strong>asdfasdf</strong>
        </p>
```
#### 组合选择器：
```html
    H1,H2,input{background-color:yellow}
        <h1>hello</h1>
        <input type=“text” value=“test”/>
```


#### 样式表的优先级：
标签内部的样式 > head的样式表样式

### 今日作业：
    使用元素内联、页面嵌入、外部引用对标签进行渲染（要求使用class,id,组合选择器制作即可）