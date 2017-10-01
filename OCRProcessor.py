

def get_text_from_image(imageurl):
    from Helpers import get_filedetails_from_image_url

    try:
        import Image
    except ImportError:
        from PIL import Image
    import pytesseract
    import urllib2

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract';
    filename_with_extension, filename_without_extension, extension = get_filedetails_from_image_url(imageurl)

    # download the image from the URL

    imagesLocalFolderLocation = "C:\\Users\\anchat\\Desktop\\Python\\"

    completeImageLocation = imagesLocalFolderLocation + filename_with_extension
    r = urllib2.urlopen(imageurl)
    f = open(completeImageLocation, 'wb')
    f.write(r.read())
    f.close()



    textFromImage = (pytesseract.image_to_string(Image.open(completeImageLocation)))
    return textFromImage, filename_without_extension, extension

