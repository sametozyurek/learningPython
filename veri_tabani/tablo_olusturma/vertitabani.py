import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplik VALUES('Istanbul Hatirasi','Ahmet Umit','Everest Yayincilik',561)")
    con.commit()

"""def kullanici_veri(kitap,yazar,yayinevi,sayfa):
    try:
        cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(kitap,yazar,yayinevi,sayfa))
        con.commit()
        print("Kayit Basarili.")
    except:
        print("Kayit Yapilamadi.")"""

def veri_cek():
    try:
        cursor.execute("SELECT * FROM kitaplik")
        liste = cursor.fetchall()
        print("Kitaplik Tablosunun bilgileri...\n")
        for i in liste:
            print(i)
    except:
        pass

def veri_cek2():
    cursor.execute("SELECT Isim,Yazar FROM kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik tablosunun bilgileri...\n")
    for i in liste:
        print(i)

def veri_cek3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik WHERE Yayinevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("Kitaplik tablosunun bilgileri...\n")
    for i in liste:
        print(i)

def veriguncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET Yayinevi = ? WHERE Yayinevi = ?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

def verisil(yazar):
    cursor.execute("DELETE FROM kitaplik WHERE Yazar = ?",(yazar,))
    con.commit()

verisil("C. Tolkien")
veri_cek()


"""kitap = input("Kitap : ")
yazar = input("Yazar : ")
yayinevi = input("Yayinevi : ")
sayfa = int(input("Sayfa : "))"""


con.close()
