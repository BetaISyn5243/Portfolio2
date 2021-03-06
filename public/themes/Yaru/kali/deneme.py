import glob
import os

path = "./"
# search text files starting with the word "sales"
pattern = path + "kali" + "*.svg"

# List of the files that match the pattern
result = glob.glob(pattern)

# Iterating the list with the count
count = 1
for file_name in result:
    old_name = file_name
    new_name = path + 'kali_' + str(count) + ".svg"
    os.rename(old_name, new_name)
    count = count + 1

# printing all revenue txt files
res = glob.glob(path + "revenue" + "*.txt")
for name in res:
    print(name)