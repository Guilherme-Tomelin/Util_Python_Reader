import os
import datetime

def write_py_files_to_txt(project_dir, ignore_files_list=None):
    if ignore_files_list is None:
        ignore_files_list = []

    def get_timestamp():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    project_name = os.path.basename(os.path.normpath(project_dir))
    txt_filename = f"{project_name}_{get_timestamp()}.txt"

    ignore_dirs = {".venv", ".idea", "__pycache__"}

    def process_directory(directory):
        with open(txt_filename, "w", encoding="utf-8") as txt_file:
            for root, dirs, files in os.walk(directory):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]

                for file in files:
                    if file.endswith(".py") and file not in ignore_files_list:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, start=project_dir)
                        txt_file.write(f"{relative_path}\n")
                        with open(file_path, "r", encoding="utf-8") as py_file:
                            txt_file.write(py_file.read())
                        txt_file.write("\n" + "-"*65 + "\n")

    process_directory(project_dir)

project_directory = r"C:\Users\.."
ignore_files_list = []

write_py_files_to_txt(project_directory, ignore_files_list)
