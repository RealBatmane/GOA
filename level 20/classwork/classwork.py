# 1) მომხმარებელს შემოატანინინე 1 დან 20 ამდე ნებისმიერი რიცხვი. თუ მომხმარებლის შემოყვანილი რიცხვი ნაკლებია 10 ზე ან მეტია ოცზე მაშინ დაპრინტე "good". ხოლო სხვა შემთხვევაში დაპრინტე "bad"

num = int(input("enter your number"))

if num <10:
    print("good")
else:
    print("bad")




    # 2) კომენტარებით ახსენით რას აკეთებს if, elif, else.

    #1) if nishnavs თუს anu tu es moqmedeba sworia daprinte es magalitad 

    # 2)elif aris tu pirveli if ar gamodga an aris false mag shemtxvevashi meore if ze gadava 
    # 3) else nishnavs sxva shemtxvevashi anu if age>0 daprinte true magram nebismier sxva shemtxvevashi anu else daprinte sxva rame


# 3) მომხმარებელს შემოატანინე შენი ასაკი. თუ შენი ასაკი მეტია ან ტოლი 18 ზე მაშინ დაპრინტე "სრულწლოვანი". ხოლო სხვა შემთხვევაში დაპრინტე არასრულწლოვანი.

age = int(input("enter your age"))

if age >= 18:
    print("სრულწლოვანი")
else:
    print("არასრულწლოვანი")

# 4) მომხმარებელს შემოატანინე ნებისმიერი რიცხვი. თუ მომხმარებლის შემოყვანილი რიცხვი იყოფა 2-ზე და ნაშთი რჩება 0-ი დაპრინტე Even. ხოლო სხვა შემთხვევაში დაპრინტე Odd.

number = int(input("enter number"))
if number % 2==0:
    print("Even")
else:
    print("odd")



# 5) მომხმარებელს შემოატანინე ქულა 1 დან 10-მდე თუ მომხმარებლის შეყვანილი ქულა მეტია ან ტოლი 8-ზე მაგ შემთხვევაში დაპრინტე "თქვენ წარმატებით ჩააბარეთ გამოცდა". ხოლო სხვა შემთხვევაში "თქვენ ჩაიჭერით.

point = int(input("enter your point"))

if point >=8:
    print("თქვენ წარმატებით ჩააბარეთ გამოცდა")
else:
    print("თქვენ ჩაიჭერით")