#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
       num=line.split(',')[1] 
       word=line.split(',')[0]
       num=int(num) 
       sys.stdout.write('{}\t'.format(num)+'{}\n'.format(word))
        