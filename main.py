def main():
    total = 0
    i = 0 
    while i < 5:
           num = int(input("Enter your input:"))
           total += num
           i += 1
        
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
