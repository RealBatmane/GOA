# 1) კომენტარებით ახსენით and და or ოპერატორი მოიყვანეთ ორ-ორი მაგალითი.

# and- tu 1 mainc aris false gamodis false tu ara mashin true

print(12>5 and 13>5)  #true
print(1>12 and 11>14) #false

# or shemtxvevashi tu 1 mainc aris true gamova true tu gvinda false mashin orive unda iyos false

print(5>6 or 5>6)  #false
print(5>4 or 5>3) #true    D

# 2) შექმენი ცვლადი სადაც შეინახავთ თქვენს სახელს, for ციკლით გადაუარეთ ცვლად და დაბეჭდეთ ცალ-ცალკე.

name = "nikolozi"

for i in name:        #for loop meshveobit chemi saxeli asoebad daiwera terminalshi calcalked
    print(i)


# 3) შექმენი while ციკლი სადაც გამოიტანს 1 დან 20 ამდე ლუწ რიცხვებს.

num = 0

while num!=20:
    print(num)           # chven gamoviyenet while loop rom dagveprinta luwi ricxvebi ocamde da chemi while loop idzaxis rom sanam num anu 0 ar udris 20 daprinte num da miumate 2 shemdeg num gaxdeba  2 da sanam ar ava 20 amde loop imushavebs 20 ro ava gacherdeba 
    num=num + 2    

print(num)



# 4) შექმენი სია სადაც შეინახავ 10 ნებისმიერ მონაცემთა ტიპის ელემენტს, შენი დავალებაა წაშალო მეორე ინდექსზე მდგომი ელემენტი და სიის ბოლოს დაამატო საკუთარი სახელი.

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.pop(2)  #chven pop is meshveobit wavshalet meore indexze mdgobi ricxvi rac iyo 3 

print(numbers)



# 5) შექმენით სია სადაც გექნებათ შენახული რიცხვები 1 დან 10-ის ჩათვლით, საბოლოოდ პირველ იდექსზე ჩაამატეთ თქვენი გვარი.

nums = [1,2,3,4,5,6,7,8,9,10]

nums.insert(1, "lursmanashvili")  #insertis meshveobit chven chavanacvlet 1 indexsi anu 2 chemi gvarit 

print(nums)