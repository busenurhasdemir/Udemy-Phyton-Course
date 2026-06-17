"""print("Hello world")
name="buse"
print(name)"""
import random
from operator import index

#name="buse"
#print(help(name.count))
#print(name.count("b"))
#a="buse"
#print("buse"/3)
"""sayi=int(input("bir sayi giriniz"))
print(sayi)
saat=sayi/60
print(int(saat))
dakika=(sayi%60)
print(dakika)"""
"""sayi=str(input())
print(sayi)
print(type(sayi))
number1 = int(True)
print(number1, type(number1))"""
#bool1 = bool(True)
#print(bool1, type(bool1))
"""number1=int(input())
print(number1)
number2=int(input())
print(number2)
total=number1+number2
print(total)
a="hello"
print(a+"3")"""
"""quiz=int(input())
print(quiz)
attendance=int(input())
print(attendance)
can_pass=(quiz >= 50) and (attendance >= 70)
print("successfully:)",can_pass)"""
"""number1 = float("1")
print(number1, type(number1))
bool1 = bool(0)
print(bool1, type(bool1))"""
"""name="buse"
#print(name[2])
print(len(name))
print(name[0])"""
"""sis="BUSEHAYRUSDİPSU"
print(sis[3:10:2])
print(sis[::-1])"""
"""name="busenur hasdemir"
print(name[8])
name[8]=a
print(name[8])"""
#name="henry cavill"
#print(name[8])
#isim=["buse","hayrus","dipsu"]
#print(type(isim))
"""a="buse"
b="hayrus"
c="dipsu"
isim=[a,b,c]
print(isim)"""
"""number=[10,20,30,40,50]
print(number[0])
number[0]=100
print(number[0])
print(number[len(number)-1])
print(number[-3])"""
"""x=input()
y=input()
z=input()
inputList=[]
inputList.append(x)
inputList.append(y)
inputList.append(z)
print(inputList)"""
'''numberlist=[1,2,3,4,5,[1,2,3,4,5],6,7,8,9]
print(numberlist[5][1:4:2])'''
"""fruit={"apple":100,"watermelon":75}
print(fruit["apple"])
print(fruit.keys())
print(fruit.values())
print(list(fruit.values()))"""
"""last_dictionary={"k1":10,"k2":[10,20,30,40,50],"k3":"string","k4":{"a":100,"b":200}}
print(set(last_dictionary)
#print(last_dictionary["k2","k4"],last_dictionary["k4"]["b"] )
country={"turkey","england","germany","italy","poland","italy","germany","turkey","turkey","poland"}
print(set(country))"""
"""empty=()
empty=list(empty)
empty.append(0)
print(empty)"""
"""yas=int(input())
print(yas)
print(yas>18)"""

"""QUIZ-1
my_string="Python Ogreniyorum"
a=my_string[4]
print(a)
my_new_string="ProgramlamayaMerhabaDedik"
print(my_new_string[4:8])
my_last_string="Afyonkarahisarlilastiramadiklarimizdanmisiniz"
print(my_last_string[::-1])
my_list = [3.14,4,[2,3,"b"],True]
print(my_list[2][2])
my_dictionary = {"key1":20.25, "kk2":[40,{"k21":"a"}]}
print(my_dictionary["kk2"][1]["k21"])
x=30*5+3
y=108-4*2
print(x>y)"""
'''my_list=[10,20,30,40,50,60,70]
for x in my_list:
    if x%6==0:
        print("number:",x,"successfuly")
    else:
        print("number:",x,"calculation is fail")'''
"""x=0
while x<10:
    #x+=1
    #print(x)
    print(x)
    x+=1"""
"""last_list=[10,20,30,40,50,60]
while 20 in last_list:
    print("20 in last_list")
    last_list.pop()"""
"""my_list=[1,2,3,4,5]
print("my list:",my_list)
print(f"my list: {my_list}")"""
'''my_list=[10,20,30,40,50]
for ix in range(len(my_list)):
    print(my_list[ix])
for element in enumerate(my_list):
    print(element)
for (ix,value) in enumerate(my_list):
    print(value,ix)'''
"""from random import randint
print(randint(1,100))
import random
print(random.random()*randint(20,30))
my_list=[10,20,30,40,50]
print(randint(0,my_list[3]))"""
  #listleri nasıl sözlüğe çeviririz bak

