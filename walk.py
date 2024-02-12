import os
import sys
print(os.walk("/home/ubuntu"))
print("files,directories are")
for root,dire,files in os.walk("/home/ubuntu"):
    #print(root,dire,files
    #    sys.exit(0)
    for file in files:
        if file.lower().endswith(".py"):
             print(file)
