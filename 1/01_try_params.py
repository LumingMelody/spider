import requests

headers =  {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
# p = {'wd':'淘宝网'}
#
# # url_temp = 'https://www.baidu.com/s?'
# url_temp = 'https://www.baidu.com/s'
#
# r = requests.get(url_temp, headers=headers, params=p)
#
# print(r.status_code)
#
# print(r.request.url)

url = 'https://www.baidu.com/s?wd={}'.format('传智播客')

r = requests.get(url, headers=headers)

print(r.status_code)

print(r.request.url)
