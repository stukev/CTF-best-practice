import zipfile, re, os
zfile = "./zipception.zip"
zfolder = "."
def extract(zfile, zfolder):
    with zipfile.ZipFile(zfile, 'r') as ifile:
        ifile.extractall(path=zfolder)
    os.remove(zfile)
    for root, dirs, files in os.walk(zfolder):
        for filename in files:
            if re.search(r'\.zip$', filename):
                fileSpec = os.path.join(root, filename)
                extract(fileSpec, root)


extract(zfile, zfolder)
