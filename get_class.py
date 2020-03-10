import json


def getClass_fun():
    """

    :return: 课程的字典列表
    """
    try:
        xnd = json.loads(request.values.get('stuYear'))
        xqd = json.loads(request.values.get('stuTerm'))
    except TypeError:
        return '请选择学期'

    selector_classPage = etree.HTML(responseText)
    url_class = selector_classPage.xpath('//a[contains(@href,"gnmkdm=N121603")]/@href')[0]
    post_url_class = 'http://jwxt.nfsysu.cn/' + url_class[0:28] + urllib.parse.quote(url_class[28:-15]) + url_class[
                                                                                                          -15:]

    if (xnd == '2018-2019' and xqd == '2'):
        headers_class = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'jwxt.nfsysu.cn',
            'Origin': 'http://jwxt.nfsysu.cn',
            'Referer': 'http://jwxt.nfsysu.cn/xs_main.aspx?xh=' + url_class[15:24]
        }

        response_class = session.post(post_url_class, headers=headers_class)
    else:
        headers_class = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Host': 'jwxt.nfsysu.cn',
            'Origin': 'http://jwxt.nfsysu.cn',
            'Referer': post_url_class
        }
        response_iframe2 = session.get(post_url_class, headers=headers_class)

        selector_ViewState = etree.HTML(response_iframe2.text)

        ViewState = selector_ViewState.xpath('//*[@id="xskb_form"]/input[3]/@value')[0]

        post_data_class = {
            '__EVENTTARGET': 'xnd',
            '__EVENTARGUMENT': '',
            '__VIEWSTATE': ViewState,
            'xnd': xnd,
            'xqd': xqd
        }

        response_class = session.post(post_url_class, data=post_data_class, headers=headers_class)

    #    if response_class.status_code == 200:
    #        print(response_class.text)
    #    else:
    #        print(response_class.status_code)
    #        # print(response_class.headers['Location'])

    selector_class = etree.HTML(response_class.text)

    class_tr = selector_class.xpath('//br/../text()')

    class_list = class_tr[3:-5]

    item_classList = list()
    item_class = ['className', 'classTime', 'classTea', 'classLoc']

    for n in range(0, len(class_list), 4):
        item_classList.append(dict(zip(item_class, class_list[n:n + 4])))

    #    for i in range(0, len(class_list), 4):
    #        print(n, class_list[i])
    #        n = n + 1

    return item_classList
