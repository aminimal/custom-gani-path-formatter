# Custom Gani Path Formatter

Generates .txt files of paths for each .gani inside an unpacked .mtar in various formats to assist with building a custom motions mod for MGSV:TPP.

## Assumptions

This tool was created for those following [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/) or making their own custom motions mod with a basic understanding of the process. This is also under the assumption that the user's end goal is a custom motions mod for use with IH.

## Installation

Place the .exe into any unpacked .mtar folder and execute to generate .txt files.

## Specifics

This is a simple Python script compiled into an .exe using PyInstaller. The script looks for a folder named "Asset" in the current directory and then recursively searches that directory for .gani files. Then .txt files are generated which contain lists to the .gani files each formatted to make for easy copy/paste to other files. (The .mtar must be unpacked.)

### Visual Aid

| Generated File                  | Destination File        | Post-execution Action                                                                                    |
|---------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------|
| gani_lines.txt                  | mtar_dictionary.txt     | Manually copy/paste from generated file to end of destination file without overwriting existing content. |
| gani_lines_xml.txt              | custom_motions.mtar.xml | Manually copy/paste from generated file to "Entries" section of destination file.                        |
| gani_lines_lua_motions.txt      | IHDev_AddMotions.lua    | Manually copy/paste from generated file to "this.motions" section destination file.                      |
| gani_lines_lua_motiongroups.txt | IHDev_AddMotions.lua    | Manually copy/paste from generated file to "this.motionGroups" section of destination file.              |

Note: This is not a custom motions modding tutorial. Please follow [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/) for further information on making custom motions mods.

## Considerations

- To use this tool properly, one should have a basic understanding of custom motions modding. Please refer to [this guide](https://chocmake.github.io/guides/mgsv-adding-player-motions/) by choc for more information about this process.
- It is not required for file folders to be named exactly as they are in the guide. This can be used for unpacked .mtars of any name including original files, not just those provided in the motions-template from the guide mentioned above.
- This tool works best for animations which have only one .gani as opposed to the more complex animations which may have a beginning, middle, and end .gani file for each motion respectively. Though, it will still work for this situation, but each .gani will be put into it's own motion group in the .txt file. These would still be accessible in the IH menu, but might take a while to sift through. This can be changed manually for now.
- The motion and motionGroups are named automatically to the name of the .gani file. These can be renamed manually if desired.

## Thank Yous

- choc
- kapuragu

## License

[MIT](https://choosealicense.com/licenses/mit/)
