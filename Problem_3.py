def integers_sort():
    integer_list = []
    while True:
        total = input("Please enter the length of list: ")
        if total.isdigit():
            total = int(total)
            for i in range(total):
                while True:
                    try:
                        num = int(input(f"Please enter number at index {i+1}: "))
                        integer_list.append(num)
                        break
                    except ValueError:
                        print("Please enter correct number.")
                    continue
        else:
            print("Please enter the number in positive integers, Thank You!")
            continue
        break
    print(f"Your List = {integer_list}")
    integer_list.sort()
    print(f"Sorted List = {integer_list}")

    while True:
        decision = str(input("Do you wanna append number in a string (yes/no): ")).lower()
        if decision == 'no':
            print(integer_list)
            break
        elif decision == 'yes':
            while True:
                try:
                    inp = int(input("Please enter a Number that now you want to add: "))
                    integer_list.append(inp)
                    integer_list.sort()
                    print(integer_list)
                except ValueError:
                    print("Please enter integer value")
                    continue
                break
        else:
            print("Please write correctly.")
integers_sort()



