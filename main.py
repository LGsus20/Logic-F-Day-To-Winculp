import prepare_string

print("¿Cuántas variables desea introducir?")
quantity = int(input())

values = []
for number in range(quantity):
    print(f"Introduce la variable {number+1}:")
    values.append(input())


file = open('FdayToWinculp.txt', 'w')
for value in values:
    final_value = str(prepare_string.stringFormater(value))
    file.write(final_value + "\n")

file.close()
