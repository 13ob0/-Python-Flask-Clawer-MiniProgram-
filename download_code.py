import os

import requests
from flask import request, send_from_directory


def downloadCode_fun(filename):
    """

    :param filename: 验证码名称
    :return: 报错信息
    """
    if request.method == "GET":
        if os.path.isfile(os.path.join('img', filename)):
            send_from_directory('img', filename, as_attachment=True)
        else:
            return 'error'
    else:
        return 'METHOD error'
