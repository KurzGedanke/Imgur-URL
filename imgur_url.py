import re
import requests

class ImgurURL:

    def __init__(self):
        self = self

    def get_blog_layout(self, starturl):
        '''
        Uses regualar expression to convert the input url to an /layout/blog url
        where all the hashes are within the html. Returns a stringt with url.
        '''

        regex = r"imgur.com\/a\/([\w\d]*)"
        urlhash = re.search(regex, starturl)
        try:
            return 'https://imgur.com/a/{0}/layout/blog'.format(urlhash.group(1))
        except:
            print('There was an error with link.')
            exit()

    def get_imgur_urls(self, starturl):
        '''
        Uses regular expression to get the hashes and the format out of the json in the html
        and converts them into a working imgur url. Returns a arrays.
        '''

        finishedurl = []
        regex = r"\{\"hash\":\"([\w\d]*)\"\,\"title\".*?\"ext\"\:\"(\.jpg|.png|.gif|.gifv|.mp4)\".*?\}"
        try:
            imgurHTML = requests.get(self.get_blog_layout(starturl))
        except:
            print('Something failed with the download.')
            exit()
        imgurhashes = re.findall(regex, imgurHTML.text)

        for hashes in imgurhashes:
            finishedurl.append('https://i.imgur.com/{0}{1}'.format(hashes[0], hashes[1]))
        return finishedurl


def main():
    urlinput = input('Please enter your Imgur Album URL: \n')
    imgururls = ImgurURL()
    urls = imgururls.get_imgur_urls(urlinput)

    for url in urls:
        print(url)

if __name__ == '__main__':
    main()
