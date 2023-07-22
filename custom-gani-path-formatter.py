from sys import exit
import pathlib
from tkinter import filedialog
from tkinter import *

def exitOnEmptyVariable(x):
    if not x:
        exit()

# get input directory from user
selected_folder = filedialog.askdirectory(initialdir='/', title='Select the folder created by MtarTool (e.g. "custom_motions_mtar")')
exitOnEmptyVariable(selected_folder)
input_dir = pathlib.Path(selected_folder)
input_dir_name = input_dir.stem

# get output directory from user
selected_folder = filedialog.askdirectory(initialdir='/', title='Select the folder for storing the output files')
exitOnEmptyVariable(selected_folder)
output_dir = pathlib.Path(selected_folder)
output_dir_name = output_dir.stem

# create output file paths
of1_path = pathlib.PurePath.joinpath(output_dir, input_dir_name + '_mtar_dictionary.txt')
of2_path = pathlib.PurePath.joinpath(output_dir, input_dir_name + '_xml.txt')
of3_path = pathlib.PurePath.joinpath(output_dir, input_dir_name + '_lua_motion.txt')

# get list of gani from input_dir as root
gparts = []
for g in input_dir.rglob('*.gani'):
        leading_characters = g.stem[:4]
        char5 = g.stem[4]
        if leading_characters.isnumeric and char5 == '_':
            xtuple = g.relative_to(input_dir).parts
            xlist = list(xtuple)
            xlist[-1] = xlist[-1][5:]
            ytuple = tuple(xlist)
            gparts.append(ytuple)
        else:
            gparts.append(g.relative_to(input_dir).parts)
exitOnEmptyVariable(gparts)

# generate generic path list
paths_invalid = []
plist = []
for g in gparts:
    leng = len(g)
    if leng < 3:
        paths_invalid.append('/' + '/'.join(g))
    else:
        plist.append('/' + '/'.join(g))

# generate lines for mtar dictionary and mtar .xml
paths_mtar_dict = []
paths_mtar_xml = []
for p in plist:
    paths_mtar_dict.append(p.replace('.gani', ''))
    paths_mtar_xml.append('<Gani FilePath=\"' + p.replace('.gani', '') + '\" />')

# generate lines for lua
paths_lua_motions = []
for i, p in enumerate(plist):
    mgid = "MOTION" + f"{i:04}"
    paths_lua_motions.append(mgid + '={\"' + str(p) + '\"},')

# generate files
with open(of1_path, 'w') as file:
    lines = paths_mtar_dict
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

with open(of2_path, 'w') as file:
    lines = paths_mtar_xml
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

with open(of3_path, 'w') as file:
    lines = paths_lua_motions
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)