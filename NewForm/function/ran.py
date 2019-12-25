import random
class RanNum():
    '''9位随机数字'''
    def ran_phone(self,s,num):
        l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = random.sample(l, num)
        b = s + "".join(a)
        return b
    def ran_str(self,c):
        '''26位随机字母'''
        l = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
             "q","r","s","t","x","y","z","v","u","w"]
        a = random.sample(l, c)
        b = "".join(a)
        return b

    def ran_digi_str(self, c):
        '''随机数字字母'''
        l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
             "s", "t", "x", "y", "z", "v", "u", "w", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        a = random.sample(l, c)
        b = "".join(a)
        return b