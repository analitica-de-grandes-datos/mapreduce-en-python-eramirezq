#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    
    for line in sys.stdin:
        val,key=line.split()
        sys.stdout.write('{},{}\n'.format(key,val))
        