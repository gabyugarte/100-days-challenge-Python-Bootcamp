
from prettytable import PrettyTable

table = PrettyTable()
another_table = PrettyTable()

table.field_names = ['name', 'value', 'type']
table.add_row(['Gaby', 'Ugarte', 'Electric'])
table.add_row(['Jhonatan', 'Suncion', 'Electric'])

another_table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
another_table.add_column('Type', ['Electric', 'Winter', 'Fire'])
print(table)
another_table.align = "l"
# another_table.border = False
print(another_table)

