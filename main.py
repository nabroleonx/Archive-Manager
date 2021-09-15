from zipfile import ZipFile
from gooey import Gooey, GooeyParser
import os


def get_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def parse_args():
    parser = GooeyParser(description="This program will let you extract zip files or compress files into a zip file")
    
    subparsers = parser.add_subparsers(required=True, dest="process")
    extractor = subparsers.add_parser("Extract", help="Extract zip files")
    compressor = subparsers.add_parser("Compress", help="Compress to zip files")

    extractor.add_argument('input_file', widget="FileChooser", help="Choose the file to extract")
    compressor.add_argument('input_folder', widget="DirChooser", help="Choose the file to Compress")

    extractor.add_argument('output_folder', widget="DirChooser",
                           help="Extracted file location")
    compressor.add_argument('output_file', widget="DirChooser",
                            help="Compressed file location")

    extractor.add_argument('--Password', default=None, help="If you are working with encrypted file, enter the password below")

    return parser.parse_args()


@Gooey(program_name="Archive Manager", navigation="TABBED")
def main():
    args = parse_args()

    if args.process == "Extract":
        f_name, f_ext = os.path.splitext(args.input_file)
        with ZipFile(args.input_file) as output:
            output.extractall(os.path.join(args.output_folder, f_name), args.Password, pwd=args.Password)
    else:
        folder_name = os.path.basename(args.input_folder)
        file_paths = get_file_paths(args.input_folder)

        with ZipFile(os.path.join(args.output_file, folder_name + ".zip"), 'w') as zipped:
            for file in file_paths:
                zipped.write(file)


if __name__ == "__main__":
    main()
