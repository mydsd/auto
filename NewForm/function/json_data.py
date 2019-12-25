import re
import json
class Json_Data():
    def list_get(self,args,key,tmp_list):
        for i in args:
            if isinstance(i, dict):
                self.dict_get(i, key, tmp_list)
            elif isinstance(i, list):
                self.list_get(i, key,tmp_list)
        return tmp_list
    def dict_get(self,args, key,tmp_list):
        for k,v in args.items():
            if k != key:
                if isinstance(v, dict):
                    self.dict_get(v, key,tmp_list)
                elif isinstance(v, list):
                    self.list_get(v, key,tmp_list)
            elif k == key:
                tmp_list.append(v)
        return tmp_list

    def loads_jsonp(self,_jsonp):
        """
        解析jsonp数据格式为json
        :return:
        """
        try:
            return json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')