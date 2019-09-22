# Arda Mavi - ardamavi.com
# 8-Puzzle
import os
import random

# Ekranı temizleyen fonksiyonumuz:
def clear_screen():
    os.system('clear')
    return

class Tas:
    def __init__(self, lbl):
        self.lbl = lbl
        self.konum = lbl

    # Tasın Numarası:
    def getLbl(self):
        return self.lbl

    # Tasın Konumu:
    def getKonum(self):
        return self.konum

    # Tasın Konumunu Ayarlar:
    def setKonum(self, konum):
        self.konum = konum

# Oluşturulan tablo çözülebilir mi:
def solvable(rnd_list):
    count = 0;
    for i in range(0,len(rnd_list)):
        if rnd_list[i] == 0:
            continue
        for j in range(i+1,len(rnd_list)):
            if rnd_list[j] == 0:
                continue
            elif rnd_list[i]>rnd_list[j]:
                count = count+1
    if count%2 == 0:
        return True
    else:
        return False;

# Taşlar oluşturulur:
def taslar_olustur():
    taslar = []
    for i in range(0,9):
        taslar.append(Tas(i))
    
    # Tasların yerini rastgele yerlestir:
    rnd_list = []
    while 1:
        rnd_list = random.sample(range(9), 9)
        if solvable(rnd_list):
            break

    for tas in taslar:
        tas.setKonum(rnd_list[0])
        del rnd_list[0]
    return taslar

# Tası bulur:
def tas_bul(taslar, lbl = -1, konum = -1):
    for tas in taslar:
        if konum == -1:
            if tas.getLbl() == lbl:
                return tas
        else:
            if tas.getKonum() == konum:
                return tas
    return False # Tas Bulunamadı

# Tasları Yazdır:
def yazdir(taslar):
    tahta = '\n'
    for i in [0,3,6]:
        tahta += ' '
        for j in [0,1,2]:
            tas = tas_bul(taslar, konum = i+j)
            tas_lbl = str(tas.getLbl())
            if tas_lbl == '0':
                tas_lbl = ' '
            tahta += ' '+tas_lbl
        tahta += '\n'
    print(tahta)
    return

# Hareket Ettirme:
def hareket(taslar):
    bosTas = tas_bul(taslar, lbl = 0)
    switcher = {'w': +3, 'a': +1, 's': -3, 'd':-1}
    izin_list = ['w','a','s','d'] # W-A-S-D izin listesi
    if bosTas.getKonum() in [2,5,8]:
        izin_list = ['w','s','d']
    elif bosTas.getKonum() in [0,3,6]:
        izin_list = ['w','a','s']
    while 1:
        inpt = input('Hareket: ').lower()
        if inpt in izin_list:
            tas_konum = bosTas.getKonum()+switcher[inpt]
            tas = tas_bul(taslar, konum = tas_konum)
            if tas == False:
                clear_screen()
                print('Hatalı Giriş')
                yazdir(taslar)
                continue
            else:
                tas_bul(taslar, konum = tas_konum).setKonum(bosTas.getKonum())
                bosTas.setKonum(tas_konum)
                break
        elif inpt == 'q':
            return []
        else:
            clear_screen()
            print('Hatalı Giriş')
            yazdir(taslar)
            continue
    return taslar

# Durum Kontrolu:
def durum_kntl(taslar):
    for i in range(0,9):
        if tas_bul(taslar, konum = i).getLbl() is not i:
            return False
    return True

# Oyun Başlar
def oyun():
    taslar = taslar_olustur()
    while 1:
        clear_screen()
        yazdir(taslar)
        taslar = hareket(taslar)
        if taslar == []:
            clear_screen()
            print('Çıkış Yapıldı !')
            break
        if durum_kntl(taslar):
            clear_screen()
            yazdir(taslar)
            print('Tebrikler Oyunu Tamamladınız !')
            break
    return

def main():
    clear_screen()
    print('8-Puzzle Oyunuma Hoş Geldiniz!\nArda Mavi - ardamavi\n')
    print('-- Oynanış --\nR -> Oyunu Başlat\nW-A-S-D -> Yön Tuşları\nQ -> Çık\n')
    secim = input('Seçim: ').lower()
    clear_screen()
    if secim == 'r':
        oyun()
    print('8-Puzzle\nArda Mavi - ardamavi\nProgramdan Çıkış Yapıldı')
    return

if __name__ == '__main__':
    main()
