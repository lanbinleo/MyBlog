import os

# 获取当前文件夹下的所有子文件夹（不包括特定的文件夹）
excluded_folders = ['node_modules', '.git', '.vscode', '.idea']

def list_subfolders(folder):
    subfolders = []
    for f in os.scandir(folder):
        if f.is_dir() and f.name not in excluded_folders:
            subfolders.append(f.path)
            subfolders.extend(list_subfolders(f.path))
    return subfolders

def list_files(folder):
    files = []
    for f in os.scandir(folder):
        if f.is_file():
            files.append(f.path)
    return files

# 获取当前文件夹下的所有子文件夹（不包括特定的文件夹）
subfolders = list_subfolders('.')

# 将结果写入 hot_load.txt 文件
with open('hot_load.txt', 'w') as file:
    for folder in subfolders:
        file.write(folder + '\n')
        files = list_files(folder)
        for file_path in files:
            file.write(file_path + '\n')

print("子文件夹列表及其文件已写入 hot_load.txt 文件中。")
