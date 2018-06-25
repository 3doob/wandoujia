# -*- coding: gbk -*-
import json
import os
def writeFile(filename,data):
    dirname = os.path.dirname(filename)
    try:
        mkdir(dirname)
    except Exception as e:
        print(e)
    with open(filename, 'w') as file_obj:
        json.dump(data, file_obj,ensure_ascii=False)
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False