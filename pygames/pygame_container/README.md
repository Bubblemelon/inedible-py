## Using Docker in Pygame Development

This configuration will allow Pygames GUI(s) to work from a Docker Container using the host machine's X11 session.

### Pull from [Docker Hub](https://cloud.docker.com/repository/docker/bubblemelon/pygame-x11):

```bash
docker pull bubblemelon/pygame-x11
```

To build from scratch see the sections that follow.

### How to Run:

Run `./docker-build_run.sh` to build the image and run a container of that image, this will launch one of Pygame's example games.

This build could also work with the `debian:jessie-slim` image, remove the ubuntu image in the `Dockerfile` if desired. There are some more notes in the `Dockerfile`.

### To reuse the image from the above script, run:

`# docker run -it --rm -e DISPLAY=unix$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <image-name> <container-command> <options> <args>`

### Notes on `docker-build+run.sh`:

> This image is set to build with `ubuntu:latest`, i.e. currently [Ubuntu 18.04 LTS Bionic](https://packages.ubuntu.com/bionic/).
>
> **Before executing this script**:
>
> (1) May not need the "unix" keyword as part of "...unix$DISPLAY".
>
> (2) May need to run `xhost +` on the host machine and then place the restrictions back again by running `$ xhost -` after container exits.

This error may occur if `xhost +` was not executed:

```bash
Traceback (most recent call last):
  File "/usr/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/usr/local/lib/python3.6/dist-packages/pygame/examples/aliens.py", line 321, in <module>
    if __name__ == '__main__': main()
  File "/usr/local/lib/python3.6/dist-packages/pygame/examples/aliens.py", line 188, in main
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
pygame.error: video system not initialized
```
The following statement is returned if executing `xhost +` was successful, `access control disabled, clients can connect from any host`.

The above notes can also be found in `docker-build+run.sh` but are worded differently.

### Expected errors:

Some expected errors will show when lauching one of Pygame's examples, but will work nonetheless.

See [Expected-Errors.md](/Docker_Container/Expected-Errors.md).
