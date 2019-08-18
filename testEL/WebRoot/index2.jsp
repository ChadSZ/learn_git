<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
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
    	String username = "今天是周末";
    	//pageContext.setAttribute("username", username);
    	//request.setAttribute("username", username);
    	session.setAttribute("username", username);
    	application.setAttribute("username", username);
     %>
     username = ${username}<br/>
     <%
    	pageContext.setAttribute("address", "aaa");
    	request.setAttribute("address", "bbb");
    	session.setAttribute("address", "ccc");
    	application.setAttribute("address", "ddd");
     %>
     address = ${address}<br/>
     address = ${sessionScope.address } <br/>
     address = ${applicationScope.address } <br/>
     
  </body>
</html>
