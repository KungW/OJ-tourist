#coding:utf-8
"""
@file:      zoj_spider.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2017-06-25 20:29
@description:
            抓取zoj的所有题目，存入questions.json中
"""
import requests
import json
import re
from bs4 import BeautifulSoup


class ZOJSpider:
    host = "http://acm.zju.edu.cn"
    volume_urls = [("http://acm.zju.edu.cn/onlinejudge/showProblems.do"
                    "?contestId=1&pageNumber={}").format(volume_id) for volume_id in range(1, 30)]

    def get_volume_questions(self, url):
        resp = requests.get(url)
        if resp.status_code != 200:
            raise LookupError
        volume_questions = []
        soup = BeautifulSoup(resp.text, "html.parser")
        for question_ele in soup.find_all("tr", class_=re.compile("row"))[1:]:
            tds = question_ele.find_all("td")
            question = {
                "id": tds[0].text,
                "title": tds[1].text,
                "ratio": tds[2].text,
                "url": self.host + tds[0].find("a")["href"]
            }
            volume_questions.append(question)
        return volume_questions

    def write_to_json(self, questions):
        try:
            with open("questions.json", "r") as f:
                json.loads(f.read())
        except FileNotFoundError:
            with open("questions.json", "w") as f:
                data = {
                    "questions": [],
                    "saved_ids": [],
                }
                f.write(json.dumps(data))

        for question in questions:
            with open("questions.json", "r") as f:
                saved_json = json.loads(f.read())
            if question["id"] in saved_json["saved_ids"]:
                continue
            else:
                saved_json["questions"].append(question)
                saved_json["saved_ids"].append(question["id"])

            with open("questions.json", "w") as f:
                f.write(json.dumps(saved_json))

    def run(self, start_page=1, end_page=30, page_gap_time=3):
        import time
        for url in self.volume_urls[start_page:end_page]:
            self.write_to_json(self.get_volume_questions(url))
            print("[success] {}".format(url))
            time.sleep(page_gap_time)


if __name__=="__main__":
    ZOJSpider().run(start_page=10, end_page=20, page_gap_time=1)