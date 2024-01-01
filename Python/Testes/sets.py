# Set

# planeta_anao = {'Plutão': None,'Ceres': None, 'Eris': None,'Haumea': None, 'Makemake': None}
# print(len(planeta_anao))
# #print('Lua' in planeta_anao)

# # for astro in planeta_anao:
# #     print(f'\n{astro.upper()}')

# astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)
# planeta_anao['Ceres'] = 1
# print(type(planeta_anao))

astros1 = {'Lua', 'Venus','Sirius','Marte', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa de Halley'}

# print(astros1 & astros2)
# print(astros1.intersection(astros2))

# print(astros1 ^ astros2)

astros1.add('Urano')
astros1.add('Sol')
astros1.clear()
print(astros1)

