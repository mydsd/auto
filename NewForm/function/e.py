import random
from function.tkl import Tkl
from function.connectdb import ConnectDb
from function.json_data import Json_Data
read = Json_Data()
db = ConnectDb()
sql= "select id,goodsid,quan_id,d_title,pic,seller_id from dtk_lingquan_goods where is_delete=0 and is_online=1 and quan_num>0 and quan_time>=now() limit 100;"
tmp = db.operational_database(sql)
id = read.list_get(tmp,'id',[])
goodsid = read.list_get(tmp,'goodsid',[])
quan_id = read.list_get(tmp,'quan_id',[])
d_title = read.list_get(tmp,'d_title',[])
pic = read.list_get(tmp,'pic',[])
sellerId = read.list_get(tmp,'seller_id',[])
db.close_db()
class Get_e():
    def seller(self,id,goodsid,quan_id,d_title,pic):
        tkl_index= random.randint(0,len(id)-1)
        tkl = Tkl(id=id[tkl_index],goodsid=goodsid[tkl_index],quan_id=quan_id[tkl_index],
                  d_title=d_title[tkl_index],pic=pic[tkl_index])
        return tkl.tkl()['data']['link'].split('&')[0].split('?')[1].split('=')[1],quan_id[i]
if __name__ == '__main__':
    with open(r'D:\data\e.txt','w') as f:
        for i in range(0,10000):
            tmp = Get_e().seller(id,goodsid,quan_id,d_title,pic)
            f.write(tmp[0]+','+tmp[1]+'\n')
            print('已写入{}条数据'.format(i+1))

