def pdf_to_image(file_path):

    '''Converts PDF to images, one image per page.
    
    file_path | str or Path | path to PDF file

    '''
    
    import pdf2image
    import io

    out = []
    
    images = pdf2image.convert_from_path(file_path)
    
    for i in range(len(images)):

        img_byte_arr = io.BytesIO()
        images[i].save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        out.append(img_byte_arr)
        
    return out
