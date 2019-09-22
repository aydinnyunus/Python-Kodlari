def sifrele(metin):
    sifrelimetin=""
    for harf in metin:
        asciikod=ord(harf)
        asciikod=asciikod+3
        karakterkod=chr(asciikod)
        sifrelimetin=sifrelimetin+karakterkod

    print("Şifresiz:",metin,"Şifreli:",sifrelimetin)
sifresiz=input("Şifrelenecek metni giriniz:")
sifrele(sifresiz)
        
