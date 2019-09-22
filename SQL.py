import sqlite3

vt=sqlite3.connect("database")
im=vt.cursor()


eski=input("Değiştirilecek ismi giriniz:")
yeni=input("Yeni adı giriniz")

im.execute("UPDATE OGRENCI SET ADI=? WHERE ADI=?",(yeni,eski))


vt.commit()
vt.close()
