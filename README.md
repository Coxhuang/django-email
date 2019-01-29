@[toc]
# Email

## #0 Blog

```
https://blog.csdn.net/Coxhuang/article/details/86692160
```

## #1 环境


```
Python3.6
Django==2.0.7
```

## #3 需求分析

某网站用户忘记密码,需要邮箱验证找回密码

## #4 开始

### #4.1 新建一个django项目

### #4.2 配置

settings.py
设置邮箱/授权码(如何设置自己的邮箱?后面详细讲解)
```

EMAIL_USE_TLS = True  # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
# EMAIL_USE_SSL = True                         #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'  # 发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
EMAIL_HOST_USER = 'mhesat@163.com'  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'mhesat163'  # 发送邮件的邮箱密码(这里使用的是授权码)
EMAIL_FROM = 'mhesat<mhesat@163.com>'  # 收件人看到的发件人
```

views.py


```
class sendEmailAPI(APIView):
    def post(self, request):
        email = request.data.get("email",None)
        send_mail('subject', # 邮件标题
                  "message", # 邮件内容
                  settings.EMAIL_FROM, # 源
                  [email]) # 目的
        return Response({"msg":"邮件发送成功!"}, status=status.HTTP_200_OK)
```

请求数据

```
{
	"email":"xxx@gmail.com" # 目的邮箱地址
}
```


**发送成功**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190129165023309.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NveGh1YW5n,size_16,color_FFFFFF,t_70)

## #5 邮箱配置详解


### #5.1 配置自己的邮箱地址(xxx.@163.com)
```
EMAIL_HOST_USER = 'xxx@163.com'  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = '授权码'  # 发送邮件的邮箱密码(这里使用的是授权码)
EMAIL_FROM = 'xxx<xxx@163.com>'  # 收件人看到的发件人
```

### #5.2 配置授权码(这里以163为例)

进入163官网,点击设置
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190129164012623.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NveGh1YW5n,size_16,color_FFFFFF,t_70)
设置授权码

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190129164108873.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0NveGh1YW5n,size_16,color_FFFFFF,t_70)
拿到授权码后,填入settings.py中的EMAIL_HOST_PASSWORD="授权码"即可













