# Guam-CRB-damage-map-2020-10

The online interactive map is available at https://aubreymoore.github.io/Guam-CRB-damage-map-2020-10/.

## Note on Videos

The videos used as raw data for generating the damage map are stored using the GitHub LFS (large File Storage) facility
because they are very large (greater than 1 GB in most cases).

When you clone this repo, LFS files will be replaced with pointers. For example videos/20201001_092426.mp4 will not contain a video file, but a pointer to the actual file on GitHub (only 135 bytes). If you really need to work with the video files, you will need install [Git LFS](https://git-lfs.github.com/).

To see which files are stored in LFS:
    git lfs ls-files

    git lfs pull --include '20201001_092426.mp4'
