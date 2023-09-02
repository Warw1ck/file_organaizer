import os
import shutil


def organizer_dekstop(folder_name, *file_types):
    print(folder_name)
    print(file_types)
    desktop_path = 'C:\\Users\\Warwick\\Desktop\\'
    files_to_move = [dekstop_file for dekstop_file in list(os.listdir(desktop_path)) if os.path.splitext(dekstop_file)[1] in file_types]
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



