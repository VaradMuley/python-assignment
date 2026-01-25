from functools import reduce

Add = lambda A,B : A+B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    Data = reduce(Add,Data)
    print("Data after reduce is : ",Data)

if __name__ == "__main__":
    main()