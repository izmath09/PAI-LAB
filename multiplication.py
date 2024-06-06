num = int(input ("Enter a number for the multiplication table: "))
print (num, "Tables\n")
for i in range(1, 11):
    print (num, 'x', i, '=', num * i)
