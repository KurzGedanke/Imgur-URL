# Imgur URLS
[![license MIT License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/KurzGedanke/Imgur-URL/blob/master/LICENSE)
[![Python Version 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://github.com/KurzGedanke/Imgur-URL)
[![Say Thanks!](https://img.shields.io/badge/Donate%20Bitcoin-💵-lightgrey.svg)](https://kurzgedanke.de/donate/)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-🐿️-1EAEDB.svg)](https://saythanks.io/to/KurzGedanke)

A Python script which gives out an array of the images url of an imgur link.

Album links and single image links are working! 

## How to use the Command Line Tool: 

Donwload or clone this repository:

```bash
$ git clone https://github.com/KurzGedanke/Imgur-URL.git
```
Change the directory to the `Imgur-URL` dir and install the requirements.

```bash
$ cd Imgur-URL
$ pip install -r requirements.txt
```

Run the file with the `-h` flag for help:

```bash
$ python imgur_url.py -h
usage: imgur_url.py [-h] [-list ImgurLink] [-download ImgurLink]

List or Download Imgur Links

optional arguments:
  -h, --help           show this help message and exit
  -list ImgurLink      List all links from the Album.
  -download ImgurLink  Downloads all images from the album.
```

With the `-list` flag it prints out the whole list of urls and with the `-download` flag its downloading all images into
a folder of your choice. For example:

```bash
$ python imgur_url.py -download https://imgur.com/a/3aeC1
Please enter your desired path:
$ /Users/lucius/Desktop/newFolder
Your Download starts:
/Users/lucius/Desktop/newFolder/ITKdVe8.png
/Users/lucius/Desktop/newFolder/TBkr4BC.png
/Users/lucius/Desktop/newFolder/vZjTwWQ.png
/Users/lucius/Desktop/newFolder/2c1NIP2.png
/Users/lucius/Desktop/newFolder/ITKdVe8.png
/Users/lucius/Desktop/newFolder/TBkr4BC.png
/Users/lucius/Desktop/newFolder/vZjTwWQ.png
/Users/lucius/Desktop/newFolder/2c1NIP2.png
Download finished!
```

You have to enter a full path but a new folder is created for you.
## How to use it in your own project:
Enter: 

```bash
$ git clone https://github.com/KurzGedanke/Imgur-URL.git
```

in your Terminal and copy the `requirements.txt` and `imgur_url.py` to your project directory.
With your virtualenv enabled or not, run following command in your terminal:

```bash
$ pip install -r requirements.txt
```

Now import the script in your python file. 

```python
import imgur_url
```

Then assign the `ImgurURL()` class to your desired variable and call the `get_imgur_urls` function.

```python
url = imgur_url.ImgurURL()

print(url.get_imgur_urls('imgur.com/a/$HASH'))
```
**`.get_imgur_urls()` returns always an array!** 

## TODO:

- [x] single image links
- [x] album links
- [x] downloading files as Command Line Tool
- [x] path normalisation for downloading
- [ ] gallery links
- [ ] pip install
- [ ] tests
- [ ] CI
