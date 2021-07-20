# Anthony Velez
# Software - Tercer semestre

# TUPLAAS - LISTAS - DICCIONARIOS
usuario = ('jquijije','1234','jquijije2001@gmail.com')
materias = ['Python','PHP','POO','Go']
alumno = {'nombre':'Josue','edad':20,'fac':'faci'}
print(usuario[0],materias[1],alumno['nombre'])
print(usuario[0:2],alumno.keys(),alumno.values())
materias.append('Programacion Movil')
alumno['sexo'], alumno['edad']='M', 20
print(materias,alumno)
tupla,lista,diccionario=(),[],{}
# RECORRIDOS TUPLAS Y LISTAS CON "IN"
for valor in usuario: print(valor)
# RECORRIDOS LISTAS CON "ENUMERATE"
for i, c in enumerate(materias): print(i,':',c)
# RECORRIDOS DICCIONARIOS CON "ITEMS"
for c, v in alumno.items(): print(c,':',v)