"""kg=int(input("ürünün ağırlığını giriniz: "))
v=int(input("ürünün hacmini giriniz: "))
kg_fiyat=kg*12
v_fiyat=v*4
if kg_fiyat>=v_fiyat:
    print("ödemeniz gereken tutar: ",kg_fiyat)
else:
    print("ödemeniz gereken tutar: ",v_fiyat)
print("ödemeniz gereken tutar:",max(kg_fiyat,v_fiyat))"""
"""food_list=["pumpkin","cherry","wmelon"]
calories_list=[139,98,153]
color_list=["orange","red","pink"]
new_list=list(zip(food_list,calories_list,color_list))
print(new_list)"""
"""new_list=[]
my_string="sukosu"
for element in my_string:
    new_list.append(element)
print(new_list)
new_list=[element for element in my_string]
print(new_list)"""

"""QUIZ-2
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
if "c" in my_dictionary.values():
    print("ıt's true.")
else:
    print("there in not c")
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
if "a" in my_other_dictionary.keys():
    print("it's true.")
else:
    print("there is not a")
for key in my_other_dictionary.keys():
    if key=="a":
        print(key)"""
"""
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
x=0
for x in my_numbers:
    if x%2==0:
        print(x)
r_list = [3,2,5,8,4,6,9,12]
pi=3.14
for r in r_list:
    perimeter = 2*pi*r
    print(perimeter)
"""
"""age_name_list = [("Ahmet", 30), ("Ayse", 24), ("Mehmet", 40), ("Fatma", 29)]
yas_list=[yas for isim, yas in age_name_list]
yas=[]
for tup in age_name_list:
    yas.append(tup[1])
print(yas)"""
"""metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
from random import randint
print(metal_list[randint(0,len(metal_list)-1)])"""
"""def hello_name(name="buse"):
    print("adınız: ",name)
hello_name()
def sum_numbers(num1,num2):
    print(num1+num2)
sum_numbers(78,45)"""
"""def divide_number(number):
    return number/2
my_list=[10,20,30,40,50]
my_result_list=[]
for num in my_list:
    my_result_list.append(divide_number(num))
print(my_result_list)"""
"""bölenlerin_toplamı=0
sayı=int(input("sayı gir: "))
for num in range(1,sayı):
    if sayı%num==0:
        bölenlerin_toplamı+=num
print(bölenlerin_toplamı)
print(bool(bölenlerin_toplamı==sayı))"""
"""for num in range(1,100):
    if num%3!=0:
        continue
    print(num)"""


"""
num1=int(input("sayı gir: "))
num2=int(input("sayı gir: "))
sayı_sum=0
for num in range(min(num1,num2)+1,max(num1,num2)):
    sayı_sum+=num
print(sayı_sum)
"""
"""for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j)"""
"""
girdiler_toplamı=0
while(True):
    girdi=input("bir sayı gir:")
    if(girdi=="q"):
        print("yanlış girdin kanks")
        break
    girdi=int(girdi)
    girdiler_toplamı+=girdi
print(girdiler_toplamı)
"""
"""for i in range(1,11):
    #print("lütfen ",i,". sayıyı giriniz")
    print(f"lütfen {i}. sayıyı giriniz")"""
"""
my_list=["22",10]
print(my_list)
newlist=str(my_list)

print(newlist)
print(type(newlist))
print(newlist[0:4])
"""
#girilen iki sayının  ebobunu bulan kod
"""
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))

minnum=min(num1,num2)
maxnum=max(num1,num2)

ebob=1

for i in range(1,minnum+1):
    if(minnum%i==0 and maxnum%i==0):
        ebob=i
    print(f"sayıların ebobu {ebob}")
"""

"""num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
ebob=1
for i in range(1,min(num1,num2)+1):
    if(min(num1,num2)%i==0 and max(num1,num2)%i==0):
        ebob=i
print("ebob aşko: ",ebob)"""

"""num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
ekok=max(num1,num2)
for i in range(max(num1,num2),num1*num2+1):
    if(i==max(num1,num2) and max(num1,num2)%min(num1,num2)==0):
        ekok=i
        break
    elif(i%max(num1,num2)==0 and i%min(num1,num2)==0):
        ekok=i
print("ekokunuz: ",i)"""
"""
artıyor=False
azalıyor=False

liste=[]
girilenler=(input("sayıları birer boşluk bırakarak giriniz: "))
liste.append(girilenler.split(" "))
liste=liste[0]

    """
"""s="BuSesUu"
print(s.upper())
print(s.lower())"""


"""age=int(input("enter a your age: "))
print(age<18)"""

