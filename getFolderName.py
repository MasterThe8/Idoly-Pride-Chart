import os

def get_folder_names(path):
    # Membuat list kosong untuk menyimpan nama folder
    folder_names = []

    # Iterasi melalui setiap item di dalam path
    for item in os.listdir(path):
        # Memeriksa apakah item adalah folder
        if os.path.isdir(os.path.join(path, item)):
            # Menambahkan nama folder ke dalam list
            folder_names.append(item)

    return folder_names

# Contoh penggunaan
path = "D:\Chart\song\!DOLY PRIDE Pack\!Part1\!VideoBackground"
folder_names = get_folder_names(path)
for folder_name in folder_names:
    print(folder_name)