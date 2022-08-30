# CTFK

![在这里插入图片描述](https://img-blog.csdnimg.cn/6dd89e85c0c145a29210c68b8ce53cce.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAS0tmaW5lXw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## Getting Started

admin，frontend是前端目录

进行

`yarn install`

`yarn add element-ui`

`yarn serve`

之后即可开启两个服务

剩下的都是后端的文件，在backend中的settings配置好本地postgresql的用户密码后，直接在根目录进行

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python manage.py runserver`

即可开启后端服务

- https://twitter.com/vuetifyjs)

# structure

网站采用`vue`和`django`前后端分离的结构，二次开发者可以重写前端，后端路由对上即可