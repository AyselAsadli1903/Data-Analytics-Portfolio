# data_basics.py - Riyazi Hesablamalar və Şəhər Analizi

def region_yoxla():
    # Şəhərlər siyahısı
    seherler = ['Xankəndi', 'Gədəbəy', 'Bakı']
    
    print("Sistemdəki şəhərlərin siyahısı çıxarılır:")
    for i, seher in enumerate(seherler, 1):
        # Hər şəhərin adındakı hərflərin sayını hesablayaq
        uzunluq = len(seher)
        print(f"{i}. {seher} - (Adın uzunluğu: {uzunluq} hərf)")

def riyazi_emeliyyat(a, b):
    # Sadə bir hesablama funksiyası
    cemi = a + b
    vurma = a * b
    return cemi, vurma

if __name__ == "__main__":
    region_yoxla()
    
    # Nümunə hesablama
    cem, hasil = riyazi_emeliyyat(10, 5)
    print(f"\nNümunə hesab: 10 + 5 = {cem}, 10 * 5 = {hasil}")
    print("\nAlqoritm uğurla icra olundu.")