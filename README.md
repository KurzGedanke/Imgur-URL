# Imgur URLS
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/KurzGedanke)

A Python script which gives out an array of the images url of an imgur album.

**Important**: At the moments the script just works with imgur albums. Your url has to look like this: `https://imgur.com/a/$HASH`. Important here is the `/a/`.

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

### TODO:

- [ ] single image links
- [ ] gallery links
- [ ] pip install
- [ ] tests
- [ ] CI
