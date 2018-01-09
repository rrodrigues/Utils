import os
import argparse
from PIL import Image


def crop_image(file_path, padding, dest_path=None):
    """Crop Image"""
    try:
        image = Image.open(file_path)
        image = image.crop((padding, padding, image.size[0] - padding,
                            image.size[1] - padding))
        image.save(dest_path if dest_path else file_path)
    except IOError as e:
        print("cannot create thumbnail for", file_path, ' error: ', e)


def crop_images(files_paths, padding, dest_folder):
    """Add padding to images"""
    for file_path in files_paths:
        dest_file = file_path if dest_folder is None else os.path.join(
            dest_folder, os.path.basename(file_path))
        crop_image(file_path, -1 * padding, dest_file)


def auto_crop_images(files_paths, padding, dest_folder):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image utils:')
    parser.add_argument(
        '--add-padding', dest='padding', type=int, help='Padding')
    parser.add_argument(
        '-o', '--output', type=str, help='Output folder (must exist)')
    parser.add_argument(
        '--auto-crop', action='store_true', default=False,
        help='Auto crop images')
    parser.add_argument('files', nargs='+', help='Files')

    args = parser.parse_args()

    # ToDo: method to iterate over files and run func?
    if args.padding and args.padding != 0:
        crop_images(args.files, args.padding, args.output)
    elif args.auto_crop:
        auto_crop_images(args.files, args.padding, args.output)
    else:
        print('Nothing to do here. Exiting now....')
