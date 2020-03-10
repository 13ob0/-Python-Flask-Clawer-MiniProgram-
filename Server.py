# -*- coding: UTF-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import logging
import os
from flask import send_from_directory
from flask import jsonify
from lxml import etree
import urllib
from selenium import webdriver
import time

import sys
import importlib

from download_code import downloadCode_fun
from get_class import getClass_fun
from get_code import getCode_fun
from get_news_link import getNewsLink_fun
from get_scores import getScores_fun
from login import login_fun

importlib.reload(sys)


############################################################################################
app = Flask(__name__)

session = requests.Session()

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('window-size=1080,1920')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome('C://chromedriver')

notes_url = 'http://jw.nfu.edu.cn/index.php?m=content&c=index&a=lists&catid=85'
driver.get(notes_url)

global notes, list_notes
notes = list()
list_notes = list()

############################################################################################
# Global variables #
####################
# global stuNum
# global stuPw
# global code
# newsLink???
# notesNum
# notesName
#
##########################################################################################

@app.route('/post')
def postData():
    stuNum = request.values.get('txtUserName')
    stuPw = request.values.get('TextBox2')
    code = request.values.get('code')
    print(type(json.loads(stuNum)))

    return stuNum

##########################################################################################

@app.route('/getcode')
def getCode():
    getCode_fun()

    return '已爬取验证码'


@app.route('/img/<string:filename>')
def downloadCode(filename):
    downloadCode_fun(filename)

    return '已获取验证码'


@app.route('/login')
def login():

    response = login_fun()

    if response.status_code == 200:
        if response.url != post_url:
            global login_response
            login_response = response.text
            return '登录成功'
        else:
            return response.url, '登录失败'
    else:
        return response.status_code, '网页响应失败'


@app.route('/login/class')
def getClass():

    return jsonify(getClass_fun())

@app.route('/login/scores')
def getScores():


    return jsonify(getScores_fun(login_response))


@app.route('/news/<string:newsLink>')
def getNewsLink(newsLink):

    return jsonify(getNewsLink_fun())

#    driver.get(news1)
#
#    article = driver.find_element_by_class_name('ny_content')
#
#    article.screenshot('./news/news11.png')


@app.route('/notes')
def getNotes():
    item_notesList = list()
    item_notes = ['notesNum', 'notesName']

    for i in range(0, len(list_notes), 2):
        item_notesList.append(dict(zip(item_notes, list_notes[i:i + 2])))

    return jsonify(item_notesList)

@app.route('/notes/<string:notesNum>')
def getNoteDetail(notesNum):

    driver.get(notes_url)
    note = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/ul/li[' + notesNum + ']/a')
    note.click()
    driver.find_element_by_class_name('main').screenshot('./Notes/note' + notesNum + '.png')
    driver.get(notes_url)

    if os.path.isfile(os.path.join('Notes', 'note'+notesNum+'.png')):
        return send_from_directory('Notes', 'note'+notesNum+'.png', as_attachment=True)
    else:
        return '暂无详情'

@app.route('/refreshNotes')
def refresh():
    notes_url = 'http://jw.nfu.edu.cn/index.php?m=content&c=index&a=lists&catid=85'
    driver.get(notes_url)

    global notes, list_notes
    notes = list()
    list_notes = list()

    for i in range(20):
        notes.insert(i, driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/ul/li[' + str(i + 1) + ']/a'))
        #print(notes[i].text)
        #print(notes[i].get_attribute('href'))
        list_notes.append(str(i + 1))
        list_notes.append(notes[i].text)
        # list_notes.append(notes[i].get_attribute('href'))
        #driver.get(notes[i].get_attribute('href'))
        #driver.find_element_by_class_name('main').screenshot('./Notes/note' + str(i + 1) + '.png')
        driver.get(notes_url)

    return '刷新成功'

###########################################################################################
@app.route('/public')
def getPublic():
    public_url = 'http://jw.nfu.edu.cn/index.php?m=content&c=index&a=lists&catid=79'
    driver.get(public_url)

    global public
    public = list()

    for i in range(20):
        public.insert(i, driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/ul/li[' + str(i + 1) + ']/a'))
        #print(public[i].text)
        #print(public[i].get_attribute('href'))
        driver.get(public[i].get_attribute('href'))
        driver.find_element_by_class_name('main').screenshot('./Public/public' + str(i + 1) + '.png')
        driver.get(public_url)

    return jsonify(public)

@app.route('/projects')
def getProjects():
    projects_url = 'http://jw.nfu.edu.cn/index.php?m=content&c=index&a=lists&catid=80'
    driver.get(projects_url)

    global projects
    projects = list()

    for i in range(20):
        projects.insert(i, driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/ul/li[' + str(i + 1) + ']/a'))
        #print(projects[i].text)
        #print(projects[i].get_attribute('href'))
        driver.get(projects[i].get_attribute('href'))
        driver.find_element_by_class_name('main').screenshot('./Projects/projects' + str(i + 1) + '.png')
        driver.get(projects_url)

    return jsonify(projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', ssl_context=('1_www.###.###_bundle.crt', '2_www.###.###.key'), threaded=True)
