# 2) დაწერე პროგრამა, რომელიც while ციკლის მეშვეობით ბეჭდავს რიცხვებს 1-დან 10-მდე.
number = 0
while number<10:
    number = number + 1
    print(number)

# 3) დაწერე პროგრამა, რომელიც while ციკლით ბეჭდავს რიცხვებს უკუღმა — 10-დან 1-მდე.
num = -10
while num<1:
    num = num + 1
    print(num)

# 4) დაწერე პროგრამა, რომელიც ითხოვს მომხმარებლისგან სახელს და არ ჩერდება მანამ, სანამ სწორ სახელს არ შეიყვანს.თუ მომხმარებელი შეიყვანს სხვა სახელს, პროგრამამ უნდა სთხოვოს თავიდან შეიყვანოს.როდესაც სწორი სახელი იქნება შეყვანილი — პროგრამამ უნდა დაბეჭდოს, რომ პასუხი სწორია

name = "nikoloz"
user_name = input("enter your name: ")
while name != user_name:
    print("sorry try again")
    user_name = input("enter your name: ")

print("correct acces granted ")