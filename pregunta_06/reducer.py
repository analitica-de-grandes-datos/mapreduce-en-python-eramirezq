#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    curkey=None
    max=0
    min=0
    
    for line in sys.stdin:
        key, val = line.split('\t')
        val=float(val)
        
        if key==curkey: 
            if val>max:
                max=val
            if val<min:
                min=val
        else:
            if curkey is None:
                curkey=key
                max=val
                min=val
            else:
                sys.stdout.write('{}\t{}\t{}\n'.format(curkey,max,min))
                curkey=key
                max=val
                min=val
                    
    sys.stdout.write('{}\t{}\t{}\n'.format(curkey,max,min))