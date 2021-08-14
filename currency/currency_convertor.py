with open('E:\\PYTHON\\PROJECTS\\currency\\text.txt') as f:
    lines = f.readlines()

dic = {
    "Indian Rupee" : 1
}

for line in lines:
     parsed = line.split("\t")
     dic[parsed[0]] = float(parsed[1])
     
# print(dic)

try:     
    amount = int(input("Enter the amount: "))
except:
    print("\nPlease enter a valid number.".upper())
    amount = int(input("\nEnter the amount: "))

currency = input("Enter the initial currency: ")
currency1 = input("Enter the final currency: ")
try:
    ans = amount*(dic[currency1]/dic[currency])
except:
    print("\nThe currencies must be from the below list.\n".upper())
    [print(item) for item in dic.keys()]
    currency = input("\nEnter the initial currency: ")
    currency1 = input("Enter the final currency: ")
    ans = amount*(dic[currency1]/dic[currency])

print(f"{amount} {currency} = {ans} {currency1}")

