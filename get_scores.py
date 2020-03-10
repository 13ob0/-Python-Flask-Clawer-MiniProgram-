from lxml import etree


def getScores_fun(login_response):
    """

    :param login_response: 登录响应
    :return: 分数的字典列表
    """
    selector_scoresPage = etree.HTML(login_response)

    url_scores = selector_scoresPage.xpath('//a[contains(@href,"gnmkdm=N121605")]/@href')[0]

    post_url_scores = 'http://jwxt.nfsysu.cn/' + url_scores[0:28] + urllib.parse.quote(url_scores[28:-15]) + url_scores[
                                                                                                             -15:]

    headers_scores = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host': 'jwxt.nfsysu.cn',
        'Origin': 'http://jwxt.nfsysu.cn',
        'Referer': post_url_scores
    }

    response_iframe2 = session.get(post_url_scores, headers=headers_scores)

    selector_ViewState = etree.HTML(response_iframe2.text)

    ViewState = selector_ViewState.xpath('//*[@id="Form1"]/input/@value')[0]

    post_data_scores = {
        '__VIEWSTATE': ViewState,
        'ddlXN': '',
        'ddlXQ': '',
        'Button2': '在校学习成绩查询'
    }

    response_scores = session.post(post_url_scores, data=post_data_scores, headers=headers_scores)

    selector_scores = etree.HTML(response_scores.text)

    list_scoreName = selector_scores.xpath('//*[@id="Datagrid1"]/tr/td[4]/text()')[1:]
    list_score = selector_scores.xpath('//*[@id="Datagrid1"]/tr/td[9]/text()')[1:]
    list_GPA = selector_scores.xpath('//*[@id="Datagrid1"]/tr/td[8]/text()')[1:]

    for i in range(0, len(list_GPA)):
        list_GPA[i] = list_GPA[i][3:]

    list_scores = list()
    for i in range(0, len(list_score)):
        list_scores.append(list_scoreName[i])
        list_scores.append(list_score[i])
        list_scores.append(list_GPA[i])

    item_scoresList = list()
    item_scores = ['className', 'classScore', 'GPA']

    for i in range(0, len(list_scores) - 1, 3):
        item_scoresList.append(dict(zip(item_scores, list_scores[i:i + 3])))

    return  item_scoresList