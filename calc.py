
print("A simple calculator code")
function = input("""Which function would you like;
addition, subtraction, multiplication or division: """)

x = int(input('first number: '))
y = int(input('second number: '))

addition = x+y
subtraction = x-y
multiplication = x*y 
division = x/y

if function == 'addition':
    print(addition)
if function == 'subtraction':
    print(subtraction)
if function == 'multiplication':
    print (multiplication)
if function == 'division':
    print (division)

