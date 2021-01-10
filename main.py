import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import sys


#layoutData[0].dataList[0].intro
def get_json(appID,language):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    try:
        r = requests.get('https://web-dra.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=10&reqPageNum=1&maxResults=2&uri=app%7C{}&locale={}'.format(appID,language), headers=headers)
    except:
        print('Network Error when fetching info for {}...'.format(appID))
        return None
    soup = BeautifulSoup(r.text, 'lxml')
    parse = json.loads(soup.p.get_text())
    return parse
    #json格式输出

def get_ID(filename):
    df = pd.read_csv(filename)['appID']
    return df
    #DataFrame格式输出

def get_info(appID,language):
    parse_origin = get_json(appID,language)
    from operator import itemgetter
    if parse_origin is None:
        return [appID,"App not found due to Network error","","","","",""]
    if parse_origin['layoutData'] == []:
        return [appID,"App not exists","","","","",""]
    else:
        parse_result = itemgetter(*['appid','name','versionName','package','portalUrl','icon'])(parse_origin['layoutData'][0]['dataList'][0])
        parse_result_list = list(parse_result)
        parse_result_list.insert(4,parse_origin['layoutData'][1]['dataList'][0]['intro'])
        return parse_result_list

    # list  格式输出

if __name__ == "__main__":
    print("读取文件中...{}".format(sys.argv[1]))
    applist = get_ID(sys.argv[1])
    listResult = []
    for i in applist:
        info_cache = get_info(i,'zh')
        listResult.append(info_cache)
        print("正在爬取{}".format(info_cache[slice(0,2)]))
    print('爬取完毕，保存为csv文件...')
    df = pd.DataFrame(listResult,columns=['appID','appName','versionNumber','packageName','downloads','appUrl','iconUrl'])
    df.to_csv('output.csv')
