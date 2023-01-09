"""
Baştan ve sondan yazıldığında değişmeyen sayılara pelindrom sayılar denir. Örneğin 1001, 23432. 
2 haneli sayıların çarpımından elde edilen en büyük pelindrom sayısı 91*99 =9009'dur. 
3 Haneli sayıların çarpımından elde edilen en büyük pelindrom sayısını bulan fonksiyon yazınız.
"""
def solution(limitMax):
  pal = []
  for i in range(limitMax, 100, -1):
    for j in range(limitMax, 100, -1):
      value = i * j
      if str(value) == str(value)[::-1]:
        # Bu aralıkta bulunan ve bu kurala uyan tüm sayıları bir listeye ekliyoruz.
        pal.append(value)
  # Kurala uyan tüm sayılardan en büyüğünü döndürüyoruz.      
  return max(pal)   
    

print(solution(999))