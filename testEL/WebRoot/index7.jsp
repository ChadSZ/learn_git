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
  
	<%
     	Map<String,Object> map = new HashMap<String,Object>();
     	map.put("school", new School("清华大学","北京"));
     	map.put("mobile","123456");
     	map.put("age", 20);
     	pageContext.setAttribute("map", map);
     %>
	empty name = ${empty name }<br/>
	
	
  </body>
</html>
