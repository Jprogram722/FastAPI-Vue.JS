# this file will contain helper functions

def get_img_path(img_file: str) -> str:
    """
    This function will take in a img file as a string and concatinate it will a folder path string

    Example:
    >>> get_img_path("phone.png")
    >>> "\\src\\pics\\phone.png"
    """

    if img_file is not None:
        pic_folder = '\\src\\pics\\'
        img_path = pic_folder + img_file
    else:
        img_path = img_file

    return img_path