import sys
import OCRProcessor
import SQLServerConnector

def main(argv):
    if len(argv) != 2:
        print 'Usage: OCRProcessor.py <<URL>>'
    else:
        # imageFileUrl = "http://www.keil.com/pack/doc/mw/Network/html/http_server_block_diagram.png"
        imageUrl = argv[1]
        textFromImage, filename_without_extension, extension = OCRProcessor.get_text_from_image(imageUrl)
        print textFromImage
        SQLServerConnector.insert_image_details_and_image_text(textFromImage, filename_without_extension, extension, imageUrl)

if __name__ == "__main__":
    main(sys.argv)
