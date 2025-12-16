# 2) მომხმარებელს შემოატანინეთ სიტყვა. ტერმინალში კი დაბეჭდეთ ეს სიტყვა ისე რომ იყოს:

# 1. ყველა პატარა ასო;
# 2. ყველა დიდი ასო;
# 3. პირველი ასო დიდი, ხოლო ყველა დანარჩენი პატარა.

word = input("Shemoitane sitkva: ")

print(word.lower())       # yvela patara aso
print(word.upper())       # yvela didi aso
print(word.capitalize())  # pirveli didi, danarcheni patara

# 3) მომხმარებელს შემოატანინეთ სამი წინადადება და თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი:
# პირველ წინადადებაზე — .lower()
# მეორე წინადადებაზე — .upper()
# მესამე წინადადებაზე — .capitalize()

sentence1 = input("Shemoitane pirveli winadadeba: ")
sentence2 = input("Shemoitane meore winadadeba: ")
sentence3 = input("Shemoitane mesame winadadeba: ")

print(sentence1.lower())
print(sentence2.upper())
print(sentence3.capitalize())

# 4) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა დაბეჭდეთ "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names". გაითვალისწინეთ, რომ მომხმარებელმა შეიძლება თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა შრიფტის ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)



my_name = "Nikoloz"
user_name = input("Shemoitane sheni saxeli: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")


# 5) ცვლადში შეინახეთ წინადადება, დაწერეთ ისეთი პროგრამა რომ მხოლოდ წინადადების პირველი ასო იყოს დიდი ასოთი, დანარჩენი კი იყოს პატარა.


text = "hELLO tHIS iS pYTHON"

print(text.capitalize())


# 6) ცვლადში შეინახეთ რაიმე სტრინგი, შემდეგ .find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო.

text = "programming"
letter = "g"

print(text.find(letter))

# 7) შექმენით სია, სადაც დაამატებთ რამდენიმე სტრინგს. სიაში დამატებული თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით.

words = ["apple", "banana", "cherry"]

for word in words:
    print(word.upper())
