from Crypto.Cipher import AES
import base64
class CryptAes():
    # 将text按照byteAlignLen字节对齐，如果不对齐，按照差数填充
    def bytePad(self,text, byteAlignLen=16):
        count = len(text)
        mod_num = count % byteAlignLen
        if mod_num == 0:
            return text
        add_num = byteAlignLen - mod_num
        # print("bytePad:", add_num)
        return text + chr(add_num) * add_num

    def byteUnpad(self,text, byteAlignLen=16):
        count = len(text)
        print("byteUnpad:", count)
        mod_num = count % byteAlignLen
        assert mod_num == 0
        lastChar = text[-1]
        lastLen = ord(lastChar)
        lastChunk = text[-lastLen:]
        if lastChunk == chr(lastLen) * lastLen:
            # print "byteUnpad"
            return text[:-lastLen]
        return text
    '''aes加密'''
    def crypt_aes(self,s,key,iv,bate=16): #AES加密方法
        pad = lambda s:s + (bate -len(s) % bate) * chr(bate - len(s) % bate) #补足16位chr(返回ASCII码值)(必须是16、24、32位)
        cipher = AES.new(key, AES.MODE_CBC,iv) #实例化，key，iv必须16位
        msg = cipher.encrypt(pad(s)) #加密输入的字符串
        return base64.b64encode(msg) #二次加密
    def descypt_aes(self,s,key,iv): #解密
        uppad = lambda s: s[0:-ord(s[-1])]  # 对原长度进行还原
        de_cipher = AES.new(key, AES.MODE_CBC,iv) #实例化
        bytedt = base64.b64decode(s) #base64解码
        y = de_cipher.decrypt(bytedt).decode() #AEX解码
        return uppad(y)
if __name__ == '__main__':
    s="dsd01wejfheuwgheijryhjrhgkqoeteriyhiewjweirtqoiwuerihjiqjgioqjgiqjyoijqopweiewrjhwiojiqjiherhrt"
    key = iv = "qazwsxedcrfvtgb1"
    data = CryptAes().crypt_aes(s,key,iv)
    print(data)
    de_data = CryptAes().descypt_aes(data,key,iv)
    print(de_data)
