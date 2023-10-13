import functions


def main():
    print("¿Cuántas variables desea introducir?")
    quantity = int(input())

    values = []
    for number in range(quantity):
        print(f"Introduce la variable {number + 1}:")
        values.append(input())

    functions.create_file(values)


if __name__ == '__main__':
    main()
