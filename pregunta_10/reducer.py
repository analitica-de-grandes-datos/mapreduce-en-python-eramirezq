#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    curkey=None
    lista=[]
    for line in sys.stdin:
        key,val=line.split()
        val=int(val)
        if key==curkey:
            lista.append(val)
        else:
            if curkey is None:
                curkey=key
                lista.append(val)
            else:
                l=','.join(map(str,lista))
                sys.stdout.write('{}\t{}\n'.format(curkey,l))
                lista.clear()
                curkey=key
                lista.append(val)
                
    l=','.join(map(str,lista))
    sys.stdout.write('{}\t{}\n'.format(curkey,l))
                
             