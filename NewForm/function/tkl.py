import base64
from function.aes import CryptAes
import time
import json
import requests
import re
now_time = int(time.time())
headers = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; MI2 Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0xiaochan"}
def loads_jsonp(_jsonp):
    try:
        return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')
linkParams = {'site_id':'530399',
            'gid':'18112374',
            'goodsid':'560050971707',
             'quan_id' : '25cda25344a04f0aa3b61009785fda9c',
            'd_title':'【迪士尼】秋冬款中筒纯棉儿童袜6双',
            'pic' :'https://img.alicdn.com/imgextra/i3/1609684488/O1CN01uXQYC41j1Y1xHJZCv_!!1609684488.jpg',
            'pid':'mm_15470675_23582941_78534989',
            'wx_pid':'',
            'terminal':'wap',
            'time':now_time,
            'captain_link':''
}
class Tkl():
    def __init__(self,site_id=1,id=None,goodsid=None,quan_id=None,d_title=None,pic=None,pid='mm_314500175_315100398_86176250285',):
        self.linkParams = {'site_id': site_id,
                      'gid': id,
                      'goodsid': goodsid,
                      'quan_id': quan_id,
                      'd_title': d_title,
                      'pic': pic ,
                      'pid': pid,
                      'wx_pid': '',
                      'terminal': 'wap',
                      'time': now_time,
                      'captain_link': ''
                      }
    def tkl(self):
        key = base64.b64decode('Eh9D1HYJ6+LhRnNhTzONegX7a4rRdV9aN2ej8vLFmlw=')
        iv = base64.b64decode('P096F6CBir/LyCcO3ScD+A==')
        de = CryptAes()
        data = json.dumps(self.linkParams)
        s = de.crypt_aes(data,key,iv)
        res = requests.request('get','http://third.baikedna.com/api/detail.html',params={'p':s},headers=headers)
        return loads_jsonp(res.text)

