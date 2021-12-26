def ad_soyad_gir(i):
    Ad = input('Adi: ')
    Soyad = input('Soyadı: ')
    with open("ogrenci.txt", "a", encoding="utf-8") as file:
        file.write(str(i) + '. Ogrenci Adi - Soyadi: ' + Ad + ' ' + Soyad + ' ')

def sinif_gir():
    sinif = input('Sinifi: \n')
    with open("ogrenci.txt", "a", encoding="utf-8") as file:
        file.write('Sinifi: ' + sinif + ' ')
        
def yas_gir():
    yas = input('Yasi: \n')
    with open("ogrenci.txt", "a", encoding="utf-8") as file:
        file.write('Yasi: ' + yas + ' ')

def cinsiyet_gir():
    cinsiyet = input('Cinsiyeti: \n')
    with open("ogrenci.txt", "a", encoding="utf-8") as file:
        file.write('Cinsiyeti: ' + cinsiyet + ' ')
        
def Bilgileri_ayir():
    liste = []
    with open("ogrenci.txt", "r", encoding="utf-8") as file:
        for satir in file:
            satir = satir[:-1]
            satir = satir.split('*')
            liste.append(satir)
    for i in range(len(liste)):
        print(liste[i])
    print(liste)       
    return liste

while True:
    for i in range(100):
        print('Yapilacak islem turunu seciniz')
        islem = int(input('1- Ogrenci kaydi ekleme\n2- Ogrenci kaydi silme\n3- Bilgileri sorgulama\n'))
        if islem == 1:
            print('İslem yapilacak ogrenciyi belirleyiniz.')
            ad_soyad_gir(i+1)
            print('\nOgrencinin:')
            sinif_gir()
            yas_gir()
            cinsiyet_gir()
            with open("ogrenci.txt", "a", encoding="utf-8") as file:
                file.write('\n*\n')
        elif islem == 2:
            Bilgileri_ayir()
        elif islem == 3:
            Bilgileri_ayir()
        else:
            break
"""
liste = []
with open("ogrenci.txt", "r", encoding="utf-8") as file:
    for satir in file:
        liste.append(satir)
satir = satir[:-1] #satir arasındaki bosluklar alindi
liste = satir.split('***********') # *********** 'dan liste bolundu
print(liste)"""