from PIL import Image
from resizeimage import resizeimage
from io import BytesIO
from .exception import *
import requests

class ImgResizer(object):

    def resizeFromUrl(imageUrl, width, height, proxies = None):
        # bytes stream
        # use proxies if give
        if proxies:
            req = requests.get(imageUrl, stream=True, proxies=proxies)
        else:
            req = requests.get(imageUrl, stream=True)

        if not req.ok:
            raise ResponseIsNotOK('request is not OK, status code: {}'.format(req.status_code))

        # store into imag
        img = BytesIO(req.content)

        image = resizeimage.resize_cover(Image.open(img), [width, height])

        # return object

        return image
