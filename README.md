# Imgur URLS
[![license MIT License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/KurzGedanke/Imgur-URL/blob/master/LICENSE)
[![Python Version 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://github.com/KurzGedanke/Imgur-URL)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/KurzGedanke)

A Python script which gives out an array of the images url of an imgur link.

Album links and single image links are working! 

### How to use:
Enter: 

```bash
git clone https://github.com/KurzGedanke/Imgur-URL.git
```

in your Terminal and copy the `requirements.txt` and `imgur_url.py` to your project directory.
With your virtualenv enabled or not, run following command in your terminal:

```bash
pip install -r requirements.txt
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

### TODO:

- [x] single image links
- [x] album links
- [ ] gallery links
- [ ] pip install
- [ ] tests
- [ ] CI
