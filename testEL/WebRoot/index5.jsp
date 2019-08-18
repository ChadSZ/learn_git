<%@ page language="java" import="java.util.*,learn03.Student,learn03.School" pageEncoding="utf-8"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
  </head>
  
  <body>
<!--   	EL 可以通过索引访问list，但无法访问set。因为set中没有所以的概念。-->     
	<%
     	List<String> names = new ArrayList<String>();
     	pageContext.setAttribute("names", names);
     	names.add("张三");
     	names.add("李四");
     	names.add("王五");
     	pageContext.setAttribute("names", names);
     %>
	names[2]=${names[2] }<br/>
	names[200]=${names[200] }<br/>
	
	
  </body>
</html>
