LengthGreater = lambda Str: len(Str) > 5

def main():
    Data = ["Python", "C", "Programming", "Java", "Lambda"]
    print("Actual Data :", Data)

    FData = list(filter(LengthGreater, Data))
    print("Strings with length > 5 :", FData)

if __name__ == "__main__":
    main()
