# Comprehensive-information-website

后端使用Django，前端使用Vue3，爬虫使用Scrapy ，数据库使用Mysql实现的资讯综合网站，包含微博、b站、知乎的热榜信息以及微博和b站的博主的动态信息，并将其统一展示在网页中以方便浏览，还包含完善的个人管理页面和超级用户管理页面

**热榜**

![image](https://user-images.githubusercontent.com/65942634/233374822-07b57074-534e-4520-9d3f-c005ef808d53.png)

![image](https://user-images.githubusercontent.com/65942634/233374836-027f9cfc-a2ac-40a2-b933-507c3443f191.png)

![image](https://user-images.githubusercontent.com/65942634/233374851-25fb5290-5e92-444f-b4f8-506860081e26.png)

**动态**

![image](https://user-images.githubusercontent.com/65942634/233374925-f3dace28-e54e-4706-abab-e6e891eccbbc.png)

![image](https://user-images.githubusercontent.com/65942634/233374938-78c1c69f-17db-4c5a-a3a7-e0df5ccb8fca.png)

## 数据流图

![image](https://user-images.githubusercontent.com/65942634/233379040-78dba2f9-ad50-4145-8cff-29f7365d737a.png)

## 后端功能介绍

![image](https://user-images.githubusercontent.com/65942634/233377275-b337afb7-a69b-42a2-ad48-d2ad1f7f6ff6.png)

## 爬虫功能介绍

* 爬取知乎热榜
* 爬取微博热榜
* 爬取b站热榜
* 爬取微博博主动态
* 爬取b站up主动态

## 数据库需求介绍

![image](https://user-images.githubusercontent.com/65942634/233377666-5d6919d7-1875-417c-affa-895b993ebaa8.png)

![image](https://user-images.githubusercontent.com/65942634/233377676-c68942d1-5db3-4b83-a10e-70adf33633f5.png)

![image](https://user-images.githubusercontent.com/65942634/233377701-9cdfccc0-6abd-4236-93e6-c8f9496d4b80.png)

![image](https://user-images.githubusercontent.com/65942634/233377713-565936df-9451-4f7f-a076-903fd6f579ef.png)

![image](https://user-images.githubusercontent.com/65942634/233377724-cdd09fd2-582c-48d1-9a06-075479a50bf3.png)

![image](https://user-images.githubusercontent.com/65942634/233378930-d5e47f1a-df94-4707-a167-592efbfed134.png)


## 前端介绍

登陆页面

* 走马灯式的设计
* 一个页面承载3个热榜
* 任何人都可以访问
* 按钮随着身份进行变化

![image](https://user-images.githubusercontent.com/65942634/233377901-7c445465-35ab-4515-ae02-b0af3577499f.png)

热榜页面

![image](https://user-images.githubusercontent.com/65942634/233377965-f8adb582-e8e4-4541-8789-ffb408ef9340.png)

![image](https://user-images.githubusercontent.com/65942634/233377975-910e5e7a-c5c0-4321-b13e-3ef3f2973bac.png)

![image](https://user-images.githubusercontent.com/65942634/233377993-c94a9c7c-02fc-4bce-971d-e124758512e5.png)

动态页面

* 走马灯式的设计
* 一个页面承载2个动态
* 不登录不能查看
* 支持多种类的动态卡片

![image](https://user-images.githubusercontent.com/65942634/233378078-9053361b-5bd4-48ac-a120-2dd7fd2ce883.png)

![image](https://user-images.githubusercontent.com/65942634/233378097-c7bae3c8-ac15-4893-8bd3-ba4c77b07bfb.png)

个人页面

* 展示b站、微博关注的人
* 关注、取消关注b站、微博的人
* 修改用户名
* 修改密码
* 退出登陆

![image](https://user-images.githubusercontent.com/65942634/233378301-c3f5f5fb-5ba4-4424-b499-2f4dadc88643.png)

超级用户管理页面

* 添加、删除用户
* 修改用户密码
* 添加、删除b站、微博需要爬取的博主
* 修改热榜的爬取时间间隔

![image](https://user-images.githubusercontent.com/65942634/233378561-609fdcad-85e7-4bb9-bbdd-f7c5e54d0ef8.png)

![image](https://user-images.githubusercontent.com/65942634/233378577-4d5c61c6-c8ca-40d0-b395-db0b900a53d1.png)

![image](https://user-images.githubusercontent.com/65942634/233378599-f82e1c2e-d3c1-40d1-bc48-b4f6b94b022a.png)

![image](https://user-images.githubusercontent.com/65942634/233378617-d4b16509-1ed5-4fd0-b641-76f797008531.png)

![image](https://user-images.githubusercontent.com/65942634/233378632-20044db6-834b-4d4d-a707-d60c63e3a1dc.png)

