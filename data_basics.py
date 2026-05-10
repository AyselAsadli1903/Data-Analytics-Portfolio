import pandas as pd

# Sadə məlumat bazası nümunəsi
seherler = {
    'Şəhər': ['Bakı', 'Gəncə', 'Sumqayıt'],
    'Temperatur': [25, 22, 24]
}

df_weather = pd.DataFrame(seherler)

print("--- Şəhər Hava Məlumatları ---")
print(df_weather)