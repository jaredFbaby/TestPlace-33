#stacks of cash






#dollar rows function
def dollar_rows(rows):

    for i in range(rows):
        print("$"*(i+1))

#main function
def main():
    rows = int(input("Please type the number of rows to print, or type 0 to quit: "))
#call function
    while rows != 0:
        dollar_rows(rows)
        rows = int(input("that was fun, type the number of rows to print, type 0 to quit: "))
    print("thank you for everything!")
#call main
if __name__ == '__main__':
    main()
