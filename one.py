

f = open("text.txt","r")

for line in f:

    for x in line:
        if x=='+':
            n1, n2 = line.split('+')
            k = int(n1)+ int(n2)
            print(k)
        elif x== '-':
            n1, n2 = line.split('-')
            k=int(n1) - int(n2)
            print(k)
        elif x== '*':
            n1, n2 = line.split('*')
            k= int(n1)*int(n2)
            print(k)
        elif x== '/':
            n1, n2 = line.split('/')

            if(int(n2) ==0):
                print("not defined")

            else: print(int(n1)/ int(n2))



f.close()
