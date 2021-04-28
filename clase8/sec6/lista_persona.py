persona = ['Cristóbal Ugarte',26,1.70,False,['Fight Club','Inception','Nightcrawler']]

print(f'Nombre {persona[0]}')
print(f'Edad {persona[1]}')
print(f'Estatura {persona[2]}')

if  persona[3]:
    print('En una relación')
else:
    print('Soltero')

print('Peliculas Favoritas: ')
for i in persona[4]:
    print(i)
    

