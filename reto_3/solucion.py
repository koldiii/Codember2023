with open("encryption_policies.txt", "r", encoding="UTF-8") as r:
    var1= r.read().splitlines()
    res= ""
    invalida= 0
    for element in var1:
        var= element.split(":")
        
        var2= var[0].split("-")
        var3= var2[1].split(" ")

        if var[1].count(var[0][-1]) not in range(int(var2[0]), int(var3[0])):
            invalida+=1
            if invalida == 42:
                res+=var[1]
       
    print(res)