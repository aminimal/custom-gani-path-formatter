import pathlib

# store path objects for gani files in list
path = pathlib.Path('Assets')
gen = path.rglob('*.gani')
list = list(gen)

# lists of lines for each type
gani_stems = []
gani_lines = []
gani_lines_xml = []
gani_lines_lua_motions = []
gani_lines_lua_motiongroups = []

# iterate through each gani file and generate lines
for i, item in enumerate(list):
    itemid = "CGPF" + f"{i:04}"
    posix = item.as_posix()
    stem = pathlib.Path(item).stem.split('.')[0]
    gani_lines.append('/' + posix[:-5])
    gani_lines_xml.append('<Gani FilePath=\"' + '/' + posix[:-5] + '\" />')
    gani_lines_lua_motions.append(itemid + '={\"' + '/' + posix + '\"},')
    gani_lines_lua_motiongroups.append('\"' + itemid + '\",')

# generate files for each type
with open(f'{gani_lines=}'.split('=')[0] + '.txt', 'w') as file:
    lines = gani_lines
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

with open(f'{gani_lines_xml=}'.split('=')[0] + '.txt', 'w') as file:
    lines = gani_lines_xml
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

with open(f'{gani_lines_lua_motions=}'.split('=')[0] + '.txt', 'w') as file:
    lines = gani_lines_lua_motions
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

with open(f'{gani_lines_lua_motiongroups=}'.split('=')[0] + '.txt', 'w') as file:
    lines = gani_lines_lua_motiongroups
    cnt = len(lines)
    for i, line in enumerate(lines):
        if not i == cnt - 1:
            file.write(line + '\n')
        else:
            file.write(line)

# end