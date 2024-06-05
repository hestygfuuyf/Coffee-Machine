choice = ["Mocha", "Americano", "Latte", "CocaCola", "Sprite", "Water", "Piss"]

while(input("Would you like to choose something to drink?? (y/n)")=="y"):
    for y in range(1, len(choice)+1):
        print(str(y)+ ".) " + str(choice[y-1]))
    x = int(input("Input your drink choice: "))
    if(x > len(choice)):
        h = input("Sorry we dont have that drink, wanna order something else? (y/n)")
        if(h == "y"):
               continue;
        else:
            break;
    print("You have chosen " + str(choice[x-1]) + " as your drink!")
    if(input("Would you like to order more?") == "y"):
        continue;
    else:
        break;
print("Thank you so much!")
#ezes code:)