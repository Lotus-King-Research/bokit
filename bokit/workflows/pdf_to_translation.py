def pdf_to_translation(file_path):

    '''Converts PDF to translation using Google Cloud Vision API and Mitra Translation API.
    file_path | str or Path | path to PDF file
    '''

    import bokit
    from .image_to_translation import image_to_translation


    images = bokit.utils.pdf_to_image(file_path)

    return image_to_translation(images)
