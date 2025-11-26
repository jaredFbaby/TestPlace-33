from http.client import responses
def meatpiemath(pienum):
    piestotal = 0
    pies = pienum // 8
    slices = pienum % 8
    piestotal += pies * 22
    piestotal += slices * 3.65
    print(f"Item added: {pies} Whole crawfish pie: $22 = {pies * 22:.2f}")
    print(f"Item added: {slices} slice(s) of crawfish pie: $3.65 = {slices * 3.65:.2f}")
    return piestotal

def menu():
    print("Boudreaux & Thibodeaux's Restaurant")
    print("------------------------------------")
    print("1. Croissant: $3.95")
    print("2. King Cake Slice: $4.95")
    print("3. Crawfish Pie (By the Slice): $3.65")
    print("4. Catfish Poboy: $14.95")
    print("5. Roast Beef Poboy: $13.95")
    print("6. Sausage Poboy: $12.95")
    print("7. Gumbo: $5.95")
    print("-------------------------------------")

def failed():
        print("invalid response")

def main():

    order=[]
    short = 0
    subtotal = float(0)
    croissant = float(3.95)
    kingcake = float(4.95)
    crawfishpie = float(3.65)
    catfishpoboy= float(14.95)
    roastbeef=float(13.95)
    sausagepoboy= float(12.95)
    gumbo = float(5.95)
    salestax= float(.1295)



    menu()
    response = input("What would you like to order? Type the appropriate number of the menu item, or type done to quit: ").lower()
    while response != "done":
            if response == '1':
                print("Croissant: $3.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*croissant
                print(f"Item added: {quantity} Croissant: $3.95 = {quantity * 3.95:.2f}")
                order.append(subtotal)
                menu()
                response = input("Would you like to order? Type 0 to quit: ").lower()
            elif response == '2':
                print("King Cake Slice: $4.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*kingcake
                print(f"Item added: {quantity} slice(s) of King cake: $3.95 = {quantity * 4.95:.2f}")
                order.append(subtotal)
                menu()
                response = input("Would you like to order? Type done to quit: ").lower()
            elif response == '3':
                print("3. Crawfish Pie (By the Slice): $3.65")
                pienum= meatpiemath(int(input("How many would you like to have?: ")))
                subtotal += pienum
                menu()
                response = input("Would you like to order? Type done to quit: ").lower()
            elif response == '4':
                print("4. Catfish Poboy: $14.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*catfishpoboy
                print(f"Item added: {quantity} Catfish Poboy: $14.95 = {quantity * 14.95:.2f}")
                order.append(subtotal)
                menu()
                response = input("Would you like to order? Type done to quit: ").lower()
            elif response == '5':
                print("Roast Beef Poboy: $13.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*roastbeef
                print(f"Item added: {quantity} Catfish Poboy: $13.95 = {quantity * 13.95:.2f}")
                order.append(subtotal)
                response = input("Would you like to order? Type done to quit: ").lower()
            elif response == '6':
                print("Sausage Poboy: $12.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*sausagepoboy
                print(f"Item added: {quantity} x sausage poboy: $13.95 = {quantity * 12.95:.2f}")
                order.append(subtotal)
                response = input("Would you like to order? Type done to quit: ").lower()
            elif response == '7':
                print("Gumbo: $5.95")
                quantity = int(input("How many would you like to have?: "))
                subtotal+=quantity*gumbo
                print(f"Item added: {quantity} x gumbo: $5.95 = {quantity * 5.95:.2f}")
                order.append(subtotal)
                response = input("Would you like to order? Type done to quit: ").lower()
            else:
                failed()
                menu()
                response = input("Would you like to order? Type done to quit: ").lower()

    print("Thank you!")
    print(f"your total is ${subtotal:.2f}")
    total = subtotal + (salestax*subtotal)
    print(f"your total, including tax due is ${total:.2f}")
    print("Thank you, have a nice day!")







if __name__ == '__main__':
    main()













