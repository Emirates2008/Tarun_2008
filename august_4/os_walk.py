import os
k=os.walk('C:\\Users\\Tarun\\Desktop\\testing')
for (root,dirs,files) in k:
    print(root)
    print(dirs)
    print(files)
