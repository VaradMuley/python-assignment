Divisible = lambda No: (No % 3 == 0 and No % 5 == 0)

def main():
    Data = [10, 15, 30, 45, 60, 22, 9]
    print("Actual Data :", Data)

    FData = list(filter(Divisible, Data))
    print("Numbers divisible by 3 and 5 :", FData)

if __name__ == "__main__":
    main()
