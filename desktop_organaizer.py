import os
import shutil


def organizer_dekstop(folder_name, file_type):
    desktop_path = 'C:\\Users\\Warwick\\Desktop\\'
    files_to_move = [dekstop_file for dekstop_file in list(os.listdir(desktop_path)) if dekstop_file.lower().endswith(file_type)]
    print(list(os.listdir(desktop_path)))
    print(files_to_move)
    new_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    for file_name in files_to_move:

        if os.path.exists(os.path.join(new_path, file_name)):
            copy_text = '_copy'
            first_part_name, last_part_name = os.path.splitext(file_name)
            new_file_name = os.path.join(new_path, first_part_name + copy_text + last_part_name)
            shutil.move(desktop_path + file_name, new_file_name)

        else:
            shutil.move(desktop_path + file_name, os.path.join(new_path, file_name))



organizer_dekstop('Desktop_Text', '.pdf')