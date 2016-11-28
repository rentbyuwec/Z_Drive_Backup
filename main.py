import os
import shutil


def get_folder_names(parent):
    return [d for d in os.listdir(parent)]


def remove_blacklisted(blacklist, folder_list):
    return [x for x in folder_list if x not in blacklist]


def copy_to_google_drive(z_drive_path, google_drive_path, folder_name):
    from_path = os.path.join(z_drive_path, folder_name)
    to_path = os.path.join(google_drive_path, folder_name)

    print("Begin copying folder/file from Z Drive: " + folder_name)

    if os.path.exists(to_path):
        print("Folder/file already exists, overwriting")
        if os.path.isdir(to_path):
            shutil.rmtree(to_path)
        if os.path.isfile(to_path):
            os.remove(to_path)

    if os.path.isfile(from_path):
        shutil.copy2(from_path, to_path)
    else:
        shutil.copytree(from_path, to_path)

    print("Done copying folder/file: " + folder_name + "\n")


if __name__ == "__main__":
    z_drive = os.path.abspath(r"\\ANITA-DESKTOP\Users\Anita Desktop\Z Drive")
    google_drive = os.path.abspath(r"C:\Users\Mike - CCAH\Google Drive\Z Drive Backup")

    blacklist = ["Certified Landlord Class", "Chase' Working Files", "EC plan commission", "J Drive", "Old Misc Files",
                 "OSHA Training Video", "Pictures Drive.lnk"]

    print "Source folder: " + z_drive
    print "Destincation folder: " + google_drive + "\n"

    for folder in remove_blacklisted(blacklist, get_folder_names(z_drive)):
        copy_to_google_drive(z_drive, google_drive, folder)
