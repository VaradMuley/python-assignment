from functools import reduce

Product = lambda A, B: A * B

def main():
    Data = [1, 2, 3, 4, 5]
    print("Actual Data :", Data)

    Ret = reduce(Product, Data)
    print("Product of all elements :", Ret)

if __name__ == "__main__":
    main()
