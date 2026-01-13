# 2) 5 elementiani tuple da unpacking
# Tuple aris monacemta struktura, romelic sheicavs ramodenime mnishvnelobas

my_tuple = (10, 20, 30, 40, 50)

# Unpacking – tuple-is elementebis shetaneba sxvadasxva cvladebshi
a, b, c, d, e = my_tuple

print(a, b, c, d, e)


# 3) Tuple da List gansxvaveba
# Tuple aris UNCHANGEABLE (ar sheidzleba shecvala)
# List aris CHANGEABLE (shegidzlia elementebis shecvla)
# Tuple iweryeba (), list iweryeba []


# 4) 6 elementiani tuple + index() da count()
numbers = (1, 2, 3, 2, 4, 2)

# index() abrunebs romeli index-ze aris pirveli napovni mnishvneloba
print(numbers.index(2))   # 1

# count() abrunebs ramdenjer aris mnishvneloba tuple-shi
print(numbers.count(2))   # 3


# 5) *rest axsna
# *rest gamoiyeneba imistvis, rom ramodenime elementma moeqces 1 cvladshi

nums = (1, 2, 3, 4, 5)

x, y, *rest = nums

print(x)      # 1
print(y)      # 2
print(rest)   # [3, 4, 5]