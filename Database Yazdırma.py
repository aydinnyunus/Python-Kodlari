import sqlite3

vt=sqlite3.connect("database")
im=vt.cursor()


satırlar=im.execute("select ID,ADI,SOYADI,OKULNO FROM OGRENCI") 
for i in (satırlar):
    print(i)





vt.commit()
vt.close()
