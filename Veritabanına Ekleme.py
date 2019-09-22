import sqlite3

vt=sqlite3.connect("database")
im=vt.cursor()
im.execute('''CREATE TABLE IF NOT EXISTS OGRENCI
           (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           ADI TEXT NOT NULL,
           SOYADI TEXT NOT NULL,
           OKULNO TEXT NOT NULL);''')
ad=input("İsim:")
soyad=input("Soyad:")
okulno=input("Okul No:")
veri=[]
veri.append(ad)
veri.append(soyad)
veri.append(okulno)

im.execute("INSERT INTO OGRENCI(ADI,SOYADI,OKULNO) VALUES (?,?,?)",veri)
vt.commit()
vt.close()
