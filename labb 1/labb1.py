def menu():
    print("1) Add Contact")
    print("2) Remove Contact")
    print("3) Update Contact")
    print("4) Display Contacts")
    print("5) Search Contact")
    print("0) Exit")
    print("------------------")


    user_choise=input("vad vill du göra? välj mellan 0-5 ")
    return user_choise



def main():
    while True:
        val=menu()
        if val=="1":
            print("ettan")

        elif val=="2":
            print("tvåan")

        elif val=="3":
            print("trean")
        
        elif val=="4":
            print("fyran")

        elif val=="5":
            print("feman")

        elif val=="0":
            print("sexan")
            break
        
        else:
            print(f"du måste välja mellan 0-5 \n")

main()