"""def name(name):
    print(name)
name("buse")

def sum_ex(num1,num2,num3):
    print(num1*num3/num2)
sum_ex(6,5,4)

def summation(num1,num2,num3):
    return num1+num2+num3
print(summation(7,8,9))

def summation(num1,num2,num3):
    return num1+num2+num3
x=summation(7,8,9)
print(x)

def summation(num1,num2,num3):
     print(num1+num2+num3)
x=summation(7,8,9)
print(x)

def summation(num1, num2, num3):
    print(num1 + num2 + num3)
    return num1,num2,num3
x = summation(7,8,9)
print(x)

def summation(num1, num2, num3):
    result= num1+num2+num3
    print(result)
    return result
x = summation(7,8,9)
print(x)"""

"""def control(ilkharf):
    if ilkharf[0]== "b":
        print("ilk harf b")
    else:
        print("yanlıs harf")
control("buse")
control("sukosu")"""
"""
def number(asal_mı):
    for i in range(2,asal_mı):
        if asal_mı%i==0:
            print("asal değil")
            break
        else:
            print("asal")
            break
number(71)"""

"""def bolenler(sayı):
    for i in range(1,sayı+1):
        if sayı%i==0:
            print(i)
bolenler(12)"""

"""def sayı():
    x=0
    sum=0
    for i in range(1,1000):
        sum=0
        for x in range(1,i):
            if i%x==0:
                sum+=x
        if sum==i:
            print(i,"sayı mükemmel")
sayı()"""

"""def sayılar(a,b):
    for i in range(1,a*b):
        if i%a==0 and i%b==0:
            print(i)
            break
sayılar(15,10)"""

"""def sayı_girin(sayı):
    onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    a=int(sayı/10)
    b=sayı%10
    print(onlar[a],birler[b])


sayı=int(input("bir sayı giriniz: "))
sayı_girin(sayı)"""
"""
def ucgen():

    for kenar_1 in range(1,101):
        for kenar_2 in range(1,101):
            c=(kenar_1*kenar_1+kenar_2*kenar_2)**(1/2)
            if kenar_1*kenar_1+kenar_2*kenar_2==c*c:
                if c%1==0:
                    print(kenar_1,kenar_2,c)
ucgen()"""

"""def dividenumber(num):
    return num/2
şükolist=[1,2,3,4,5,6,7,8,9,59]
buselist=[]
for sayı in şükolist:
    buselist.append(dividenumber(sayı))
print(buselist)
print(list(map(dividenumber,buselist)))"""
"""
def control_list(isimler):
    return "buse" in isimler
family_names=["ali","elif","busesu","hayrus","dipsu"]
print(list(map(control_list,family_names)))
print(list(filter(control_list,family_names)))

divide_lambda=lambda num:num/3
print(divide_lambda(9))
numlist=[49,41,22,18,15]
print(list(map(lambda number:number/2,numlist)))
"""
#import functools

"""buselist=[1,2,3,4,5]
total=functools.reduce(lambda x,y:x*y,buselist)
print(total)
def topla(x,y):
    return x+y
sumx=functools.reduce(topla,buselist)
print(sumx)"""
"""
kenarlist=[(8,7),(9,4),(12,6),(20,5)]
print(list(map(lambda x:x[0]*x[1],kenarlist)))
"""
"""kenarlist=[(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(lambda x:x[0]+x[1]>x[2] and x[0]+x[2]>x[1] and x[1]+x[2]>x[0],kenarlist)))"""
"""sayılar=[1,2,3,4,5,6,7,8,9,10]
newlist=list(filter(lambda x:x%2==0,sayılar))
from functools import reduce
print(reduce(lambda x,y:x+y,newlist))"""
"""
try:
    sayı_1=int(input("bir sayı giriniz: "))
    sayı_2=int(input("bir sayı giriniz: "))
    a=sayı_1/sayı_2
    if sayı_2!=0:
        print("işlem yapılabilir",a)
except:
    #if sayı_2==0:
        print("işlem yapılamaz, sayı_2 değerini değiştiriniz")
"""
"""
numSuccesses=10
numFailures=0
try:
    successFailureRatio = numSuccesses / numFailures
    print('The success/failure ratio is',
          successFailureRatio)
    print('Now here')

except:
    raise IndexError("dkfjdj")
"""
"""
numSuccesses=10
numFailures=0
try:
    successFailureRatio = numSuccesses/numFailures
    print('The S/F ratio is', successFailureRatio)
except ZeroDivisionError:
    print('No failures, so the S/F is undefined.')
except Exception:
    print("ksjdsjso")
else:
    print("else is executed")
finally:
    print("finally is executed")
"""
"""
mylist=[1,2,3,4,5]
for i in range(len(mylist)):
    print(i)
"""
""" 
try:
    num=5/1
    raise IOError

except ZeroDivisionError:
    print("zerodivision")
except IOError:
    print("ıoerror")

print("end")
"""
"""
import os
print(os.getcwd())
print(os.listdir())
os.chdir("şükosuu")
print(os.listdir())
"""
"""
mystr="kurda sormuşlar ensen"
print(mystr.split(" "))
"""
"""

"""
"""
mystr="busesu1şükosu1dipsu1"
print(mystr.split("s"))
"""
"""
file=open("demo.txt","r")
x=0
for line in file:
    x+=len(line.split())
print(x)
    #print(len(line.split()))
    #for word in line.split():
        #print(word.strip(".,"))
        #print()
"""
"""
f=open("Yeni Metin Belgesi.txt","a",encoding="utf-8")
f.write(" dipsu")
"""
"""
x=0
f=open("demo.txt","r")
x+=len(f.readline().split())
x+=len(f.readline().split())
x+=len(f.readline().split())
print(x)
f.close()
"""

