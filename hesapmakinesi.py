# -*- coding: utf-8 -*-

def topla (sayi1,sayi2):
    return sayi1+sayi2

def cikar (sayi1,sayi2):
    return sayi1-sayi2

def carp (sayi1,sayi2):
    return sayi1*sayi2


def bol (sayi1,sayi2):
    return sayi1/sayi2


print("İşlemler:")
print (" + : Topla ")
print(" - : çıkar ")
print(" * : çarp ")
print(" / : böl ")


secenek = input(" Hangi işlemi yapmak istiyorsunuz? ")

sayi1=int(input(" Birinci sayıyı giriniz : "))
sayi2=int(input (" İkinci sayıyı giriniz : "))

if secenek =='+':
    print("toplam: " + str(topla(sayi1,sayi2)))
    
elif secenek == '-':
    print("çıkarma: " + str(cikar(sayi1,sayi2)))
    a
elif secenek =='*':
    print("çarpma: " + str(carp(sayi1,sayi2)))
    
    
elif secenek =='/':
    print("bölme: " + str(bol(sayi1,sayi2)))
    
else:
    print(" Geçersiz işlem ")