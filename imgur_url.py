import re
import os
import argparse
import requests


class ImgurURL:

    def __init__(self):
        self = self

    def get_imgur_urls(self, starturl):
        '''
        Scans which kind of imgur url the link is and used the correct
        function for returning it.
        '''
        albumRegEx = r"imgur.com\/a\/([\w\d]*)"
        galleryRegEx = r"imgur.com\/gallery\/([\w\d]*)"
        singleImageRegEx = r"imgur.com\/([\w\d]{7})"

        if re.search(albumRegEx, starturl.replace(' ', '')):
            return self.get_album_urls(starturl.replace(' ', ''))
        elif re.search(galleryRegEx, starturl.replace(' ', '')):
            return self.get_gallery_urls(starturl.replace(' ', ''))
        elif re.search(singleImageRegEx, starturl.replace(' ', '')):
            return self.get_single_image_url(starturl.replace(' ', ''))
        else:
            raise ValueError('Not an valid imgur link!')

    def get_blog_layout(self, starturl):
        '''
        Uses regualar expression to convert the input url to an /layout/blog
        url where all the hashes are within the html. Returns a string with
        url.
        '''

        regex = r"imgur.com\/a\/([\w\d]*)"
        urlhash = re.search(regex, starturl)
        try:
            return 'https://imgur.com/a/{0}/layout/blog'.format(urlhash.group(1))
        except:
            raise Exception('Album Link couldn\'t get converted')

    def get_album_urls(self, starturl):
        '''
        Uses regular expression to get the hashes and the format out of the
        json in the html and converts them into a working imgur url. Returns a
        arrays.
        '''
        finishedurl = []
        regex = r"\{\"hash\":\"([\w\d]*)\"\,\"title\".*?\"ext\"\:\"(\.jpg|.png|.gif|.gifv|.mp4)\".*?\}"
        try:
            imgurHTML = requests.get(self.get_blog_layout(starturl))
        except:
            raise Exception('Something failed with the download')
        imgurhashes = re.findall(regex, imgurHTML.text)

        # fixes a bug with a single image album where it outputs the same links twice
        if imgurhashes[0] == imgurhashes[1]:
            finishedurl.append('https://i.imgur.com/{0}{1}'.format(imgurhashes[0][0],
                                                                   imgurhashes[0][1]))
        else:
            for hashes in imgurhashes:
                finishedurl.append('https://i.imgur.com/{0}{1}'.format(hashes[0], hashes[1]))
        return finishedurl

    def get_gallery_urls(self, starturl):
        print('Gallery Links are not supported yet.')
        pass


    def get_single_image_url(self, starturl):
        finishedurl = []
        regex = r"href\=\"https://i\.imgur\.com\/([\d\w]*)(\.jpg|\.png|\.gif|\.mp4|\.gifv)"
        try:
            imgurHTML = requests.get(starturl)
        except:
            raise Exception('Something failed with the download')

        imgurhash = re.findall(regex, imgurHTML.text)
        finishedurl.append('https://i.imgur.com/{0}{1}'.format(imgurhash[0][0], imgurhash[0][1]))
        return finishedurl


def list_url(urlinput):
    imgururls = ImgurURL()
    urls = imgururls.get_imgur_urls(urlinput)

    for url in urls:
        print(url)


def download(urlinput):
    path = input('Please enter your desired path: ')
    imgururls = ImgurURL()
    urls = imgururls.get_imgur_urls(urlinput)
    hashAndEndigRegEx = r"i.imgur.com\/([\w\d]*)(\.jpg|\.gif|\.png|\.mp4|\.gifv)"
    print('Your Download starts: ')
    for url in urls:
        hashAndEnding = re.findall(hashAndEndigRegEx, url)
        print('{0}{1}{2}'.format(path, hashAndEnding[0][0], hashAndEnding[0][1]))
        with open('{0}{1}{2}'.format(path, hashAndEnding[0][0], hashAndEnding[0][1]), 'wb') as f:
            r = requests.get(url)
            f.write(r.content)
    print('Download finished!')

def main():

    parser = argparse.ArgumentParser(description='Lists or downloads Imgur links.')
    parser.add_argument('-list', metavar='ImgurLink', type=str,
                        help='Lists all links from the Album.')
    parser.add_argument('-download', metavar='ImgurLink', type=str,
                        help='Downloads all images from the album.')

    args = parser.parse_args()

    if args.list:
        list_url(args.list)
    elif args.download:
        download(args.download)
    else:
        raise Exception('Something went wrong.')


if __name__ == '__main__':
    main()


'''
Test URLS:
Album: https://imgur.com/a/3aeC1

SingleImage: https://imgur.com/URyijAU

Gallery: https://imgur.com/gallery/sQJ2h
'''