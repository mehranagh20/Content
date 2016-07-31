import magic
import os
import sys

types = dict()

def content(fN, flag=False):
    if not os.path.exists(fN):
        print 'there is not path', fN
        exit(1)
    for files in os.listdir(fN):
        ff = os.path.join(fN, files)
        if os.path.isfile(ff):
            ext = magic.from_file(ff, mime=True)
            if not ext in types:
                l = [files, ]
                types[ext] = l
            else: types[ext].append(files)
        elif os.path.isdir(ff) and flag:
            content(ff)
    return types


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 5 or (len(sys.argv) == 3 and sys.argv[1] != '--r') or (
            len(sys.argv) == 4 and sys.argv[1].lower() != '--tofile') or (len(sys.argv) == 5 and (sys.argv[1] != '--r' or sys.argv[2].lower() != '--tofile')):
        print "usage: python content.py [--r (for recursively give content of nested folders.)] [--toFile fileName] folder-to-list-its-content"
        sys.exit(1)
    if len(sys.argv) == 4 or len(sys.argv) == 5:
        try:
            if(len(sys.argv) == 4): f = open(sys.argv[2], 'w')
            else: f = open(sys.argv[3], 'w')
        except IOError:
            print 'problem opening or creating', sys.argv[2]
            sys.exit(1)
        if len(sys.argv) == 4: lis = content(sys.argv[3])
        else: lis = content(sys.argv[4], True)
        for (fileT, fileNs) in sorted(lis.items()):
            f.write(fileT)
            f.write('\n')
            for fileN in fileNs:
                f.write('\t\t\t')
                f.write(fileN)
                f.write('\n')
            f.write('---------------------------------------------------------------\n\n')
    else:
        if len(sys.argv) == 2: lis = content(sys.argv[1])
        else: lis = content(sys.argv[2], True)
        for (fileT, fileNs) in sorted(lis.items()):
            print '\n', fileT, ":"
            for fileN in fileNs:
                print '\t\t\t', fileT
            print '\n---------------------------------------------------------------\n\n'


if __name__ == '__main__': main()
