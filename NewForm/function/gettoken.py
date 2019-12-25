import requests
import re
class GetToken():
    def get_token(self,url,header,payload,regular):
        session = requests.session()
        html = session.get(url=url,headers=header, data=payload, verify=False)
        pattern = re.compile(b'%s' %regular) #正则表达式
        authenticity_token = pattern.findall(html.content)[0]
        return authenticity_token