# coding=utf-8

import urllib.request as request
import re

def search(author,start):
    if(" " in author):
        author = author.replace(" ","+") #確保輸入時的空白有代換
    url = f"https://arxiv.org/search/?query={author}&searchtype=author&size=50&start={start}"
    content = request.urlopen(url)
    res = content.read().decode('utf-8')
    return res #return html
def numberOfpapers(author):
    dic = {} #所有年度資料的字典
    start = 0 #去抓下一頁的資料要用到的參數
    pattern = "has-text-black-bis has-text-weight-semibold\">originally announced</span>[\s\S]*?</p>" #每一筆論文
    year = '[0-9][0-9][0-9][0-9]' #抓發布年的pattern
    while(1): #迴圈確保有搜尋結果不只一頁
        res = search(author,start)
        result = re.findall(pattern, res)
        if(not len(result)):
            break
        for r in result:
            date = re.search(year,r).group()
            if(date in dic): #放到字典
                dic[date] += 1
            else:
                dic[date] = 1
        start += 50 
    return dic
def numberOfcoauthor(author):
    dic = {} #所有共同作者的字典
    start = 0
    pattern = "<span class=\"search-hit\">Authors:</span>[\s\S]*?</p>" #每一筆論文
    coauthorPattern = "<a href=[\s\S]*?</a>" #每一筆論文下所有個共同作者
    while(1):
        res = search(author,start)
        result = re.findall(pattern, res)
        if(not len(result)):
            break
        for r in result:
            coauthors = re.findall(coauthorPattern,r) #每一筆論文下每一位共同作者
            for coauthor in coauthors:
                temp = re.split(r'<a href=[\s\S]*?>',coauthor)[1] #把不必要的字串拿掉只剩下作者名子
                nameOfcoauthor = re.split(r'</a>',temp)[0] #把不必要的字串拿掉只剩下作者名子
                if(nameOfcoauthor in dic): #放到字典
                    dic[nameOfcoauthor] += 1
                else:
                    dic[nameOfcoauthor] = 1
        start += 50
    if(author in dic): #把原作者從共同作者拿掉
        del dic[author] 
    return dic
def printNumberOfcoauthor(dic):
    for key in sorted(dic.keys()):
        print(f'{key} : {dic[key]} times')