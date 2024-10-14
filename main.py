def main():
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input("Enter a value:"))       
    total = 0
    for num in numbers:
           total += num
        
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
