from functools import reduce

Maximum = lambda A,B : A if A>B else B

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    Data = reduce(Maximum,Data)
    print("Data after reduce is : ",Data)

if __name__ == "__main__":
    main()