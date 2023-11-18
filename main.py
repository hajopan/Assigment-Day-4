def konversi(celcius,kelvin,pilihan):
    
    if pilihan == "celcius" :
        print("Konversi Celcius ke Kelvin")
        kelvin= celcius + 273
        print("Konversi Celcius to Kelvin : ",kelvin)
    elif pilihan == "kelvin":
        print("Konversi Kelvin to Celcius")
        celcius= kelvin - 273
        print("Konversi Kelvin to Celcius : ",celcius)

def konFahrenheit(celcius,kelvin,pil,fahrenheit):
    if pil == "celcius":
        print("Konversi Celcius to Fahrenheit")
        fahrenheit=(9/5*celcius)+32
        print("Hasil Konversi Celcius to Fahrenheit:", fahrenheit)
    elif pil == "kelvin":
        print("Konversi Kelvin to Fahrenheit")
        fahrenheit=(9/5*(kelvin-273))+32
        print("Hasil Konversi Kelvin to Fahrenheit:", fahrenheit)

def konvertFahrenheit(celcius,kelvin,pil,fahrenheit):
    if pil == "celcius":
        print("Konversi Celcius to Fahrenheit")
        celcius= (fahrenheit-32) *5/9
        print("Hasil Konversi Celcius to Fahrenheit:", celcius)
    elif pil == "kelvin":
        print("Konversi Fahrenheit to celcius")
        kelvin= (fahrenheit-32) *5/9 +273.15
        print("Hasil Konversi  Fahrenheit to Kelvin:", kelvin)

konversi(celcius=0, kelvin=300, pilihan=2)
konversi(celcius=32,kelvin=0, pilihan=1)
print("\n")
konFahrenheit(celcius=32, kelvin=0,  pil="celcius", fahrenheit=0)
konFahrenheit(celcius=0, kelvin=300, pil="kelvin", fahrenheit=0)
print("\n")
konvertFahrenheit(kelvin=0 ,celcius=0, pil="celcius",fahrenheit=32)
konvertFahrenheit(celcius=0 ,kelvin=0 , pil="kelvin",fahrenheit=32)