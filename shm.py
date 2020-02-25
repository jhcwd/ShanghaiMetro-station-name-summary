#coding=utf-8
import pinyin
import requests
import json
import demjson

def getAccent(zi):
    str = pinyin.get(zi,format='numerical')
    return str[-1]
def pushdata(ac,sta):
    final[ac].append(sta)




lines = ['1','2','3','4','5','6','7','8','9','10','11','12','13','16','17','41']
stations = []
final = [[],[],[],[],[]]
for line in lines:
    url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=lineStations&line=' + line
    data = requests.get(url).text
    #print(data)
    text = demjson.decode(data)
    list = text['levels'][0]['locations']
    for obj in list:
        if(obj['title'] not in stations):
            stations.append(obj['title'])

print(stations)
for item in stations:
    accent = ''
    num = ''
    for letter in item:
        accent += getAccent(letter)
        num += '1'
    if(int(accent) % int(num) == 0):
        pushdata(int(int(accent)/int(num)),item)

print(final)

