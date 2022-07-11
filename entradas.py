#forma de ingresar info


from curses import intrflush


a=input('Hola, me podrías decir tu nombre?')
print(f'entiendo, tu nombre es {a}')

b=int(input('Cuantos años tienes?'))
print(f'entiendo, tu edad es {b+2}')