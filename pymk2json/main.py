import json

my_str='''
| Some Title | Some Description             | Some Number |
|------------|------------------------------|-------------|
| Dark Souls | This is a fun game           | 5           |
| Bloodborne | This one is even better      | 2           |
| Sekiro     | This one is also pretty good | 110101      |
'''

def mrkd2json(inp):
    lines = inp.split('\n')
    ret=[]
    keys=[]
    for i,l in enumerate(lines):
        if i==0:
            keys=[_i.strip() for _i in l.split('|')]
        elif i==1: continue
        else:
            ret.append({keys[_i]:v.strip() for _i,v in enumerate(l.split('|')) if  _i>0 and _i<len(keys)-1})
    return json.dumps(ret, indent = 4) 


if __name__ == "__main__":
    print(mrkd2json(my_str))