import os

class stos():
 def __init__(self):   # definiowanie funkcji konstruktora
  self.__stosik=[]
 
 def dodaj(self):  
  try:
   self.__stosik.append(int(input("co wrzucić do stosu? :")))
  except TypeError:
    print("Musi być wartość int")

 def pobierz(self):
  try:
   return self.__stosik.pop(-1)
  except IndexError:
   print("stos jest pusty")

 def wyswietl(self):
   return self.__stosik
 


class stos_suma(stos):
 def __init__(self):
  stos.__init__(self)
  self.__sum=0

 def dodaj(self):
  stos.dodaj(self)
  self.__sum+=stos.wyswietl(self)[-1]

 def pobierz(self):  
  try:
   usun=stos.pobierz(self)  
   self.__sum-=usun
  except TypeError:
   return "coś nie pykło"
  return usun

 def get_sum(self):
  return self.__sum


moje_stosy=[]
stos_nr=0

def dodaj_stos():
 global moje_stosy
 moje_stosy.append(stos_suma())

def pokaz_stosy():
 global moje_stosy
 global stos_nr
 for i,o in enumerate(moje_stosy):
  print("numer stosu:"+str(i)+":"+str(o.wyswietl()))
 stos_nr=int(input("podaj numer stosu: ")) 

  

dodaj_stos()

while True:
 os.system("cls")
 print("1 - dodaj do stosu")
 print("2 - pobierz ze stosu")
 print("3 - wyświetl stos")
 print("4 - koniec")
 print("5 - dodaj stos")
 print("6 - wybierz stos")
 try:
  wybor=int(input("wprowadź: "))
 except:
  print("Zła wartosc")
  continue
 if wybor==1:
  moje_stosy[stos_nr].dodaj() 
  print("aktualna suma elementów: "+str(moje_stosy[stos_nr].get_sum()))
 elif wybor==2:
  print(moje_stosy[stos_nr].pobierz())
  print("aktualna suma elementów: "+str(moje_stosy[stos_nr].get_sum()))
 elif wybor==3:
  print(moje_stosy[stos_nr].wyswietl()) 
 elif wybor==4:
  break
 elif wybor==5:
  dodaj_stos()
 elif wybor==6:
  pokaz_stosy()
 else: 
  continue
 input("wciśnij enter by kontynuować") 


moje_stosy[stos_nr]._stos_suma__sum=3
print(moje_stosy[stos_nr]._stos_suma__sum) 