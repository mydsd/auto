import base64
from function.md5 import Md5
class R4C(Md5):
    def crypt(self,data,key):
        """RC4 algorithm"""
        x = 0
        box = list(range(256))
        for i in range(256):
            x = (x + box[i] + ord(key[i % len(key)])) % 256
            box[i], box[x] = box[x], box[i]
        x = y = 0
        out = []
        for char in data:
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
            out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
        return ''.join(out).encode()
    def app_code(self,data,key):
        """RC4 encryption with random salt and final encoding"""
        data = base64.b64encode(self.crypt(data, self.md5(key)))
        return data
    def app_decode(self,data,key):
        d = base64.b64decode(data).decode()
        x = self.crypt(d,self.md5(key))
        return x







