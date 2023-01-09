"""
Verilen cumledeki kelimelerin ortalama uzunlugunu bulan fonksiyon yaziniz. ",.!?:;" gibi noktalama itaretlerini kelime uzunluguna dahil etmeyiniz. or: avg_len("Elma, portakal, armut") -> 5.66 
"""

def solution(sentence):
    # Noktalama işaretlerini ve boşlukları atalım
    sentence = sentence.replace(',', ' ').replace('.', '').replace('!', '').replace('?', '').replace(':', '').replace(';', '')
    print(f'Noktalama işaretleri ve boşluklar atildi: {sentence}')  #check
    # Cümleyi kelimelere ayıralım
    words = sentence.split()
    print(f'Kelimeler: {words}') #check
    # Kelimelerin uzunluklarını toplayalım
    total_len = sum(len(word) for word in words)
    # Ortalama uzunluğu hesaplayalım
    avg_len = total_len / len(words)
    # Ortalama uzunluğu döndüralım
    return avg_len

test = "Elma, portakal, armut"
avg_len = solution(test)
print(avg_len)

test2 = "Verilen cumledeki kelimelerin ortalama! uzunlugunu bulan? fonksiyon yaziniz" # Noktalama işareti denemek için test
avg_len2 = solution(test2)
print(avg_len2)