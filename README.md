# Custom Gani Path Formatter

Assists with the creation of custom motions mods for MGSV:TPP by generating lines of code for each .gani file found in a directory tree <ins>in bulk</ins> ready to paste directly into related dictionaries and scripts.

## Context

This tool was created to assist those following [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/) or using a similiar process to create a custom motions mod for IH. After unpacking a .mtar file with MtarTool and placing the desired motion files inside, <ins>before</ins> repacking with MtarTool, use this program to generate the lines of code needed to tell MtarTool what files to look for. Afterwards, more lines of code can be added to the IH AddMotions module for accessing with the IH menu in-game or using other lua scripts.

## Examples

For each .gani file found, this program will output multiple lines of code. Examples can be seen below:

| Example Output                                                 | Related File            | Related Tool                |
|----------------------------------------------------------------|-------------------------|-----------------------------|
| /Assets/tpp/foldername/filename.gani                           | mtar_dictionary.txt     | MtarTool                    |
| <pre><Gani FilePath="/Assets/tpp/foldername/filename" /></pre> | filename_mtar.xml       | MtarTool                    |
| MOTION0000={"/Assets/tpp/foldername/filename.gani"},           | IHDev_AddMotions.lua    | Infinite Heaven (IH) module |

## Installation

- Put the program wherever you want! It allows the working folders to be selected via gui.

## Instructions

1. Run the program. (After all the .gani files are in place.)
2. Select the folder that was extracted using MtarTool. (e.g. "custom_motions_mtar" or "player2_resident_mtar")
3. Select the folder where the output files will be generated.
4. Copy/paste generated lines of code from the output files to the related scripts.

## Specifics

- This is a simple Python script compiled into an .exe using PyInstaller.
- The program runs a recursive search for gani files from the selected directory and reformats their paths as strings ready to be placed in scripts.
- The generated files are just .txt files you can copy/paste from. This does not automatically update any files anywhere.
- In the generated lines of lua code, each gani is placed in it's own motion group with a generated id unrelated to any prepended id generated by the MtarTool.
- Grouping motions or specifying their order will have to be done manually in the lua file.
- The reference to the fpk in the IH lua will still need to be entered manually. (This program has nothing to do with fpk files.)

### Disclaimer

This is not a custom motions modding tutorial. If you're looking for one try [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/).

## Considerations

- To use this tool properly, one should have a basic understanding of custom motions modding. Please refer to [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/) by choc for more information about this process.
- It is not required for file folders to be named exactly as they are in the guide. This can be used for unpacked .mtars of any name including original files, not just those provided in the motions-template from the guide mentioned above.
- This tool works best for animations which have only one .gani as opposed to the more complex animations which may have a beginning, middle, and end .gani file for each motion respectively. Though, it will still work for this situation, but each .gani will be put into it's own motion group in the .txt file. These would still be accessible in the IH menu, but might take a while to sift through. This can be changed manually for now.
- The motion and motionGroups are named automatically to an automatic, arbitrary id such as "CGPF0001". These can be renamed manually if desired.

## Thank Yous

- choc for a great guide on custom motions modding
- kapuragu for answering a bunch of unrelated questions about various things

## License

[MIT](https://choosealicense.com/licenses/mit/)
