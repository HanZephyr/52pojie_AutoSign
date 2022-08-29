# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

def sign(cookie):
    result = ""
    headers = {
        "Cookie": cookie,
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    res = requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers
    )
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in text:
        result += "Cookie 失效"
    elif "恭喜" in text:
        result += "签到成功"
    elif "不是进行中的任务" in text:
        result += "今日已签到"
    else:
        result += "签到失败"
    return result 

def main():
    b = os.environ['POJIE']
    cookie = b
    sign_msg = sign(cookie=cookie)
    print(sign_msg)


if __name__ == "__main__":
    main()
