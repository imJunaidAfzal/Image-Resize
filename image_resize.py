import cv2
import os


def resize_profile(img_path: str, dim=(200, 200), save_path=None) -> tuple:
    """
    Take Image Path, resize image according to dim and
    save it to current working directory with name (cropped_filename).

    Parameters:
     img_path: path of Image (str)
     dim: Output size of image (tuple)

    Returns:

    """
    saved_path = save_path
    if not os.path.isfile(img_path):
        raise FileNotFoundError('Image Not Found at given path')
    im = cv2.imread(img_path)
    shape = im.shape
    im_size = round((os.path.getsize(img_path) / 1024), 1)
    print(str(im_size) + 'Kb')
    if shape[0] < dim[0] or shape[1] < dim[1]:
        raise Exception('ImageDimensionToSmall')
    elif im_size > 1024:
        raise Exception('ImageSizeTooLarge')
    elif dim[0] < 200 or dim[1] < 200:
        raise Exception('ReceiveZeroSize')
    else:
        imr = cv2.resize(im, dim)
        imr_name = img_path.split('/')[-1]
        if save_path:
            print(f'{save_path}cropped_{imr_name}')
            cv2.imwrite(f'{save_path}cropped_{imr_name}', imr)
            saved_path = f'{save_path}cropped_{imr_name}'
        else:
            cv2.imwrite(f'cropped_{imr_name}', imr)
            saved_path = f'{os.getcwd()}/cropped_{imr_name}'
        return imr, saved_path
