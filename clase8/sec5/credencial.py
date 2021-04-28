persona = ['Cristóbal',26,1.70,False,['Fight Club','Inception','Nightcrawler']]

print(f'Nombre: {persona[0]}')
print(f'Edad: {persona[1]}')
print(f'Estatura: {persona[2]}')
if persona[3]:
    print('En un relación')
else :
    print('Soltero')

print('Peliculas Fav:')
for i in persona[4]:
    print(f'- {i}')

print("......")

persona = ['Javier',28,1.75,True,['Forest Gump','Memento']]

print(f'Nombre: {persona[0]}')
print(f'Edad: {persona[1]}')
print(f'Estatura: {persona[2]}')
if persona[3]:
    print('En un relación')
else :
    print('Soltero')

print('Peliculas Fav:')
for i in persona[4]:
    print(f'- {i}')
    