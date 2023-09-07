from pprint import pprint
import glob
import gzip
import pandas as pd 
import gzip
from io import StringIO
from base64 import b64decode

 
def decompress():
    users_acces =[] 
    n=0
    gz_files = glob.glob("log/*")
    for infile in gz_files:
        print('in ',infile)
        with open(infile, encoding='ISO-8859-1') as lo:
            f = lo.readlines()
        if infile.endswith('gz'):
            with gzip.open(infile, 'rb') as lo:
                f = lo.readlines()
            f = [l.decode() for l in f]
        for l in f:
            n = n+1
            if ('Server' in l )and ('is ready' in l):
               print(l)
               s=l.split(']')
               users_acces.append({'user':s[2].split(' ')[2].split('@')[0],'date':s[1].split(' ')[2],'time':s[1].split(' ')[3]})
     

 

    
    df = pd.DataFrame.from_dict(users_acces)
    df.to_csv('C:/Users/etuejor/OneDrive - Ericsson/Metrics/logins.csv',sep=',',index=False)
 
    return df

 

 

if __name__ == '__main__':

    decompress()
