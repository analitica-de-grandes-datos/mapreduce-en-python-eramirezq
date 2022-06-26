#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    
    for line in sys.stdin:
        key=line.split()[0]
        key=int(key)
        letters=line.split()[1]
        for letter in letters.split(','):
            sys.stdout.write('{}\t{:03d}\n'.format(letter,key))
        
        