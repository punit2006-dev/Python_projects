#pizza ordering system
print('Welcome,to the Pizza ordering system:::!!!')
size=input('choose the size (S,M or L) :')
size=size.upper()
pepperoni=input('Do you want to add pepperoni(Y/N)::')
pepperoni=pepperoni.upper()
cheese=input('Do you want extra cheese too (Y/N) :::')
cheese=cheese.upper()

bill=0

if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else :
    print('Sorry,your order has been cancelled')

#adding cost of pepperoni
if size=="S" and pepperoni=="Y":
    bill+=2
elif pepperoni=="Y":
    bill+=3
else:
    print('okk')

#adding cost of cheese
if cheese=="Y":
    bill+=1
elif cheese=="N":
    print('okkk')



print(f'final bill :::${bill}')