
def main():
    filas=int(input(''))
    columnas=int(input(''))
    
    a=filas*columnas
    i=0
    lista=[]

    while i<a:
        i=i+1
        datos=int(input(''))
        if datos<10:
            lista.append(datos)
    print(lista)



if __name__=='__main__':
    main()
