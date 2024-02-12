import os
print(os.walk("/home/ubuntu"))
for root,dir,files in os.walk("/home/ubuntu"):
    for file in files:
        if file.startswith("noticefile") or file.startswith("license"):
            os.chdir(root)
            with open(file,"r") as fh:
                content=fh.read()
            with open("/home/ubuntu/notice.txt","a") as df:
                df.write(f"{file}\n")
                df.write(f"{root}\n{content}")


