try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import urllib

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract';

#download the image from the URL


print(pytesseract.image_to_string(Image.open("C:\\Users\\anchat\\Desktop\\testImage1.jpg")))