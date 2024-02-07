from os import walk
import glob
import csv
dir_path = r"C:\Downloaded Web Sites\www.unomaha.edu\college-of-information-science-and-technology\**\*.*"

import re
# folder path
IS_and_t_links = []


for file in glob.glob(dir_path, recursive=True):
    IS_and_t_links.append(file)



for idx, ele in enumerate(IS_and_t_links):
    char = "C:\\Downloaded Web Sites\\"
    IS_and_t_links[idx] = ele.replace(char, '')
print(len(IS_and_t_links))
for i, j in enumerate(IS_and_t_links):
    char = ".html"
    IS_and_t_links[i] = j.replace(char, '')
print(len(IS_and_t_links))

# printing result
#print("The list after removal of character : " + str(IS_and_t_links))

pdf_list = []
pptx_list = []
jpeg_list=[]
png_list = []
url_list = []

for r in IS_and_t_links:
    if r.endswith(".php"):
        url_list.append(r)
        
        IS_and_t_links.remove(r)
  




print(len(pdf_list))



print(len(IS_and_t_links))
#print(url_list)

modified_list = [path.replace("\\", "//") for path in url_list]

print(modified_list)
modified_list = ["https://" + path for path in modified_list]

print(modified_list)

with open("URL.csv", "w",newline="") as myFile:
    header = ["URL"]
    write= csv.writer(myFile)
    
    write.writerow(url_list)