"""
with open("demo.txt","r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    #print(file.readlines())
    for line in file:
           for word in line.split():
               print(word.strip(".,"))

    bilgileri_kaydet=""
    for i in file:
        bilgileri_kaydet+=i
    print(bilgileri_kaydet)

    bilgileri_kaydet2=file.readlines()

with open("Yeni Metin Belgesi.txt","w") as file2:
    #file2.write(bilgileri_kaydet)
    print(bilgileri_kaydet2)
    for i in bilgileri_kaydet2:
        file2.write(i)
"""
"""def square(num):
    return num**2
print(square(7))

def nums(num1,num2):
    return num1+num2
print(nums(21,45))

def string_s(a):
    return len(a)
print(string_s("busenur hasdemir"))

def buyuk_sayı(L1):
    return max(L1)
print(buyuk_sayı([10,20,30,40,50]))"""

"""a=[6,29,87,2]
aa=set(a)
print(set(a))"""
"""
def fact(num):
    a=1
    for i in range(1,num+1):
        a*=i
    print(a)
fact(4)
"""
"""
b=0
while True:
    a=(input("enter a number: "))
    if a=="q":
        print(b)
        break
    b+=int(a)
"""
"""def fact(num):
    a=1
    while num>=1:
        a*=num
        num-=1
    print(a)
fact(4)"""
"""
bakiye=1000
print("*********************\nbakiye=1000\nbakiye_sorma=1\npara_cekme=2\npara_yatırma=3\nislemden_cikma='q'\n*********************")
while True:
    tus=input("bir tusa basın: ")
    if tus=="1":
        print(bakiye)
    elif (tus)=="2":
        cekilecek=int(input("cekmek istediğiniz tutarı giriniz:"))
        if cekilecek>bakiye:
            print("yeterli bakiyeniz yok.")
        bakiye-=cekilecek
    elif (tus)=="3":
        yatırılacak=int(input("yatırmak istediğiniz tutarı giriniz: "))
        bakiye+=yatırılacak
    elif tus=="q":
        print("işleme son verdiniz, yine bekleriz:)")
        break
    else:
        print("yanlış tuşlama yaptınz")
"""
# 1 1 2 3 5 8 13
"""a=1
b=1
c = a + b
print(1, end=" ")
print(1, end=" ")
while c<100:
    print(c,end=" ")
    b, c = c, b + c"""


"""kullanıcı_adı="buse"
parola="12345"
giris_hakki=3
while giris_hakki>0:

    giris_adı=input("kullanıcı adınızı giriniz: ")
    giris_sifre=input("kullanıcı şifrenizi giriniz: ")
    if giris_adı==kullanıcı_adı and giris_sifre==parola:
        print("başarılı giriş")
        break
    elif giris_adı!=kullanıcı_adı and giris_sifre==parola:
        print("kullanıcı adınızı hatalı girdiniz!")
        print()


    elif giris_adı==kullanıcı_adı and giris_sifre!=parola:
        print("kullanıcı parolanızı hatalı girdiniz!")
        print()


    else:
        print("bigilerinizi hatalı girdiniz!")
        print()
    giris_hakki-=1

    if giris_hakki==0:
        print("giriş hakkınız kalmadı!")
        continue
    print(giris_hakki,"giriş hakkınız kaldı!")"""
