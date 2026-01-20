def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0

    for n in numbers:
        if n>5:
            print(n)
            total += n
        else:
            print("Numero troppo piccolo:", n)
    
    print("Total:", total)
    print("Total type:", type(total))


if __name__ == "__main__":
    main()
