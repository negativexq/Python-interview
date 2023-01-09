"""
10101. asal sayıyı bulan fonksiyon yaz
"""

def is_prime(n: int) -> bool: # asal sayı mı?
    if n in (2, 3): 
        return True # 2 ve 3 asal sayıdır
    if n == 1 or n % 2 == 0: # 1 ve çift sayılar asal değildir
        return False
    for i in range(3, int(n ** 0.5) + 1, 2): # 3'ten başlayarak tek sayılarla bölüyoruz
        if n % i == 0: # eğer bölen varsa asal değildir
            return False 
    return True # bölen yoksa asal sayıdır


counter = 0
number = 1
while counter < 10101: # 10101. asal sayıyı bulana kadar döngüyü çalıştır
    number += 1 # sayıyı 1 arttır
    if is_prime(number): # sayı asal mı?
        counter += 1 # asal ise sayacı 1 arttır
print(f' {counter}. asal sayı: {number}') # 10101. asal sayıyı yazdır
