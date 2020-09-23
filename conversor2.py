dollar = input("How many dollars do you have?:")
dollar = float(dollar)
peso_value = 21.06
peso = dollar * peso_value
peso = round(peso, 2)
peso = str(peso)

print("You have $" + peso + " pesos")