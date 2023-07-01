def image_to_translation(images):

    '''Converts images to translation using Google Cloud Vision API and Mitra Translation API.
    images | list of str or Path or bytes | path to image file or image bytes
    '''

    ocr = bokit.OCR()

    translate = bokit.Translate()

    out = []

    import tqdm

    for i in tqdm.tqdm(range(len(images))):
        
        data = ocr.query(images[i])
        out.append(translate.query(data))
                       
    return out
