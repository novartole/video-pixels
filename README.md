# Video-pixels
The scripts allow to apply a custom algorithm to an mp4 video clip. For now, only one algorithm is available:
- Random mix (every group of pixels mixes randomly)

## Settings
Several main script parameters can be changed in the file `$bin/config.ini`:
* `FramesDirName` &ndash; name of the permanently stored frames (this behavior can be changed by providing a special parameter, but just put *--help* while the script is calling for more information)
* `ImageExtention` &ndash; image extension that is used to store frames (*jpg* by default)

Algorithms may have their own configurations (see `$algorithms/config.ini`)
Random mix:
* `Width` &ndash; width of pixel group to process at each step
* `Hight` &ndash; hight of pixel group to process at each step

## License
MIT
