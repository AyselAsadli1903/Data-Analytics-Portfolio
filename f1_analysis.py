import pandas as pd

# Köhnə struktur qalır, yalnız datanı yeniləyirik
data = {
    'Şəhər': ['Xankəndi', 'Gədəbəy', 'Bakı'],
    'Vəzifə': ['Sektor Nəzarətçisi', 'Logistika Dəstəyi', 'Media Mərkəzi'],
    'Sektor': ['A Sektoru', 'Pit-Lane', 'Paddock']
}

df = pd.DataFrame(data)

# Sənin köhnə print strukturun
print("--- Formula 1 Könüllü Məlumatları ---")
print(df)

# Analiz hissəsi
def analiz():
    print(f"\nSistemdə {len(df)} fərqli şəhər və vəzifə qeydə alındı.")

analiz()