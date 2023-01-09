"""
Verilen listedeki None degerleri, kendinden onceki None olmayan degerle degi§tirip yeni bir liste olu Olusturan fonksiyon yaziniz. 
or: Input: [3, None, 2, None, None, 1, False, None, 10] 
Output: [3, 3, 2, 2, 2, 1, False, False, 10]. Listenin None ile baslamayacaginl varsayabilirsiniz. 
"""


def solution(list):
    # Sonuç listesi oluşturulur.
    result = [] 
    # Önceki değerin başlangıç değeri None olarak ayarlanır.
    previous_value = None 
    # Listedeki her bir değer için
    for value in list:
        # Eğer değer None ise
        if value is None:
            # Önceki değerin kopya'sını sonuç listesine ekle
            result.append(previous_value)
        # Değilse
        else:
            # Değeri sonuç listesine ekle ve önceki değer olarak ayarla
            result.append(value)
            previous_value = value
    # Sonuç listesi döndürülür
    return result

# Test
list = [3, None, 2, None, None, 1, False, None, 10]
print(list)
print(solution(list))  # [3, 3, 2, 2, 2, 1, False, False, 10]
list2 = [5,None,7,None,None,10,True,None,10]
print(list2)
print(solution(list2))  # [5, 5, 5, 5, 10]
