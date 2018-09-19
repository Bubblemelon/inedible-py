# Note on build command:
#
# This build works with ubuntu:latest as well, un-comment it in the Dockerfile and,
# change the tag of this build as you wish.
#
docker build -t debian-python-x11 . 

# Notes on run command:
# 
# docker run -it --rm -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <image-name> <container-command> <options> <args>
#
# (1) May not need the "unix" keyword as part of "...unix$DISPLAY"
#
# (2) May need to run `$ xhost +` before executing this script and then place the restrictions again by running `$ xhost -` after container exits

docker run -it --rm -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix debian-python-x11 python3 -m pygame.examples.aliens

