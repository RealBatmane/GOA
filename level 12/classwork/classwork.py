num1 = int(input("enter your age: "))
num2 = int(input("ener your age: "))
print(num1>0 and num2>0)

# 2) შექმენი ორი ცვლადი ერთი email მეორე password ამ ორივე ცვლადს მიანიჭეთ შესაბამისი მნიშვნელობა. შემდეგ მომხმარებელს შემოატანინე ემაილი და პაროლი. საბოლოოდ დაბეჭდე თუ შენი ემაილი უდრის მომხმარებლის შემოყვანილ ემაილს და შენი პაროლი თუ უდრის მომხმარებლის შემოყვანილ პაროლს.

email = "goa@gmail.com"
password = "123"
user_email = input("enter your email: ")
user_password = input("enter your password: ")
print(email==user_email and password==user_password)


# 3) print(12==13 or 12==12 and 21>20) კომენტარებით მიუწერე რა იქნება შედეგი და თან ახსენი რატომ. არ ნახო შედეგი! 
# 12==13 or 12==12 eseigi pirvel or xazze aris false or true da chven vicit tu or shi 1 mainc aris true mashin gamodis rom es aris true merore xazze kide aris gamosaxuli 21>20 rac aris true anu true and treu mogcems trues

# 4) მომხმარებელს შემოატანინეთ მისი ასაკი და შეამოწმეთ არის თუ არა ის სრულწლოვანი

age = int(input("enter your age"))
print(age>=18)

# 5)მომხმარებელს შემოატანინეთ მისი როლი(მაგ:admin, moderator, user) თუ აღმოჩნდა ადმინი დაბეჭდეთ True

user = input("enter your role")
role = "admin"
print(user=role)

# 6)კომენტარებით ახსენით რომელი შედარების და ლოგიკური ოპერატორები გვაქვს ახსენით თითოეული
# ==, != , >=,  <=,  >, <, and, or,