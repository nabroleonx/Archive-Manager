from zipfile import ZipFile
import os
from gooey import Gooey, GooeyParser


def extract_all_files(files, path_to_extract_to):
    with ZipFile(files, 'r') as file:
        file.extractall(path_to_extract_to)


def compress(files):
    with ZipFile(files+".zip", 'w') as zipped:
        for file in files:
            zip.write(file)


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


# def extract_single_file(files, path_to_extract_to, file_to_extract):
#     with open(file_to_extract, 'wb') as file:
#         file.write(files.read(os.path.join(
#             path_to_extract_to, file_to_extract)))

# def extract_selected_files(files, path_to_extract_to):
#     for file in files.namelist():
#         if file.endswith(".py"):
#             files.extract(file, path=path_to_extract_to)

# @Gooey
# def main():
#     path_of_zip_file = input("Enter path of the zip file > ")
#     path_to_extract_to = input("Enter the path you want to extract to > ")

#     menu_selection = input("What do you want to do")
#     '''1. Extract all files in a zip file.
#        2. Extract a single file.
#        3. Extract specific files using certain conditions.
#        4. Extracting password protected files.'''
#     with ZipFile(path_of_zip_file, 'r') as files:
#         if menu_selection == '1':
#             extract_all_files(files, path_to_extract_to)
#         elif menu_selection == '2':
#             extract_single_file()
#         elif menu_selection == '3':
#             extract_selected_files()
#         elif menu_selection == '4':
#             extract_protected_files
#         else:
#             print("please enter the correct number.")


# @Gooey(program_name="Archive Manager", program_description="This program will let you extract zip files or compress files into a zip file")
def parse_args():
    parser = GooeyParser()
    subparsers = parser.add_subparsers(required=True)
    extractor = subparsers.add_parser("Extract", help="Extract zip files")
    compressor = subparsers.add_parser(
        "Compress", help="Compress to zip files")

    extractor.add_argument(
        'input_file', widget="FileChooser", help="File to extract")
    compressor.add_argument(
        'to_be_zipped', widget="DirChooser", help="File to Compress")

    extractor.add_argument('output_file', widget="DirChooser",
                           help="Extracted file location")
    compressor.add_argument('zipped', widget="DirChooser",
                            help="Compressed file location")

    extractor.add_argument('--Password', default=None,
                           help="If you are working with encrypted file, enter the password below")
    compressor.add_argument('--Password', default=None,
                            help="If you are working with encrypted file, enter the password below")

    return parser.parse_args()


@Gooey
def main():
    args = parse_args()

    # files = args.input_file
    # path = args.output_file
    # extract_all_files(files, path)

    # with ZipFile(args.input_file) as output:
    #     output.extractall(args.output_file, args.Password, pwd=args.Password)

    file_paths = get_all_file_paths(args.to_be_zipped)

    with ZipFile("yay.zip", 'w') as zipped:
        for file in file_paths:
            zipped.write(file)


if __name__ == "__main__":
    main()
