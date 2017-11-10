from cmath import*
class moadele1 () :
    rishe1=0
    rishe2=0
def risheha (s) :
    print("moadele shoma Amade Ast :" + "x^2"+"-"+S+"x"+ "+"+P)
        
moadele1rishe = moadele1()
moadele1rishe.rishe1 = int(input(" Rishe 1 ra vared konid "))
moadele1rishe.rishe2 = int(input("rishe 2 ra vared konid  " ))
P = moadele1rishe.rishe1 * moadele1rishe.rishe2
S = moadele1rishe.rishe1 + moadele1rishe.rishe2
P = str(P)
S = str(S)
print(risheha(moadele1rishe))
class moadele2 ():
    zarib_a = 0
    zarib_b = 0
    zarib_c = 0
def moadele2_hi (sss) :
    print("rishe haye shoma in ast :" + rishe_1 + " va " + rishe_2)
moadele_koll=moadele2()
moadele_koll.zarib_a=int(input("Lotfan Zarib A ra Vared Konid "))
moadele_koll.zarib_b=int(input("Lotfan Zarib B ra Vared Konid"))
moadele_koll.zarib_c=int(input("Lotfan Zarib C ra varid Konid"))
delta = ((moadele_koll.zarib_b) **2)-4*(moadele_koll.zarib_a * moadele_koll.zarib_c)
if delta < 0 :
    print("delta nemitavand Bashad ! ")
rishe_1 = (-moadele_koll.zarib_b - sqrt(delta))/(2 * moadele_koll.zarib_a)
rishe_2 = (-moadele_koll.zarib_b + sqrt(delta))/(2 * moadele_koll.zarib_a)
rishe_1=str(rishe_1)
rishe_2=str(rishe_2)
print(moadele2_hi(moadele_koll))

