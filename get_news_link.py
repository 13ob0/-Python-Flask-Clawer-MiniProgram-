from selenium import webdriver

def getNewsLink_fun(newsLink):
    """

    :param newsLink: 新闻链接
    :return: 包含新闻标题和链接的字典
    """
    driver.get('http://www.nfu.edu.cn/index.php')
    # time.sleep(1)

    global news
    news = list()
    for i in range(10):
        news.insert(i, driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div[3]/div[1]/div/ul[1]/li[' + str(i + 1) + ']/p[2]/a'))

    newsName = news[int(newsLink)].text
    newsUrl = news[int(newsLink)].get_attribute('href')

    dict_news = {'newsName': newsName,
                 'newsUrl': newsUrl}

    return dict_news