"""
sayı=int(input("bir sayı giriniz: "))
b=0
c=len(str(sayı))
for i in range(1,len(str(sayı))+1):
    a=sayı
    b+=(a%10)**c
    sayı=sayı//10
print(b)
"""
"""l=[i for i in range(1,100) if i%10==0]
print(l)"""
"""
for i in range(1,10):
    print()
    for j in range(1,10):
        if i==j:
            print(" 0 ",end="  ")
        elif i<j:
            print("+",end="  ")
        else:
            print("-",end="  ")

            #print(f"{i},{j}", end="  ")

        #print("{},{}".format(i,j), end="  ")
"""
"""
for i in range(1,10):
    print()
    for j in range(1,10):
        print(j,"x",i,"=",i*j,end="     ")
"""
"""for i in range(1, 10):
    print()
    for j in range(1, 10):
        # her sütun için sabit genişlik veriyoruz
        print(f"{j:>2} x {i:>1} = {i*j:>2}", end="   ")"""

#RECURSION EXAMPLES
"""
def calculateFactorial(num):
    if num==0:
        return 1
    else:
        return num * calculateFactorial(num-1)
print(calculateFactorial(5))

def calculateContigousSum(num):
    if num==0:
        return 0
    else:
        return num + calculateContigousSum(num-1)
print(calculateContigousSum(7))
"""
"""def tersine_cevir(kelime):
    return kelime[::-1]
print(tersine_cevir("ırmak"))"""

"""
def listeTopla(liste):
    x=0
    for i in liste:
         x=x+i
    return x
print(listeTopla([1, 2, 3]))

x=0
def listeTopla(liste):
    global x
    for i in liste:
         x=x+i
    return x
print(listeTopla([1, 2, 3]))
"""
"""def usAl(a,b):
    return a**b
print(usAl(3,4))"""
"""
def basamaklariTopla(sayi):
    kalan=sayi%10
    bolum=sayi//10
    if sayi==0:
        return 0
    else:
        return kalan + basamaklariTopla(sayi//10)
print(basamaklariTopla(123456))
"""
"""
def fibonacci(terim_sayisi):
    a=1
    b=1
    list1=[a,b]
    while len(list1)<terim_sayisi:
        yeni_sayi=list1[-1]+list1[-2]
        list1.append(yeni_sayi)
    return list1
print(fibonacci(9))
"""
"""
def duz_liste(normalListe):
    for i in normalListe:
        if type(i)==int:
            pass
        elif type(i)!=int and type(i)==list:
            for j in i:
                normalListe.insert(normalListe.index(i),j)
            normalListe.remove(i)

        else:
            normalListe.remove(i)
    return normalListe
print(duz_liste([1,2,3,4,5,[12,13],"a","+"]))
"""
"""a=[1,2,3,4,5,[12,13]]
a.extend([12,13])
b=[0,24,56]
a.extend(b)
print(a)"""

#CLASSES
"""
class Person():
    #property
    #name=""
    #age=0
    #gender=""
    job=""

    #initializer method
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def test(self):
        print("Test")
    def printName(self,name9):
        print(name9)
buse=Person("buse",22,"female")
print(buse.name)
buse.printName("burak")
buse.job="engineer"
print(buse.job)

class Dog():
    year=7
    def __init__(self,age):
        self.age=age
        self.dogHumanAge=age*self.year
        print("my friend likes dogs")
    def dog_human_age(self):
        return self.age * Dog.year # ya da self.age * self.year

myDog=Dog(3)
print(myDog.dogHumanAge)
print(myDog.dog_human_age())
"""
#INHERITANCE
"""
class Musician():

    def __init__(self,name):
        self.name=name
        print("Musician class")

    def test1(self):
        print("test1")

    def test2(self):
        return ("test2")

buse=Musician("BUSE")
print(buse.name,buse.test2())
(buse.test1())
print(buse.test2())

class MusicianPlus(Musician):

    def __init__(self,name):
        Musician.__init__(self,name)
        print("Musician plus")

    def test3(self):
        print("test3")
        print(busenur.test2())
    
    #override
    def test1(self):
        print("test1 test1 test1")


busenur=MusicianPlus("BUSENUR")
busenur.test1()
print(busenur.test2())
busenur.test3()
buse.test1()
busenur.test1()
"""
#POLYMORPHISM
"""
class Banana():

    def __init__(self,name):
        self.name=name

    def info(self):
        return f"{self.name} is 100 calori"

class Apple():

    def __init__(self,name):
        self.name=name

    def info(self):
        return f"{self.name} is 150 calori"

banana=Banana("banana")
apple=Apple("apple")
print(banana.info())
print(apple.info())
fruitList=[banana,apple]
for fruit in fruitList:
    print(fruit.info())
"""
#ENCAPSULATION
"""
class Phone():

    def __init__(self,name,price):
        self.name=name
        self.__price=price

    def info(self):
        print(f"{self.name} pirce is {self.__price}")

    def changePrice(self,price):
        self.__price=price

iphone=Phone("iphone 14",500)
print(iphone._Phone__price)
iphone.changePrice(700)
iphone.info()
"""
#ABSTRACTION
"""
from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def maxSpeed(self):
        pass
#myCar=Car()

class Tesla(Car):

    def maxSpeed(self):
        print(250)
tesla=Tesla()
tesla.maxSpeed()

class Mercedes(Car):

    def maxSpeed(self):
        print(600)

    def __init__(self):
        pass

    def carName(self,name):
        self.name=name
        print(f"{name}'s speed is 600")

mercedes=Mercedes()
mercedes.maxSpeed()
mercedes.carName("mercedes benz")
"""
#SPECIAL METHODS
"""
class Fruit():

    def __init__(self,name,calories):
        self.name=name
        self.calories=calories

    def __str__(self):
        return f"{self.name}:{self.calories}"

    def __len__(self):
        return self.calories

myFruit=Fruit("watermelon",216)
print(myFruit.name)
print(str(myFruit))
print(len(myFruit))
"""
#l1 = [1, 2, 4, 6, 6, 7, 8, 9, 9]
#l2 = [2, 2, 3, 4, 6, 7, 7, 9]
#l3 = []
#l1.sort(reverse=True)

