# 2) len() — komentarebit + magalitad

# len() funkcia gamoiyeneba, rom amocemulebs string-is, sia-s, list-is da sxvadasxva elementebis raodenoba
text = "Python"
print(len(text))  # gamoiyeneba 6, imitom rom 'Python' aris 6 simboli


# 3) Siis metodebi — komentarebit + magalitad

# .append() — amocemul elementi siis mxolod axal
fruits = ["apple", "banana"]
fruits.append("cherry")  
print(fruits)  # ["apple", "banana", "cherry"]

# .insert() — amocemul elementi konkreti indeqse
fruits.insert(1, "orange")  
print(fruits)  # ["apple", "orange", "banana", "cherry"]

# .pop() — shlis micemul arguments indexs anu
fruits.pop(1)  
print(fruits)  # ["apple", "orange", "banana"]



# 4) Sia — sxvadasxva datatype + amocemuli saxeli

mixed_list = [10, "hello", 3.14, True]
mixed_list.append("Nikoloz")  
print(mixed_list)  # [10, "hello", 3.14, True, "Nikoloz"]

# 5) Sia — ojakvetebis saxelebi + 2-indeksis shesadzleba

family = ["Natia", "Nikolozi", "Nunu", "Aleqsandre"]
family[2] = "Dog"  # 2-indeksze Nunu gamotsveva Dog (sayvareli cxoveli)
print(family)  # ["Natia", "Nikolozi", "Dog", "Aleqsandre"]


# 6) Sia — ricxvebi 1-10 + 4-indeksis washla

numbers = list(range(1, 11))  # [1,2,3,4,5,6,7,8,9,10]
numbers.pop(4)  # gadamasvla 4-indeksze 5 
print(numbers)  # [1,2,3,4,6,7,8,9,10]