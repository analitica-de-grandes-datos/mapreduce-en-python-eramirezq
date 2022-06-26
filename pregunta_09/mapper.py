#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    def agregar_ceros_tres_digitos(valor):
        return f'{valor:03d}'
    
    for line in sys.stdin:
        letter,date,val=line.split()
        val=int(val)
        val=agregar_ceros_tres_digitos(val)
        sys.stdout.write('{}\t{}\t{}\n'.format(val,letter,date))