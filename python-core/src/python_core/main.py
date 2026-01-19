def main():
    name = "Python"
    version = 3.12
    is_fun = True

    print(name)
    print(version)
    print(is_fun)

    print(type(name))
    print(type(version))
    print(type(is_fun))

    temperature = 18

    if temperature > 20:
        print("Fa caldo")
    elif temperature > 10:
        print("Temperato")
    else:
        print("Fa freddo")



if __name__ == "__main__":
    main()
