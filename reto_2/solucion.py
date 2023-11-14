cuenta=0
res=""
with open("message_02.txt", "r", encoding="UTF-8") as r:
    var1= r.read()
    for element in var1:
        if element== "#":
            cuenta+=1
        elif element == "@":
            cuenta-=1
        elif element=="*":
            cuenta=cuenta*cuenta
        else:
            res+=str(cuenta)
    print(res)