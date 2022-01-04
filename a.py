import requests

url = "http://qmsg.zendee.cn/send/e79c4ab71b262105f099edccf09e63e7?msg=来自python的问候"
r = requests.get(url)
print(r.status_code)
print(r.text)
