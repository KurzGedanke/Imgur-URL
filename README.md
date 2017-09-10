# Imgur URLS
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/KurzGedanke)

A Python script which gives out an array of the images url of an imgur link.

Album links and single image links are working! 

### How to use:
Import the script in your document.

```python
import imgur_url
```

Then assign the `ImgurURL()` class to your desired variable and call the `get_imgur_urls` function.

```python
url = imgur_url.ImgurURL()

print(url.get_imgur_urls('imgur.com/a/$HASH'))
```
**`.get_imgur_urls()` returns always and array!** 

### TODO:

- [x] single image links
- [x] album links
- [ ] gallery links
- [ ] pip install
- [ ] tests
- [ ] CI
