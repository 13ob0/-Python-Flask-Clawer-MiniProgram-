import json
import requests

def getCode_fun():
    """

    :return: 保存验证码
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

    }
    login_url = 'http://jwxt.nfsysu.cn/default2.aspx'
    post_url = 'http://jwxt.nfsysu.cn/default2.aspx'
    #   self.logined_url = 'http://jwxt.nfsysu.cn/xs_main.aspx?xh=152015097'

    codeUrl = 'http://jwxt.nfsysu.cn/CheckCode.aspx'
    r = session.get(codeUrl)
    with open('./img/code.jpg', 'wb') as f:
        f.write(r.content)
        f.close()

    if request.method == "GET":
        if os.path.isfile(os.path.join('img', 'code.jpg')):
            return send_from_directory('img', 'code.jpg', as_attachment=True)
