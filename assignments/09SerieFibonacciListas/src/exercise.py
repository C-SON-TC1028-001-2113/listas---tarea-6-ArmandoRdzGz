def main():
    fibonacci = [0,1]
    lista = []
    a = [0]
    b = -1
    
    while b<0:
        b = int(input(''))
        if b == 0:
            print (lista)
        elif b>0:
            if b ==1:
                print (a)
            elif b==2:
                print (fibonacci)
            elif b>2:
                for x in range (b-2):
                    fibonacci.append(fibonacci[x]+fibonacci[x+1])
                print (fibonacci)    
    pass

if __name__=='__main__':
    main()
