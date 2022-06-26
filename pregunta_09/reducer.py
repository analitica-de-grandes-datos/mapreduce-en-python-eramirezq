#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    cont=0
    for line in sys.stdin:
        cont+=1
        val,letter,date=line.split()
        val=int(val)
        sys.stdout.write('{}   {}   {}\n'.format(letter,date,val))
        if cont==6:
            break