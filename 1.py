"""
Asal çarpanlari sadece 2, 3 ya da 5'ten oluşan, 1milyon'dan küçük doğal sayilarin toplamini bulan fonksiyon yaz. 
Asal çarpan  2, 3 ya da 5 olan sayilar : 2,3,4,5,6,8,9,10,12,15,16,18,20...
"""
def solution(n):
    # Bu liste, aradığımız sayıların bir listesi olacak
    numbers = []
    # 2, 3 ve 5'in katlarını bulmak için döngü oluşturuyoruz
    for i in range(2, n+1):
        # Eğer sayı 2'nin katı ise
        if i % 2 == 0:
            # Sayıyı listeye ekliyoruz
            numbers.append(i)
        # Eğer sayı 3'ün katı ise
        elif i % 3 == 0:
            # Sayıyı listeye ekliyoruz
            numbers.append(i)
        # Eğer sayı 5'in katı ise
        elif i % 5 == 0:
            # Sayıyı listeye ekliyoruz
            numbers.append(i)
    # Liste içinde gezinerek tüm sayıların toplamını buluyoruz
    total = 0
    for number in numbers:
        total += number
    # Toplamı döndürüyoruz
    return total

# 1 milyon'dan küçük asal çarpanları sadece 2, 3 ve 5 olan sayıların toplamını buluyoruz
print(solution(1000000))
