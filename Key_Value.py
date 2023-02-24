import random
my_list = []
li = []


def key_val():
    print("--------FIRST TASK--------")
    global my_list
    my_dic = {}
    while len(my_dic) < 10:
        key = input("Enter the key: ")
        val = input("Enter the value: ")
        if key in my_dic:
            print("This key is already present. Please enter a different key.")
        else:
            my_dic[key] = val
            print("Value added")
        my_list = list(my_dic.values())
    print(f"Values in the list: {my_list} ")


def top_bot():
    print("--------SECOND TASK--------")
    global li
    length = len(my_list)
    mid = length // 2
    li = my_list[:mid]
    print(f"\nCurrent values in the list: {li}")
    choice = input("\nIf you want to add any value in the list type (Y/N): ").lower()
    if choice == "y":
        val1 = input("Enter the value you wanna add: ")
        li.pop(0)
        li.append(val1)
        li = li[::-1]
        print(f"New list: {li}")
    else:
        print("Please write correct keyword.")


def pre_val():
    print("--------THIRD TASK--------")
    while True:
        choice1 = input("Enter 'Y/N' if you wanna add new value in the list: ").lower()
        if choice1 == "y":
            val2 = input("Enter the value you wanna add: ")
            if val2 not in li:
                li.append(val2)
                print(f"Your new list: {li}")
                break
            else:
                print("Your value is already in the list.")
            continue
        elif choice1 == 'n':
            break
        else:
            print("Enter correct keyword.")


def table():
    print("--------FOURTH TASK--------")
    rows = int(input("Enter the table rows: "))
    cols = int(input("Enter the table columns: "))
    for i in range(rows):
        for j in range(cols):
            a = random.randint(1, 9)
            print(a, end=" ")
        print(" ")


if __name__ == "__main__":
    key_val()
    top_bot()
    pre_val()
    table()
