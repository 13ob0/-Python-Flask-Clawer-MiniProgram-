# -Python-Flask-Clawer-MiniProgram-

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
* table: 课程表界面，可以选择学年和学期
* scores: 在校成绩界面
* note: 学校官网新闻和通知界面，可以保存图片和转发