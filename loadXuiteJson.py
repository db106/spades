# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:47:33 2020

@author: TibaMe-Big_Data
隨意窩json檔
"""

import json

savepath = r"D:\2019biDataProject\xuite"

f = open(savepath+"\\taipeiJson.txt","r",encoding = "utf-8")
#取得xuite大分類
links = f.readlines()
f.close

for link in links:
    tag = "{\"element_id\""
    if link.startswith(tag):
        s = json.loads(link , encoding = "utf-8")
        break
        