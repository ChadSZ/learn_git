<%@ Page Language="vb" AutoEventWireup="false" CodeBehind="WebClass01.aspx.vb" Inherits="WebName01.WebClass01" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <input type="button" value="这是一个按钮"/>
        <br />
        <input type ="text" value="这是一个文本输入框" />
        <br />
        <input type="password" />
        <input type="radio" id="1" name="sex"/><label for ="1">男</label>
        <input type="radio" id="2" name="sex"/><label for ="2">女</label>
        
        <br />
        <a href="https://upload.jianshu.io/users/upload_avatars/1221131/86474f67e08f?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96">图片</a>
        <br />
        <img src="image/05.jpg" />
        <asp:DropDownList ID="DropDownList1" runat="server">
            <asp:ListItem></asp:ListItem>
            <asp:ListItem>方炜</asp:ListItem>
            <asp:ListItem>石建</asp:ListItem>
            <asp:ListItem>孙建辉</asp:ListItem>
            <asp:ListItem>我</asp:ListItem>
        </asp:DropDownList>
        <asp:FileUpload ID="FileUpload1" runat="server" />
        
    </div>
    </form>
</body>
</html>
