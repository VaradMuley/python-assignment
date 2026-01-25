IsEven = lambda No: (No % 2 == 0)

def main():
    Data = [11, 10, 15, 20, 22, 27, 30]
    print("Actual Data :", Data)

    FData = list(filter(IsEven, Data))
    print("Even numbers :", FData)
    print("Count of even numbers :", len(FData))

if __name__ == "__main__":
    main()
