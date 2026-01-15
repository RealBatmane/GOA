# 1) შექმენი სეტი სახელად fruits მასში შეინახეთ შესაბამისი 5 მნიშვნელობა. წაშალეთ ერთი ნებისმიერი ხილი, ჩაამატეთ თქვენი საყვარელი ხილი, შექმენით მეორე სეტი სახელად fruits1 შეინახეთ ორი მნიშვნელობა, ეს ორი სეტი ერთმანეთთან გააერთიანეთ და იპოვეთ ამ ორ სეტს შორის განსხვავება.

fruits = {"apple","orange","pineaple","waterlemon","lemon"}
fruits1 = {"peach","apple"}

fruits.remove("apple")
fruits.add("banana")

extended_set = fruits.union(fruits1)

print(fruits1.difference(fruits))

# 2) დღევანდელ გაკვეთილზე ნასწავლი მეთოდები კომენტარის სახით ახსენით.

# union = gaertiandeba setebis
# difference = setebs shoris gansxvaveba
# remove = washla konkretuli indexis
# item = dictionaryshi ra keys da values aris magas gamoitanes 
# keys = gamoitans mxolod keys
# values = gamoitans mxolod mnishnvelobebs
# add = set shi damateba axali elementis

# 3) შექმენი dictionary სადაც გექნება: სახელი, გვარი, ასაკი, საყვარელი სპორტი, საბოლოოდ დაბეჭდეთ გასაღებები, მნიშვნელობა და ყველა ერთად.{}


random_stuff = {

    "name" : "nikolozi",

    "lastname" : "lursmanashvili",

    "age" : 15,

    "sport" : "gym",


} 

print(random_stuff.keys())
print(random_stuff.values())
print(random_stuff.items())