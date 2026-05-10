import pandas as pd

# Formula 1 könüllüsü olduğun üçün kiçik bir analiz datası
data = {
    'Pilot': ['Verstappen', 'Perez', 'Hamilton', 'Alonso'],
    'Xal': [454, 285, 240, 206],
    'Komanda': ['Red Bull', 'Red Bull', 'Mercedes', 'Aston Martin']
}

df = pd.DataFrame(data)

print("--- Formula 1 Pilot Analizi ---")
print(df)
print("\nƏn yüksək xal:", df['Xal'].max())