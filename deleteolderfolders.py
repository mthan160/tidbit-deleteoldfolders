import os
import sys
import datetime
import shutil
from os import DirEntry
from pathlib import Path

daystokeep = int(sys.argv[1])
target = sys.argv[2]

# Get list of x most recent days
folderstokeep = []
today = datetime.date.today()
for i in range(0, daystokeep):
    folderstokeep.append(today - datetime.timedelta(days=int(i)))

# List comprehension
folderstokeep = [str(item) for item in folderstokeep]
print(folderstokeep)

with os.scandir(target) as folderitems:
    for item in folderitems:
        if DirEntry.is_dir(item):
            if item.name in folderstokeep:
                print("Keeping!: "+item.name)
            else:
                try:
                    print("Deleting!: "+item.name+" continue?")

                    # Safety measure!
                    if str(Path(__file__).parent.resolve()) in str(Path(item.path).resolve()):
                        shutil.rmtree(item.path)
                        
                except OSError as e:
                    print("Error: %s : %s" % (dir_path, e.strerror))
