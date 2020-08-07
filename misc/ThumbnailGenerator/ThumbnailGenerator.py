import os, sys
from PIL import Image

# size of thumbnail
size = (128, 128)

# param can be more than 1 image path
for infile in sys.argv[1:]:

    # does a reverse search for '.' and returns the left & right of '.'
    # https://docs.python.org/2/library/os.path.html#os.path.splitext
    # os.path.splitext(infile)[0] == outfile path w/o extension
    outfile, ext = os.path.splitext(infile)

    if infile != outfile:
        try:
            img = Image.open(infile)
            img.thumbnail(size, Image.ANTIALIAS)

            # takes the original filename extension
            # i.e. ext[1:] removes "." from e.g. ".jpeg"
            # supported formats: https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html#id3
            if ext[1:] != 'jpg':
                img.save(outfile + "_thumbnail." + ext[1:] , ext[1:])
            else:
                img.save(outfile + "_thumbnail.jpeg", 'jpeg')

        except IOError as e:
            print ("ERROR: Unable to create thumbnail !")
            print ("ERROR:", e)
