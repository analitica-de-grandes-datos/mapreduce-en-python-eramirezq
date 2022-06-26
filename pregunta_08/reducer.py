#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import statistics

if __name__ == "__main__":
    
    curkey=None
    total=0
    cont=0
    prom=0
    
    
    for line in sys.stdin:
        key, val = line.split('\t')
        val=int(val)
        
        
        if key == curkey:
            total += val
            cont +=1
        else:
            if curkey is None:
                curkey=key
                total = val
                cont +=1
                
            else:
                prom=total/cont
                sys.stdout.write('{}\t{:.1f}\t{}\n'.format(curkey,total,prom))
                curkey=key
                total=val
                cont=1
    prom=total/cont            
    sys.stdout.write('{}\t{:.1f}\t{}\n'.format(curkey,total,prom))