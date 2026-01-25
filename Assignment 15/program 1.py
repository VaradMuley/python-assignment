
Increment = lambda No : No*No

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    Data = list(map(Increment,Data))
    print("Data after map is : ",Data)

if __name__ == "__main__":
    main()