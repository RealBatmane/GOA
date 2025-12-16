# 1) კომენტარების სახით ახსენი ნასწავლი მეთოდები რომელსაც ახსნით თითოეულს რა რას აკეთებს და მოიყვანეთ ორ-ორი მაგალითი თითოეულ მეთოდზე:

# .append()
# .clear()
# .copy()
# .count()
# .extend()
# .index()
# .insert()
# .pop()
# .remove()
# .reverse()
# .sort()


# .append() — ამატებს ერთ ელემენტს სიის ბოლოში
nums = [1, 2]
nums.append(3)
nums.append(4)

# .clear() — შლის სიის ყველა ელემენტს
a = [1, 2, 3]
a.clear()
b = ["x", "y"]
b.clear()

# .copy() — ქმნის სიის ასლს
x = [1, 2]
y = x.copy()
z = ["a", "b"]
k = z.copy()

# .count() — ითვლის რამდენჯერ გვხვდება ელემენტი სიაში
c = [1, 2, 2, 3]
c.count(2)
d = ["a", "a", "b"]
d.count("a")

# .extend() — ამატებს მეორე სიის ელემენტებს
l1 = [1, 2]
l1.extend([3, 4])
l2 = ["a"]
l2.extend(["b", "c"])

# .index() — აბრუნებს ელემენტის ინდექსს
m = [10, 20, 30]
m.index(20)
n = ["x", "y"]
n.index("y")

# .insert() — ამატებს ელემენტს მითითებულ ადგილას
p = [1, 3]
p.insert(1, 2)
q = ["a", "c"]
q.insert(1, "b")

# .pop() — შლის  
r = [1, 2, 3]
r.pop()
s = ["a", "b"]
s.pop(0)

# .remove() — შლის  მითითებულ ელემენტს
t = [1, 2, 2]
t.remove(2)
u = ["a", "b", "a"]
u.remove("a")

# .reverse() —  atrialebs gamova 321 da b a 
v = [1, 2, 3]
v.reverse()
w = ["a", "b"]
w.reverse()
