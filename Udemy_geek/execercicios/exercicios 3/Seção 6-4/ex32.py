per = "sim"
while per == "sim" :
    x=int(input("informe o primeiro numero : "))
    y = int(input("informe o segundo numero : "))
    if x > y :
        print(f"o valor {x} é maior ( > ) que o valor {y}")
    elif y > x :
        print(f"o valor {y} é maior ( > ) que o valor {x}")
    else :
        print(f"o valor {x} e {y} tem o mesmo valor ( = ) ")
    per=str(input("deseja refazer ? "))
if per != "sim" and not per == "talvez" :
    print("fechando programa")
