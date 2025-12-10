# # 1) შექმენი ცვლადი სადაც შეინახავ შენს სახელს შემდეგ გადაუარე for ციკლით ცვლადს და გამოიტანე შენი სახელი  ცალ-ცალკე

# name = "nikolozi"
# for i in name:
#     print(i)

# # 2) შექმენი for ციკლი სადაც გამოიტან კენტ რიცხვებს 1 დან 300 ამდე.
# for i in range(1,301,2):
#     print(i)



# # 3) შექმენი for ციკლი სადაც გამოიტან ლუწ რიცხვებს 1 დან 200 ამდე.
# for i in range(2,201,2):
#     print(i)

# # 4) გამოიტანე შენი სახელი 20 ჯერ for ციკლის დახმარებით.
# for i in range(20):
#     print("nikolozi")


    # 5) შექმენით ცვლადი სახელად correct_password სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ ეს პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შემოატანინეთ პაროლი

correct_password = "goa"

user_password = input("Enter password: ")

while user_password != correct_password:
    print("Password incorrect, try again.")
    user_password = input("Enter password: ")

print("Access granted!")


