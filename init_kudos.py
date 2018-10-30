import os
import re
import json
import sys

import oyaml as yaml

fnames = [x for x in os.listdir('images') if x.endswith('.svg')]

names = []
for fname in fnames:
    name = ''.join([x.lower() for x in re.sub(r'\.svg$', '', fname)])
    names.append((name, fname))


if os.path.exists('kudos.yaml'):
    print('kudos.yaml file already exists.')
    ans = input('Do you want to re-initialize it. (y/N)?  ')
    if ans.lower() != 'y':
        sys.exit(1)

objs = []
for name in names:
    obj = dict(name=name[0],
               description='lorum',
               priceFinney=1,
               numClonesAllowed=10,
               tags='',
               image=name[1]
               )
    objs.append(obj)

with open('kudos.yaml', 'w') as f:
    f.write(yaml.dump(objs, default_flow_style=False))
