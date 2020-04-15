import os
import re

def main():
    Root = r'Demo'
    fileName = 'sample.htm'
    myFile = os.path.join(Root, fileName)

    with open(myFile, "rt") as f:
        text = f.read()
        f.close()
        # Get the document content
        body = re.findall(r'<body.+</body>', text, re.DOTALL)
        if len(body) == 0:
            print('Empty doc - there is no body tag!')
            return
        body = re.split('\n', body[0], maxsplit=1)
        headNbody = text.split(body[0])
        body = re.sub(r'</body>', '', body[1])
        tail = text.split(r'</body>')[-1]
        # Get Root folder dirs list
        patternFoldy = fileName.rstrip('.htm').rstrip('.html') + r'_files/'
        tempBody = ''
        dirs = os.listdir(Root)
        for d in dirs:
            if d == patternFoldy.rstrip('/'):
                continue
            tempBody = tempBody + re.sub(patternFoldy, d + '\\\\Output\\\\', body) + '\n\n'
        text2 = headNbody[0] + tempBody + tail  # re.sub(body, tempBody, text)
        outName = os.path.split(Root)[-1] + '.htm'
        fullOut = os.path.join(Root, outName)
        with open(fullOut, "wt") as fO:
            fO.write(text2)
            fO.close()


if __name__ == "__main__":
    main()