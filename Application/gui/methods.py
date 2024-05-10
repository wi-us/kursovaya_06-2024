from PIL import Image

def changeImageSize(imagePath : str, width : int):
    """
    .png only
    """
    _image = Image.open(imagePath)
    width_percent = (width / float(_image.size[0]))
    height_size = int((float(_image.size[0]) * float(width_percent)))
    new_image = _image.resize((width, height_size))
    new_image.save(imagePath[:-4] + "_new" + ".png")
    return imagePath

