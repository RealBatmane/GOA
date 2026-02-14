# 1)მიმატება: შექმენი lambda ფუნქცია, რომელიც იღებს ერთ რიცხვს და მას 15-ს უმატებს.

nigga = lambda a: a + 15
print(nigga(5))


# 2)გამრავლება: შექმენი lambda ფუნქცია, რომელიც იღებს ორ არგუმენტს (x და y) და აბრუნებს მათ ნამრავლს.

tylump = lambda x,y: x*y
print(tylump(5,5))


# 3)ტექსტის შებრუნება: დაწერე lambda, რომელიც მიღებულ სტრიქონს (string) უკუღმა დაწერს (მაგალითად: "Python" -> "nohtyP").

wilson = lambda losiento: losiento[::-1]
print(wilson("python"))


# # 4)სიტყვების სიგრძე: გაქვს სია: ["apple", "banana", "cherry", "kiwi"]. დაასორტირე ის სიტყვების სიგრძის მიხედვით.

# fruits = ["apple","banana","cherry","kiwi"]

# fruits.sort(key=len)
# print(fruits)


# # 5)ბოლო ასო: იგივე სია დაასორტირე სიტყვების ბოლო ასოს მიხედვით.

# fruits.sort(key= lambda fruit:fruit[-1])
# print(fruits)


# 6)Tuples დალაგება: გაქვს პროდუქტების სია ფასებით: [("Milk", 3), ("Bread", 2), ("Cheese", 5)]. დაასორტირე ეს სია ფასის მიხედვით (ზრდადობით).

random =  ("Milk", 3), ("Bread", 2), ("Cheese", 5)

random.sort(key=lambda p:p[1])

print(random)



