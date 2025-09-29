
cel = float(input("Введите температуру в цельсиях: "))

far = round((cel * 9/5) + 32, 2)
kel = round(cel + 273.15, 2)

print(f'{cel} C = {far} F')
print(f'{cel} C = {kel} K')
