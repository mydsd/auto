import hashlib
class Md5():
    def md5(self,arg):
        md5 = hashlib.md5()
        loc_bytes_utf8 = arg.encode(encoding="utf-8")
        md5.update(loc_bytes_utf8)
        return md5.hexdigest()
if __name__ == '__main__':
    data = Md5().md5("sfdsdgdfststrewtyewrryr").upper()
    print(data)