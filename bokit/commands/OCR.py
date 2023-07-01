class OCR: 

    '''Converts images to text using Google Cloud Vision API.'''

    def __init__(self):

        from google.cloud import vision
        self.vision = vision

        _ = ''

    def query(self, image, lang_hint=None):

        '''Converts images to text using Google Cloud Vision API.
        
        image | str or Path or bytes | path to image file or image bytes
        lang_hint | str | language hint for OCR
        '''

        import io
        import json
        import pathlib

        vision_client = self.vision.ImageAnnotatorClient()

        if isinstance(image, (str, pathlib.Path)):
            with io.open(image, "rb") as image_file:
                content = image_file.read()
        
        else:
            content = image
        ocr_image = self.vision.Image(content=content)

        features = [
            {
                "type_": self.vision.Feature.Type.DOCUMENT_TEXT_DETECTION,
                "model": "builtin/weekly",
            }
        ]
        image_context = {}
        if lang_hint:
            image_context["language_hints"] = [lang_hint]

        response = vision_client.annotate_image(
            {"image": ocr_image, "features": features, "image_context": image_context}
        )
        response_json = self.vision.AnnotateImageResponse.to_json(response)
        response = json.loads(response_json)
        
        return response['textAnnotations'][0]['description']
    