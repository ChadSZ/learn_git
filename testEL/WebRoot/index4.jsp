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
     	String[] names = {"张三","李四","王五"};
     	pageContext.setAttribute("names", names);
     %>
	names[1]=${names[1] }<br/>
	<!-- 若访问的数组元素下标超出了数组下标上限，EL不会抛出越界异常 -->
	names[5]=${names[5] }<br/>
	
	<%
		School[] schools = new School[3];
		schools[0] = new School("清华大学","北京");
		schools[1] = new School("北京大学","北京");
		schools[2] = new School("厦门大学","福建");
		
		pageContext.setAttribute("schools", schools);
	 %>
	 schools[2].sname = ${schools[2].sname } <br/>
	
	
  </body>
</html>
