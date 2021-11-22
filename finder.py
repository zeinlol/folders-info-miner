from pathlib import Path

from core.arguments import cli_arguments
from core.engine import DisplayablePath
from core.output import write_data

target_folder = cli_arguments.path
blacklist = cli_arguments.blacklist
depth = cli_arguments.depth

if __name__ == '__main__':
    paths = DisplayablePath.make_tree(Path(target_folder))
    folders_dict = {}
    folders_list = ''
    for counter, folder in enumerate(paths):
        if cli_arguments.json:
            if counter == 0:
                folders_dict = folder.json_data()
            else:
                # folders_dict['items'] = folders_dict['items'].append(folder.parent.append_item(folder))
                folder.parent.append_item(folder)
        else:
            # print(target_folder.displayable())
            folders_list += f'{folder.displayable()}\n'

    output_data = folders_dict if cli_arguments.json else folders_list
    if cli_arguments.output:
        write_data(output_file=cli_arguments.output, data=output_data)
    else:
        print(output_data)
