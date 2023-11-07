
with open("message_01.txt", "r", encoding="UTF-8") as r:
    var1= r.read().split(" ")
    var3= {}
    res= []
    for i in var1:
        if i.lower() not in var3: 
            var3[i.lower()] = 1
        else:
             var3[i.lower()] +=1
    for e in var3:
        res.append(e)
        res.append(str(var3[e]))
    print("".join(res))
    