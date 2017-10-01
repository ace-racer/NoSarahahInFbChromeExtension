
def insert_image_details_and_image_text(text_from_image, image_name, image_extension, imageurl):
    """Inserts the details of the image in a SQL server table to persist the information"""
    import pypyodbc
    import datetime
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=ANCHAT-850G3;'
                                  'Database=PythonImageRecognition')
    cursor = connection.cursor()
    sql_command = "INSERT INTO [Image details] ([Image Text], [Image Name], [Image Extension], [Image Url], [Created On]) VALUES (?,?,?,?,?)"
    values = [text_from_image, image_name, image_extension, imageurl, datetime.datetime.now()]
    cursor.execute(sql_command, values)
    connection.commit()
    connection.close()

