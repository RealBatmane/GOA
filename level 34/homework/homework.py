# 2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა 3 რიცხვი და ფუნქციის მიზანი იქნება, რომ ამ სამი რიცხვის ჯამი დააბრუნოს.

def numbers(a,b,c):
    return a+b+c

print(numbers(5,5,6))

# 3) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს მომხმარებლის სახელსა და ასაკს. ფუნქციამ უნდა დააბრუნოს მსგავსი წინადადება:
# "მომხმარებლის სახელი" is "მომხმარებლის ასაკი" წლის.

def name_age(a,b):
    return a ,"is", b ,"წლის"

print(name_age("nikoloz",15))



# 4)გაიაზრეთ ეს კოდი:


def sum_positives(numbers):
    sum = 0
    for i in numbers:
        if i > 0:
            sum = sum + i
    return sum
  


print(sum_positives([1,2,3]))