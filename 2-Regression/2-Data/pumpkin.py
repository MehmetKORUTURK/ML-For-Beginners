import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasını oku
dosya_yolu = "C:/Users/mkoru/OneDrive/Desktop/programs/a_p_p/machine learnig/ML-For-Beginners/2-Regression/data/US-pumpkins.csv"
pumpkins = pd.read_csv(dosya_yolu)

# Sadece kullanılacak sütunları seç
sutunlar = ['Package', 'Low Price', 'High Price', 'Date']
pumpkins = pumpkins[sutunlar]

# Fiyatı hesapla (Düşük ve Yüksek Fiyatın ortalaması)
pumpkins['Price'] = (pumpkins['Low Price'] + pumpkins['High Price']) / 2

# Tarih sütunundan ay bilgisini çıkar
pumpkins['Month'] = pd.to_datetime(pumpkins['Date']).dt.month

# Paket bilgisine göre fiyat düzeltmeleri yap
# '1 1/9' içeren paketlerde fiyatı 1 + 1/9 ile böl
pumpkins.loc[pumpkins['Package'].str.contains('1 1/9', na=False), 'Price'] = pumpkins['Price'] / (1 + 1/9)
# '1/2' içeren paketlerde fiyatı 1/2 ile böl (yani 2 ile çarp)
pumpkins.loc[pumpkins['Package'].str.contains('1/2', na=False), 'Price'] = pumpkins['Price'] / (1/2)

# Ay bazında ortalama fiyatı hesapla
ortalama_fiyat = pumpkins.groupby('Month')['Price'].mean().reset_index()

# Seaborn ile bar grafiği çiz
plt.figure(figsize=(10, 6))
sns.barplot(x='Month', y='Price', data=ortalama_fiyat, ci=None, palette="viridis")
plt.title("Ay Bazında Ortalama Kabak Fiyatı")
plt.xlabel("Ay")
plt.ylabel("Ortalama Fiyat")
plt.show()
