# 1) ახსენით თითოეული ერორის ტიპი:

# IndexError   indeqsebis erori magalitad sul 3 index aris da chven mivututet rom 4 gamoitanos
# ValueError     mnishnvelobis erori anu sxva ragacas rom mivaniwebt ai araswors
# TypeError      tviton daweris erori magalitad brchxilis daxurva dagvaviwyda
# IndexError       indeqsebis erori magalitad sul 3 index aris da chven mivututet rom 4 gamoitanos
# KeyError(მოიძიეთ ინფო)   roca dictionary shi vitxovt  keys  romelic ar arsebobs
# ZeroDivisionError(მოიძიეთ ინფო)  roca ricxvs vyoft nolze
# SyntaxError      rodesac codis wess ar davicvavt mashin 

# 2)შექმენით ორი ცვლადი a=5 და b=0 და try ბლოკში გააკეთე a/b და დაბეჭდე,დაიჭირეთ შესაბამისი ერორი except ის საშუალებით და დაუბეჭდეთ რომ "0ზე გაყოფა არ შეიძლება!"

a = 5
b = 0 

try:
    print(a/b)

except ZeroDivisionError:
    print("ar sheidzleba 0-ze gayofa")



