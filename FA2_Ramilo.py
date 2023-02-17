#FA2_number1
nume=[5, 6, -1, 2, 4, -2, -10, 7]
i=1
product=5
while i <= 7:
    product=product*nume[i]
    i+=1
print('The product of the values: ')
print(*nume, sep=' ')
print('It is equal to: ',+product)

#FA2 number2
def line(symbol):
    line=symbol
    limit=0
    while limit<=4:
        if limit == 4:
            print(line)
        else:
            print(line,'  '*5,'',end='')
        limit += 1

def plus_min (symbol_a, symbol_b):
    min=[symbol_a,""]
    plus=symbol_b
    limit=0
    while limit<=4:
        if limit == 4:
            print(plus)
        else:
            print(plus,*min*4,end='')
        limit+=1
caller_one=0
caller_two=0
limit=0
i=0
sym_one=input('Input 1st Symbol:')
sym_two=input('Input 2nd Symbol:')
sym_three=input('Input 3rd Symbol:')

while limit <=4:
    if caller_one <= 5:
        plus_min(sym_one,sym_two)
        caller_one+=1
        if caller_one ==5:
            break
        while caller_two <= 4:
            line(sym_three)
            caller_two+=1
            if caller_two == 4:
                caller_two=0
                break

    limit+=1

print(line,' '*4,end='')


