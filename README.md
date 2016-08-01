# Content

This script will return dict of all files with their corresponding fileTypes.

## Dependencies
* `python-magic`

To install dependencies, use `pip`:

```bash
$ pip install -r requirements.txt --upgrade
```

## Usage
*in python:

content function will return dict of all fileTypes with their corresponding files.
True flag will make content to treat nested folders like folderName and list all
their content too.

```
>>> import content

>>> dic = content(folderName, flag=False)
```
*in bash:

```
$ python content.py folderName --> prints files in folderName with their types on screen.

$ python content.py --toFile fileName folderName --> same as before but writes to fileName.
```

--r argument will list files in nested folders in folderName too.
example:

```
& python content.py --r --tofile fileName folderName
```

## License

[MIT](LICENSE)
