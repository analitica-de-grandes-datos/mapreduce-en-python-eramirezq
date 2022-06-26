#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        letter,val,date=line.split()
        val=int(val)
        sys.stdout.write('{}   {}   {}\n'.format(letter,date,val))