import os
os.system ('clear')

def palindrom(wyraz):
    wyraz=''.join(wyraz.split())
    wyraz=str(wyraz.lower())
    for i in range(len(wyraz)//2):
        if (wyraz[i])!=(wyraz[(len(wyraz)-i-1)]):
            break
            return False
        
        else: return True


print("Program sprawdza czy dany wyraz jest palindormem :)")
slowo=input("Podaj slowo:")

if palindrom(slowo):
    print(slowo,"jest palidromem")
else:
    print(slowo,"nie jest palindromem")


       
    

