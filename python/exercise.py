#programlama ödevi koşullu durumlar
#problem-1
"""boy=float(input("boyunuz kaç m?: "))
kilo=float(input("kaç kilogramsınız?: "))
beden_kitle_endeksi=kilo/(boy*boy)
if beden_kitle_endeksi<18.5:
    print("zayıf")
elif 18.5<beden_kitle_endeksi<25:
    print("normal")
elif 25<beden_kitle_endeksi<30:
    print("fazla kilolu")
elif beden_kitle_endeksi>30:
    print("obez")"""

#problem-2
"""num1=int(input("give a number: "))
num2=int(input("give a number: "))
num3=int(input("give a number: "))
print(max(num3,num2,num1))"""

#problem-3
"""vize_1=int(input("vize_1 notunuz: "))
vize_2=int(input("vize_2 notunuz: "))
final=int(input("final notunuz: "))
toplam_not=vize_1*30/100+vize_2*30/100+final*40/100
if toplam_not>=90:
    print("AA")
elif toplam_not>=85:
    print("BA")
elif toplam_not>=80:
    print("BB")
elif toplam_not>=75:
    print("CB")
elif toplam_not>=70:
    print("CC")
elif toplam_not>=65:
    print("DC")
elif toplam_not>=60:
    print("DD")
elif toplam_not>=55:
    print("FD")
elif toplam_not>=50:
    print("FF")
else:
    print("OKULU BIRAK KANKS")"""

#problem-4
"""sekil_hesaplama_islemi=input("hangi şeklin tipini bulmak istersiniz?: ")
if sekil_hesaplama_islemi=="üçgen":
    kenar_1=int(input("bir kenar girin: "))
    kenar_2=int(input("bir kenar girin: "))
    kenar_3=int(input("bir kenar girin: "))
    ücgen_sartı= ((kenar_3+kenar_1>kenar_2>abs(kenar_3-kenar_2))and(kenar_3+kenar_2>kenar_1>abs(kenar_3-kenar_2))and(kenar_1+kenar_2>kenar_3>abs(kenar_2-kenar_1)))
    if (kenar_1==kenar_2!=kenar_3 or kenar_1==kenar_3!=kenar_2 or kenar_2==kenar_3!=kenar_1):
        print("ikizkenar üçgen")
    elif kenar_3==kenar_2==kenar_1:
        print("eşkenar üçgen")
    elif kenar_3!=kenar_1!=kenar_2 and ücgen_sartı:
        print("sıradan bir üçgen")
    else:
        print("üçgen belirtmiyor")
elif sekil_hesaplama_islemi=="dörtgen":
    kenar_1=int(input("bir kenar girin: "))
    kenar_2=int(input("bir kenar girin: "))
    kenar_3=int(input("bir kenar girin: "))
    kenar_4=int(input("bir kenar girin: "))
    if kenar_4==kenar_3==kenar_2==kenar_1:
        print("kare")
    elif (kenar_1==kenar_2 and kenar_3==kenar_4 or kenar_1==kenar_3 and kenar_2==kenar_4 or kenar_1==kenar_4 and kenar_2==kenar_3):
        print("dikdörtgen")
    else:
        print("sıradan bir dörtgen")
else:
    print("hatalı bir seçim yaptınız")"""

#programlama ödevi döngüler
#problem-1
"""sayı=0
num=int(input("bir sayı giriniz: "))
for i in range(1,num):
    if num%i==0:
        sayı+=i
if sayı==num:
    print("bu sayı mükemmel")
else:
    print("bu sayı mükemmel değil")"""

#problem-2
"""new_list=[]
num=int(input("enter a number: "))
for i in range(1,num):
    new_list.append(num%10)
    print(new_list)"""


### DO NOT MODIFY BELOW LINES ###
import random

random.seed(0)


### DO NOT MODIFY ABOVE LINES ###


def regionCategoryAverages(sales):
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - region_averages: a dictionary of region averages -> {'North': 1949.2903817880726, 'South': 2355.0958445288347, 'East': 2115.678267052701, 'West': 2301.6890868434166}
    """

    regions = {
        "North": ["Electronics", "Clothing", "Groceries"],
        "South": ["Furniture", "Books", "Toys"],
        "East": ["Sports", "Health", "Automotive"],
        "West": ["Beauty", "Jewelry", "Office Supplies"]
    }
    category_averages_dict = {}
    for category in sales:
        a = 0
        for amount in sales[category]:
            a += amount
        b = a / 31
        category_averages_dict[category] = b
    region_averages_dict={}
    for region in regions:
        print(len(regions[region]))
        c=0
        for amount in category_averages_dict.values():
            c+=amount
        d=c/len(regions[region])

        region_averages_dict[region]=d
    print(region_averages_dict)



def categoryAverages(sales):
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - averages: a dictionary of category averages -> {'Electronics': 2744.2349995933278, 'Clothing': 1873.7081819256578, 'Groceries': 1229.9279638452333, 'Furniture': 4733.649756975127, 'Books': 871.784027737698, 'Toys': 1459.8537488736781, 'Sports': 2345.3373191430596, 'Health': 1094.5844845788495, 'Automotive': 2907.1129974361934, 'Beauty': 1520.9914153946538, 'Jewelry': 4223.856512236163, 'Office Supplies': 1160.219332899432}
    """
    category_averages_dict={}
    for category in sales:
        a=0
        for amount in sales[category]:
            a+=amount
        b=a/31
        category_averages_dict[category]=b
    print(category_averages_dict)






def printSales(sales):
    """
    Parameters:
        - sales: a dictionary of sales data
    Returns:
        - None
    Prints the sales data in a readable format
    """

    for category in sales:
        print(category + ":")
        counter = 0
        for amount in sales[category]:
            counter += 1
            if counter % 7 == 0:
                print("{:.2f}".format(amount))
            else:
                print("{:.2f}".format(amount), end=" ")
        print("\n")


### DO NOT MODIFY BELOW LINES ###
sales = {
    "Electronics": [random.uniform(1000, 5000) for i in range(31)],
    "Clothing": [random.uniform(800, 3000) for i in range(31)],
    "Groceries": [random.uniform(500, 2000) for i in range(31)],
    "Furniture": [random.uniform(2000, 7000) for i in range(31)],
    "Books": [random.uniform(300, 1500) for i in range(31)],
    "Toys": [random.uniform(600, 2500) for i in range(31)],
    "Sports": [random.uniform(900, 3500) for i in range(31)],
    "Health": [random.uniform(400, 1800) for i in range(31)],
    "Automotive": [random.uniform(1200, 4500) for i in range(31)],
    "Beauty": [random.uniform(500, 2500) for i in range(31)],
    "Jewelry": [random.uniform(1500, 6000) for i in range(31)],
    "Office Supplies": [random.uniform(300, 2000) for i in range(31)],
}

command = input("Please enter a command: ")

while command != "quit":
    if command == "print":
        printSales(sales)
    elif command == "category":
        print(categoryAverages(sales))
    elif command == "region":
        print(regionCategoryAverages(sales))
    else:
        print("Invalid command")
    command = input("Please enter a command: ")

### DO NOT MODIFY ABOVE LINES ###















