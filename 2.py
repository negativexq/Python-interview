"""
5 milyondan küçük 3'e bölünebilen Fibonacci sayilarinin toplamini bulan fonksiyon yaziniz.
"""
def solution(max_value):
  # Fibonacci sayılarının ilk iki değeri
  a, b = 0, 1
  # Toplamı tutan değişken
  fibonacci_sum = 0
  
  # İlerleme koşulu
  while b < max_value:
    # Eğer sayı 3'e bölünürse, toplama ekle
    if b % 3 == 0:
      fibonacci_sum += b
    # İlerleme
    a, b = b, a + b
    
  return fibonacci_sum

print(solution(5000000))