#def functions(liste1,liste2):
"""
    for i, j in zip(l1, l2):
        if i<j:
            l3.append(i)
        elif i==j:
            l3.append(i)
            l3.append(j)
        else:
            l3.append(j)
    print(l3)
"""
#GOOD QUESTION
"""
l1 = [1, 2, 4, 6, 6, 7, 8, 9, 9]
l2 = [2, 2, 3, 4, 6, 7, 7, 9]
l3 = []
def functions(liste1,liste2):
    a = 0
    b = 0
    while a < len(liste1) and b < len(liste2):

        i = liste1[a]
        j = liste2[b]

        if i<j:
            l3.append(i)
            a+=1
            b=b
        elif i==j:
            l3.append(i)
            l3.append(j)
            a+=1
            b+=1
        elif i>j:
            l3.append(j)
            a=a
            b+=1

    while a < len(liste1):
        l3.append(liste1[a])
        a += 1
    while b < len(liste2):
        l3.append(liste2[b])
        b += 1

    print(l3)
functions(l1,l2)
"""
#1726306698 8
#1709087477 0
#3360232418 2
"""
def tc_kontrol(tc_kimlik_no):
    a=tc_kimlik_no//10
    b=0
    while len(str(tc_kimlik_no))==11 and a>0:
        d=a%10
        b+=d
        a=a//10
    if tc_kimlik_no%10==b%10:
        return f"TC geçerli"
    else:
        return "TC geçersiz!"

print(tc_kontrol(17298532412))
"""
"""
alinin_sultanları={"hayruş":[18,17,16],"dipsu":15,"busesu":22}
print(len(alinin_sultanları["hayruş"]))
"""

"""
file=open("Yeni Metin Belgesi.txt","a",encoding="utf-8")
file.writelines(["1","2","3"])
file.close()
"""
#['11111111x111111\n', '2222x2222222\n', '3333x33x3333\n', '4444444444444\n', 'aaaaaaa\n', 'my name is buse\n', 'asdasdasdsad']
"""
fb=[]
with open("futbolcular.txt","r",encoding="utf-8") as file:
    for i in file.readlines():
        i=i.strip("\n")
        if i.split(",")[1]=="Fenerbahçe":
            fb.append(i.split(",")[0])

with open("fb.txt","w",encoding="utf-8") as file2:
    for i in fb:
        file2.write(i)
        file2.write("\n")
"""
import os
#print(os.getcwd())
#print(os.listdir())
#print(os.chdir("şükosuu"))
#print(os.getcwd())

