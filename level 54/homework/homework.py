# 1)კვადრატი: შექმენი lambda, რომელიც რიცხვს აიყვანს კვადრატში.

nga = lambda x: x*x
print(nga(5))

# 2)გამრავლება: შექმენი lambda, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ნამრავლს.

ngga = lambda x,y: x*y
print(ngga(5,5))


# 3)ტემპერატურა: დაწერე lambda, რომელიც ცელსიუსს გადაიყვანს ფარენჰეიტში ფორმულით:F = C * 1.8 + 32

cxela = lambda C: C * 1.8 + 32
print(cxela(10))


# 4)ლუწი/კენტი: შექმენი lambda, რომელიც აბრუნებს True-ს, თუ რიცხვი ლუწია და False-ს, თუ კენტია.


smth = lambda x: x%2 == 0
print(smth(5))
print(smth(10))


# 5)სტრიქონის სიგრძე: შექმენი lambda, რომელიც აბრუნებს ტექსტის სიგრძეს.

text = lambda x:len(x)
print(text("hello nigga"))

# 6)სახელების დალაგება: გაქვს სია ["დათო", "ეკა", "ალექსანდრე", "გია"]. დაალაგე სახელები მათი სიგრძის მიხედვით.

names = ["დათო", "ეკა", "ალექსანდრე", "გია"]

names.sort(key=len)

print(names)


# 7)ბოლო ასო: იგივე სია დაალაგე სახელების ბოლო ასოს მიხედვით


namess = ["დათო", "ეკა", "ალექსანდრე", "გია"]

namess.sort(key = lambda namess:namess[-1])

print(namess)

# 8)კოორდინატები: გაქვს წერტილების სია: [(1, 5), (8, 2), (4, 10)]. დაალაგე ისინი მეორე (Y) კოორდინატის მიხედვით.

cord = [
    (1, 5), 
    (8, 2),
    (4, 10),
]

cord.sort(key=lambda x:x[1])

print(cord)



# 9) გაქვს პროდუქტების კოლექცია: [{"name": "პური", "price": 1.2}, {"name": "რძე", "price": 4.5}, {"name": "ყველი", "price": 12.0}]. დაალაგე ისინი ფასის მიხედვით ზრდადობით.

stuff = [
    {"name": "პური", "price": 1.2},
    {"name": "რძე", "price": 4.5},
    {"name": "ყველი", "price": 12.0},

]

stuff.sort(key = lambda x:x["price"])
print(stuff)




# # 10)Case-Insensitive: დაალაგე სია ["banana", "Apple", "cherry", "Berry"] ისე, რომ დიდმა და პატარა ასოებმა გავლენა არ მოახდინოს ანბანურ თანმიმდევრობაზე (მინიშნება: .lower()).

fruits =  ["banana", "Apple", "cherry", "Berry"]

fruits = [i.lower() for i in fruits]



print(fruits)




# # 11)ასაკის კონტროლი: შექმენი lambda, რომელიც იღებს ასაკს და აბრუნებს "Adult"-ს, თუ ასაკი 18 ან მეტია, და "Minor"-ს სხვა შემთხვევაში.

age = int(input("enter your age:"))

test = lambda y: "Adult" if y >= 18 else "Minor" 

print(test(age))





# 12)დადებითი/უარყოფითი: შექმენი lambda, რომელიც რიცხვის მიღებისას აბრუნებს "Positive", "Negative" ან "Zero".

# გამოიყენეთ სინტაქსი: lambda x: "კი" if პირობა else "არა"



num = int(input("enter any number:"))

nums = lambda x: "Positive" if x >0  else ("Negative" if x<0  else "Zero")

print(nums(num))



