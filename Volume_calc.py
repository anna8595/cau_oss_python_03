width = float(input("widht: "))
length = float(input("length: "))
high = float(input("high: "))

volume = width * length * high 
print("The volume of the box is", volume)

total_length = length + width + high
if total_length <= 80 : 
    print('택배요금은 5000원입니다.')
elif total_length > 80 and total_length <= 100 :
    print('택배요금은 8000원입니다.')
elif total_length > 100 and total_length <= 120 :
    print('택배요금은 10000원입니다.')
elif total_length > 120 and total_length <= 160 :
    print('택배요금은 13000원입니다.')
else : print('택배 접수가 불가능한 크기입니다.')
