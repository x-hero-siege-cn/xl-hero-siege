import os
import re

version = ''

with open('CHANGELOG.md', encoding='utf-8', mode='r') as f:
    first_line = f.readline()
    version = re.match(r'## v(.*)', first_line).group(1)

if not version:
    exit()

os.chdir('./releases')

map_fullname = f'XL_Hero_Siege_{version}.w3x'
original_mapname = 'SlkMap.w3x'

if os.path.exists(map_fullname):
    os.remove(map_fullname)

if os.path.exists(original_mapname):
    os.rename(original_mapname, map_fullname)


os.chdir('../table')

with open('w3i.ini', encoding='utf-8', mode='r') as f:
    w3i_ini = f.readlines()

w3i_ini[4] = '地图名称 = "XL Hero Siege v{version}"\n'.format(version=version)

with open('w3i.ini', encoding='utf-8', mode='w') as f:
    f.writelines(w3i_ini)
