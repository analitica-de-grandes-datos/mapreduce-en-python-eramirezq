#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    curkey=None
    max=0
    
    for line in sys.stdin:
        key, val = line.split('\t')
        val=int(val)
        
        if key==curkey: 
            if val>max:
                max=val
        else:
            if curkey is None:
                curkey=key
                max=val
            else:
                sys.stdout.write('{}\t{}\n'.format(curkey,max))
                curkey=key
                max=val
                    
    sys.stdout.write('{}\t{}\n'.format(curkey,max))            
                
            

        
        