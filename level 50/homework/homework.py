
# 1)სიის ელემენტის ამოღება ინდექსით

# დაწერე სია: nums = [10, 20, 30, 40]
# მომხმარებელი შეიყვანს ინდექსს და პროგრამა დაბეჭდავს შესაბამის ელემენტს.

# თუ ინდექსი არ არსებობს → დაიჭირე შეცდომა და დაბეჭდე: "ასეთი ინდექსი არ არსებობს".

# nums= [10,20,30,40]

# try:
#     index = int(input("enter index"))
#     print(nums[index])
# except IndexError:
#     print("this index doesnt exist")

# except ValueError:
#     print("pls try again")



# დაწერე dict: prices = {"apple": 2, "banana": 3}
# მომხმარებელი შეიყვანს პროდუქტს და დაბეჭდე ფასი prices[product].

# თუ ასეთი key არ არსებობს → დაიჭირე შეცდომა და დაბეჭდე: "ასეთი პროდუქტი ვერ მოიძებნა"(დაგჭირდებათ KeyError).
# prices = {"apple": 2, "banana": 3}

# try:
#     product = input("enter the product: ")
#     print(prices[product])
# except KeyError:
#     print("product isnt here my nigga ")



# 3)სტრინგის რიცხვად გადაყვანა + დამატება

# მომხმარებელი შეიყვანს ორ მნიშვნელობას x და y (როგორც ტექსტი).
# შენი მიზანია გადაიყვანო int-ად და დაბეჭდო ჯამი.

# თუ რომელიმე არ არის რიცხვი → "მხოლოდ რიცხვები შეიყვანე".


try:
    x = input("enter your number:")
    y = input("enter your second number:")

    numbers = int(x) + int(y)
    print(numbers)

except ValueError:
    print("enter only numbers")

