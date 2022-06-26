#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columnas=line.split(',')
        sys.stdout.write('{}\t{}\n'.format(columnas[3],columnas[4]))
