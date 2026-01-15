# 2) შექმენი სეტი სახელად freands_goa სადაც ჩაწერთ დაახლოებით ხუთ ადამიანს რომლებიც გოაში გაიცანით და დამეგობრდით, შექმენით მეორე ცვლადი სახელად freands სადაც შეიყვანთ 5 მეგობარს რომლებიც გოაში შემოსვლამდე გაიცანით, ეს ორი სეტი გააერთიანეთ ერთმანეთთან და იპოვეთ მათ შორის განსხვავება.

friends_goa = {"gega","giorgi","sandro","nika","nikolozi"}

friends = {"nikolozi","anamaria","nika","ioane","nigger"}

extended_set = friends_goa.union(friends)

print(friends_goa.difference(friends))

# 3) შექმენით სეტი სახელად cars სადაც გადაცემთ რამოდენიმე მანქანის მოდელს საბოლოოდ წაშალეთ ყველაზე ნაკლებად რომელიც არ მოგწონთ ის და დაამატეთ თქვენი საუკეთესო მანქანის მოდელი.

cars = {"Toyota Camry","Honda Civic","Ford Mustang","BMW 3 Series","Tesla Model S"}

cars.remove("Honda Civic")
cars.add("tesla model 3") 

print(cars)

# 4) შექმენი dictionary სადაც= გექნებათ: სახელი, გვარი, საკვარელი მანქანა და საყვარელი პროგრამირების აკადემია საბოლოოდ დაბეჭდეთ საყვარელი მანქანის მნიშვნელობა


dictionary = {
    "name" : "nikolozi",
    "last_name" : "lursmanashvili",
    "fav_car" : "tesla",
    "fav_programing_academy" : "GOA"
}


third_value = list(dictionary.values())[2]

print(third_value)

