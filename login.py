import json
import requests
from flask import request


def login_fun():
    """

    :return: 登录响应
    """
    stuNum = json.loads(request.values.get('txtUserName'))
    stuPw = json.loads(request.values.get('TextBox2'))
    code = json.loads(request.values.get('code'))
    print(json.loads(stuNum))

    post_url = 'http://jwxt.nfsysu.cn/default2.aspx'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

    }

    post_data = {
        '__VIEWSTATE': 'dDwxNTMxMDk5Mzc0Ozs+g6R0by/GzInqdfLlQMEGbEJpRJM=',
        'txtUserName': stuNum,
        'Textbox1': '',
        'TextBox2': stuPw,
        'txtSecretCode': code,
        'RadioButtonList1': '学生',
        'Button1': '',
        'lbLanguage': '',
        'hidPdrs': '',
        'hidsc': ''
    }

    return session.post(post_url, data=post_data, headers=headers)