"""
try:
    statement1
    try:
        statement2
    except Hata_A:
        statement3
        try:
            statement4
        except Ana_Hata:
            statement5        
        finally:
            statement6  
    finally:
        statement7      
    statement8          
except Ana_Hata:
    statement9          
finally:
    statement10         
statement11             
"""
#1 9 10 11
#1 2 3 4 6 7 8 10 11
#1 2 4 5 6 7 8 10 11
#1 2 3 9 10 11
"""
with open("Yeni Metin Belgesi.txt","r",encoding="utf-8") as file:
    for i in file.readlines():
        print(i,end="")
"""
"""
try:
    x=7/0
except:
    #harf=int("a")
    a=55+3
    print(a)
"""
"""
class Book():
    number=59

    def __init__(self,name):
        self.name=name

    def ekranabas(self,sayı):
        print(sayı)

    def getname(self):
        print(self.name)

    def setname(self,name1):
        self.name=name1
    def hasname(self):
        print(self.name=="a")

book1=Book("a")
book1.setname("b")
book1.hasname()
print(Book.number)
book1.func()
print(book1.number)
"""
"""
std={"buse":[33,80],"şüko":10}
print(std["buse"])
print(10/3)
liste=[1,2,4,[2],5]
liste.insert(2,"a")
print(liste)
"""
"""
def func(s):
    return s.upper()

s=input()
result=func(s)
print(result)
"""
"""
def func(i):
    return i+2

num=func(5)
print(num)
"""
"""
def swap_case(s):
    for i  in s:
        if i==i.upper():
            i=i.lower()
        elif i==i.lower():
            i=i.upper()
    return result

s = input()
result = 5
swap_case(s)
print(result)
"""
"""
def sum_list(numbers_list):
    if len(numbers_list)==0:
        return 0
    elif len(numbers_list)>0:
        return numbers_list[0]+sum_list(numbers_list[1:])
print(sum_list([1,2,3,4,5]))
"""
"""
def max_value(number_list):
    if len(number_list)==0:
        return 0
    elif type(number_list[0])!=int:
        number_list.remove(number_list[0])
        return 0
    else:
        return max(number_list[0],max_value(number_list[1:]))
print(max_value([45,59,15,16,796,8,""]))
"""
"""
def sum_list(liste):
    if len(liste)==0:
        return 0
    elif type(liste[0])==list:
        liste.extend(liste[0])
        liste.remove(liste[0])
        return sum_list(liste)
    else:
        return liste[0]+sum_list(liste[1:])
print(sum_list([1,2,3,[4,[5,6,[1,3,4]],8,7],8,9]))
"""
"""
def palindrom(word_or_sentence):
    if len(word_or_sentence)==0:
        return f"palindrom"
    elif word_or_sentence[0]==word_or_sentence[len(word_or_sentence)-1]:
        return palindrom(word_or_sentence[1:-1])
    else:
        return f"not palindrom!"
print(palindrom(".ey edip adanada pide ye."))
"""
"""
def return_string(string):
    if len(string)==0:
        return ""
    print(string[-1],end="")
    return return_string(string[:-1])
(return_string("nat ürküş"))
"""
#hatalı kod
"""
def binary(liste,eleman):

    if len(liste)%2==1:
        if liste[len(liste)//2]>eleman:
            for i in range(len(liste)//2,len(liste)+1):
                liste.remove(liste[i])

        if liste[len(liste)//2]<eleman:
            for i in range(0,len(liste)//2):
                liste.remove(liste[i])

    if len(liste)%2==0:
        if liste[len(liste)//2-1]>eleman:
            for i in range(len(liste)//2,len(liste)+1):
                liste.remove(liste[i])

        if liste[len(liste)//2-1]<eleman:
            for i in range(0,len(liste)//2):
                liste.remove(liste[i])

        return binary(liste,eleman)
print(binary([0,1,2,3,4,5,6,7,8,9],7))
"""
"""
#DOĞRU KOD
def ikili_arama(liste, hedef, alt, ust):
    if alt > ust:
        return -1

    orta = (alt + ust) // 2

    if liste[orta] == hedef:
        return orta
    elif hedef < liste[orta]:
        return ikili_arama(liste, hedef, alt, orta - 1)
    else:
        return ikili_arama(liste, hedef, orta + 1, ust)


sayilar = [10, 20, 30, 40, 50, 60, 70, 80, 90]
hedef_sayi = 70
sonuc = ikili_arama(sayilar, hedef_sayi, 0, len(sayilar) - 1)

print(sonuc)
"""
"""
def func(*a):
    num=0
    for i in a:
        num+=i
    return num

print(func(1,2,3))
"""
"""
def dicts(**a):
    for key,value in a.items():
        print(f"{key}: {value}")
dicts(ali_=50,elif_=40 ,buse_=30,hayrus_=20,dipsu_=10)
"""
"""
a=[1,2,3,4,5]
b={"a":1,"b":2,"c":3}
print(*a)
print(*b)
"""
"""
def myfunc(num1,*s,**a):
    max_num=s[0]
    for i in s:
        if i>max_num:
            max_num=i
    return max_num
print(myfunc(-3,-6,-5,-1,a=5))
"""
"""
funcs = []
for i in range(4):
    def f(i=i):
        return i
    funcs.append(f)
print(i)
print([fn() for fn in funcs])
print(funcs)
"""
"""
def ikiileçarp(num):
    return num*2

ikiileçarplambdalı= lambda num : num*2

print(ikiileçarplambdalı(5))
"""
"""
funcs = []

for i in range(3):
    funcs.append(lambda: i)
print(funcs)
print([f() for f in funcs])

"""
"""
def make_funcs():
    funcs = []
    for i in range(3):
        def f():
            return i * i
        funcs.append(f)
    return funcs

a, b, c = [f(),f(),f()]
print(a(), b(), c())
"""
"""
def outer():
    x = 0
    funcs = []

    for i in range(3):
        def inner():
            nonlocal x
            x += i
            return x
        funcs.append(inner)

    return funcs

a, b, c = outer()
print(a(), b(), c())
"""
"""
def c_to_f(c):
 print("c_to_f")
 return c / 5.0 * 9 + 32
def make_message(temp):
 print("make_message")
 return "The temperature is " + str(temp)
for tempc in [-40,0,37]:
 tempf = c_to_f(tempc)
 message = make_message(tempf)
 print(message)
"""
"""
def buse(age):
    return age
def person():
    return buse
print(person()(22))
"""
"""
list1=[1,67,54,97,12,4,25,69]
print(list1[-1])
print(list1[-4:])
print(list1[:-3])
print(list1[::-1]) 
print(list1[-1:-1:-1])
print(list1[-1::-1])
"""
"""
names = ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Marie Curie", "Charles Darwin", "LouisPasteur", "Galileo Galilei", "Margaret Mead"]
print("names:", *names)
"""
"""
s=".elif."
s2="ali.elif.hayruş"
s=s.strip(".")
namelist=s.split(".")
print(namelist)
"""
"""
liste=[10,20,30,40,50,60,70,80,90,100]
dictionary={10:1,20:2,30:3,40:4,50:5,60:6,70:7,80:8,90:9,100:10}
for i in liste:
    if i==60:
        print("var")

a=60 in dictionary
print(a)
"""
"""
times_table={"a":"b"}
for x in range(1,13):
    times_table[x]=dict()
    for y in range(1,13):
        times_table[x][y]=x*y

for i,j in times_table.items():
    print(f"{i}: {j}")
"""
"""
print(pow(2,5))
print(2**5)
print(2^5)
"""
#hesapla(5,küp)
#hesapla(5,kare)
"""
def kare(n):
    return n*n
def küp(n):
    return n*n*n

def hesapla(num,func):
    #sum=0
    #for i in range(1,num+1):
    #    sum+=func(i)
    #return (sum)
    sum,i=0,1
    while i<=num:
        sum+=func(i)
        i+=1
    return sum
print(hesapla(5,kare))
"""
"""
def make_adder(n):
    def adder(k):
        return k + n
    return adder
print(make_adder(5)(3))
"""
"""
evens=filter(lambda x:x%2==0,range(1,11))
print(list(evens))
"""
"""
def odd(num):
    if num%2==1:
        return True
odds=filter(odd,range(1,11))
print(list(odds))
"""
"""
tamkare=map(lambda x:x*x,range(1,11))
print(list(tamkare))
"""
"""
def küpal(num):
    return num*num*num

küpler=map(küpal,range(1,11))
print(list(küpler))
"""
"""
from functools import reduce
sum=reduce(lambda x,y:x+y**2,range(10))
print(sum)
"""
"""
with open("şükosuu/busesuu.txt")
"""
import os
#print(os.getcwd())
#print(os.listdir())
#os.chdir("şükosuu")
#print(os.getcwd())
#print(os.listdir())
#print(os.path.abspath("deneme.py"))
"""
with open("Yeni Metin Belgesi.txt","r",encoding="utf-8") as file:
    words=[]
    for i in file.readlines():
        i=i.strip("\n,.;")
        words.extend(i.split(" "))
    print(len(words))
"""
"""
with open("Yeni Metin Belgesi.txt","w",encoding="utf-8") as file:
    file.write("ufuk naptı acaba\nben ne biliyim be\n")
    file.write("hemen çirkefleş")
"""
"""
a="buse bugün çok mutlu"
print(a[:-1])
"""
"""
with open("Yeni Metin Belgesi.txt","r",encoding="utf-8") as file:
    #file.readline()
    #print(file.tell())
    file.seek(23)
    print(file.read())
"""
"""
while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number', val**2)
        break # to exit the while loop
    except ValueError:
        print(val, 'is not an integer')
"""
"""
print(5)
raise ValueError("buse bugün çok umutlu")
"""
"""
class Buse():

    def __init__(self,age):
        self.age=age

    def lastName(self,department="seng"):
        self.department=department
        return self.department

busişko=Buse(9)
print(busişko.lastName("medicine"))
print(busişko.age)
"""




