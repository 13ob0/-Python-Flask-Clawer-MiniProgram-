# -Python-Flask-Clawer-MiniProgram-

## 技术栈

* Flask, requests, selenium, xpath
* html, js, css

## 程序结构

* 基于Flask的后端服务器
* 基于原生语言的微信小程序

### 后端服务器

* Server: Flask主程序
* get_code: 使用xpath定位验证码
* login: post携小程序用户信息请求登录，并保持session
* get_class, get_scores: 使用xpath定位元素并爬取数据、分析url爬取Ajax数据
* get_news：使用selenium自动化爬取学校官网新闻链接并截取新闻内容

### 微信小程序

* login: 登录界面

  ![登录界面](https://github.com/13ob0/-Python-Flask-Clawer-MiniProgram-/blob/master/img/41583885856_.pic.jpg?raw=true)

* table: 课程表界面，可以选择学年和学期

  ![课程界面](https://github.com/13ob0/-Python-Flask-Clawer-MiniProgram-/blob/master/img/51583885862_.pic.jpg?raw=true)

* scores: 在校成绩界面

  ![成绩界面](https://github.com/13ob0/-Python-Flask-Clawer-MiniProgram-/blob/master/img/61583885868_.pic.jpg?raw=true)

* note: 学校官网新闻和通知界面，可以保存图片和转发

  ![新闻界面](https://github.com/13ob0/-Python-Flask-Clawer-MiniProgram-/blob/master/img/71583885874_.pic.jpg?raw=true)

  ![详情界面](https://github.com/13ob0/-Python-Flask-Clawer-MiniProgram-/blob/master/img/81583885880_.pic.jpg?raw=true)

