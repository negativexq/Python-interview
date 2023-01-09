# encoding:utf-8

from urllib import request
import numpy as np
import pandas as pd

url = 'https://tiny.cc/isimlistesi' 
isimler = request.urlopen(url).read().decode('utf-8') 
list =isimler.split('\n') # splitlines() da olabilir ama \n ile daha iyi çalışıyor gibi

ascii_letters = 'abccdefgghiijklmnooprsstuuvyz' # ascii_letters = string.ascii_letters
turkish_letters = 'abcçdefgğhıijklmnoöprsştuüvyz' # turkish_letters = string.ascii_lowercase + 'çğıöşü'

turkishTable = str.maketrans(turkish_letters, ascii_letters) # Türkçe karakterleri ingilizceye çeviriyoruz

df = pd.DataFrame(list, columns=['isimler']) # pandas dataframe oluşturuyoruz



df['isimler'] = df['isimler'].str.lower() # isimleri küçük harfe çeviriyoruz ve türkçe karakterleri ingilizceye çeviriyoruz

##df.to_csv('isimler.csv', index=False,encoding='utf-8' ) # csv dosyası oluşturuyoruz

df_drop =df.drop_duplicates() # tekrar eden isimleri siliyoruz
##df_drop.to_csv('isimler_drop.csv', index=False, encoding='utf-8') # tekrar eden isimleri sildikten sonra csv dosyası oluşturuyoruz   

print(f'İlk veri sayisi {len(df)}, tekrar edilen veriler çikarildiktan sonra veri sayisi {len(df_drop)} ')
print(f'Tekrar eden veri sayisi= {len(df)-len(df_drop)}')


df_sort = df_drop.sort_values(by=['isimler']) # isimleri alfabetik olarak sıralıyoruz
##df_sort.to_csv('isimler_sort.csv', index=False, encoding='utf-8') # alfabetik olarak sıraladıktan sonra csv dosyası oluşturuyoruz


df_sort['isimler'] = df_sort['isimler'].str.replace(' ', '') # isimlerdeki boşlukları siliyoruz
##df_sort.to_csv('isimler_space.csv', index=False, encoding='utf-8') # boşlukları sildikten sonra csv dosyası oluşturuyoruz


turkish_letters = 'abcçdefgğhıijklmnoöprsştuüvyz'
turkish_letters = {c: i for i, c in enumerate(turkish_letters)}



def score(name):
    try:
        return sum(turkish_letters[c] for c in name)
    except KeyError: # Bazı karakterler hata verdi ve bu sorunu çözemedim
        pass


df_sort['score'] = df_sort['isimler'].apply(score) # isimlerin puanlarını hesaplıyoruz
##df_sort.to_csv('isimler_score.csv', index=False, encoding='utf-8') # puanları hesapladıktan sonra csv dosyası oluşturuyoruz


df_sort['score'].max() # en yüksek puanı buluyoruz
df_sort[df_sort['score'] == df_sort['score'].max()] # en yüksek puanı bulduktan sonra isimlerini buluyoruz


df_sort['score'] = df_sort['score'] * df_sort.index

df_sort['score'].max() # en yüksek puanı buluyoruz
df_sort[df_sort['score'] == df_sort['score'].max()] # en yüksek puanı bulduktan sonra isimlerini buluyoruz


df_sort.nlargest(10, 'score') # en yüksek 5 puanı buluyoruz
print(df_sort.nlargest(10, 'score')) # en yüksek 5 puanı bulduktan sonra isimlerini buluyoruz


scoredData =df_sort['score'].notnull().sum() # score kısmı boş olmayan kaç adaet isim olduğunu buluyoruz
print(f'{scoredData} adet skor hesaplanmiştir')

nullData =df_sort['score'].isnull().sum() # score kısmı boş olan kaç adaet isim olduğunu buluyoruz

print( f'Hatadan dolayi {nullData} adet skor hesaplanamamiştir') # score kısmı boş olan kaç adaet isim olduğunu buluyoruz