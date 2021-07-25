# OH Soldier , Prettify my Folder

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1


print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to - Oh Soldier Pretiffy My Folder")



soldier(r"C:\Users\Admin\Desktop\test_exercise8" , r"C:\Users\Admin\Desktop\test_exercise8\does.txt" , ".png")


