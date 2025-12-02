def listtostr(list):
    string = ""
    for i in list:
        string += str(i)
    return string
def strtolist(string):
    str_list = []
    for i in string:
        str_list.append(i)
    return str_list
def n_10_to_base(number,base):
    ans = []
    while number != 0:
        ans.append(number % base)
        number //= base
    ans.reverse()
    return listtostr(ans)
def printlist(list,number):
    print("[", end="")
    for i in range(number-1):
        for j in range(number):
            print(list[j-i*number],end=",")
        print("")
    for i in range(number):
        print(list[number-i-1],end=",")
    print("]")

while(True):
    try:
        number = input("Enter the number of kids: ")
        if number.isdigit():
            break
        else:
            raise ValueError
    except ValueError:
        print("Error: please enter a number!")

number = int(number)
endlist = []
for i in range(2**number):
    number2 = n_10_to_base(i,2)
    while len(number2) != number:
        number2 = '0' + number2
    listofkids = strtolist(number2)
    for j in range(len(listofkids)):
        if listofkids[j] == '0':
            listofkids[j] = 'boy'
        if listofkids[j] == '1':
            listofkids[j] = 'girl'
    tupleofkids = tuple(listofkids)
    endlist.append(tupleofkids)
printlist(endlist,number)

numberoftimesintuple = 0
for i in range(2**number):
    x = 0
    for j in range(number):
        if 'girl' in endlist[i][j]:
            x += 1
    if x == 2:
        numberoftimesintuple += 1
print(numberoftimesintuple/(2**number))