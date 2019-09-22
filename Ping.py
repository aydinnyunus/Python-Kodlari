import subprocess as sp

ip=input("Ip giriniz:")
p=sp.Popen("ping "+ip,stdout=sp.PIPE)
    
if p.poll():
        print(ip+"pasif")
else:
        print(ip+"aktif")
