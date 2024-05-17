taxa_euro = 5.56
taxa_iene = 30.34

value_real =  float(input('Type the value in real  R$:'))

converted_euro = f'{value_real / taxa_euro:.2f}'
converted_iene = f'{value_real * taxa_iene:.2f}'

print(f'Euro: {converted_euro} | Iene: {converted_iene}')