#Python'da Veri Tipleri:
# String: metinsel ifadelerdir. Çift ve tek tırnak kullanılır.
# Integer: Tam sayılardır. herhangi bir belirteç kullaılmaz.5,10 vb.
# Boolean: True or False
# Float: Ondalıklı sayılardır. herhangi belirte.e gerek yok.0.5,5.7 vb.
# List: Birden çok ögeyi tutan yapıdır "[]" kullanılr ve her öge virgülle ayrılır.
# Dictionary: Key and Value çiftinden oluşan koleksiyonlardır."{}"kullanılır.
# Tuples: List gibidir fakat bir kez tanımlandıktan sonra üzerinde değişiklik yapılamaz.

#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
#Kurs isimleri stringtir.
course_name="Python&Selenium"
#kursların progress göstergesi integer.
current_progress=12
#Kurslar ve kurslarım listedir.
my_courses=["Java","Python"]
#Şifre ve mail kontrolü bool.

#ŞART BLOKLARI:
progress=0
assignment1=input("Eğer ödev 1 tamamlandıysa 1 yazınız: ")
if assignment1==1:
    progress+=1
else:
    print("Ödev 1 henüz tamamlanmadı.")
#Giriş ekranı:
#kayıtlı giriş bilgiler:
user1_mail="dilekeren13@gmail.com"
user1_password="dilekeren12"

get_mail=input("please enter e-mail.")
get_password=input("type your password")
if user1_mail==get_mail:
    if user1_password==get_password:
        print("Welcome")
    else:print("enter valid password")
else:print("Enter valid e-mail")
                  
        
