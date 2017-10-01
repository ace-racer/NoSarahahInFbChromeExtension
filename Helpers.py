def get_filedetails_from_image_url(image_url):
    """Gets the image name from the Image URL"""
    last_part_of_image_url = image_url.rsplit('/')[-1]
    filename_with_extension = last_part_of_image_url
    file_extension = filename_with_extension.rsplit('.')[-1]
    filename_without_extension = filename_with_extension.rsplit('.')[0]
    return filename_with_extension, filename_without_extension, file_extension
