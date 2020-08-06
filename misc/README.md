## Miscellaneous Python Programs

### [BinaryAsker](misc/BinaryAsker/BinaryAsker.py)
> This program tests the user's knowledge on binary numbers. It will ask for a range of decimal numbers that the program will ask the user to calculate/guess the conversion to binary.
> The user's time taken to answer is displayed after each attempt. The shortest time taken is shown before the program terminates.
> The input does not need to be padded with zeros e.g. the binary of `3` can be `0011` or `11`.

![BinaryAsker demo gif.](misc/BinaryAsker/BinaryAsker_demo.gif)

### [FoliumMapGenerator](misc/FoliumMapGenerator/FMG.py)

> This program takes a data file i.e. [`/data/customers.txt`](/FoliumMapGenerator/data/customers.txt) and generates a html file to display a map containing markers using coordinates from the data file via the [Folium](https://python-visualization.github.io/folium/) library.

![Folium map demo gif.](/misc/img/folium-map-demo.gif)

### [os-env](misc/os-env/get-env-vars.py)

> This directory contains scripts that show examples on how to retrive environment variables using the module method defined in `settings.py`, or from the `.env` file and from [exported variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps) via the [python-dotenv](https://github.com/theskumar/python-dotenv) library,


### [ThumnailGenerator](misc/ThumbnailGenerator.py)

> This program takes image files ( >= 1) and resizes it to `128x128`. If the image file is already equal or smaller that this dimension in both width and height then there will be no changes to that image file. See the difference between `Image.resize` and `Image.thumbnail` [here](https://stackoverflow.com/questions/29367990/what-is-the-difference-between-image-resize-and-image-thumbnail-in-pillow-python). The generated thumbnail image is saved in its original format if the extension is supported otherwise it will be saved in `jpeg`. Thumbnails will have `*_thumbnail.*` as its file name and saved in the same directory as the original.

Original:

![Puppy image.](/misc/img/puppy.jpg)

Thumbnail:

![Puppy thumbnail.](/misc/img/puppy_thumbnail.jpeg)