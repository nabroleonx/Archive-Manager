from zipfile import ZipFile
from gooey import Gooey, GooeyParser
import os


def parse_args():
    parser = GooeyParser(description="This program will let you extract zip files or compress files into a zip file")

    subparsers = parser.add_subparsers(required=True, dest="process")
    extractor = subparsers.add_parser("Extract", help="Extract zip files")
    compressor = subparsers.add_parser("Compress", help="Compress to zip files")

    extractor.add_argument('input_file', widget="FileChooser", help="Choose the file you want to extract")
    compressor.add_argument('input_folder', widget="DirChooser", help="Choose the file you want to Compress")

    extractor.add_argument('output_folder', widget="DirChooser", help="Extracted file location")
    compressor.add_argument('output_file', widget="FileSaver", help="Compressed file location")

    extractor.add_argument('--password', default=None, help="If you are working with encrypted file, enter the password below.")

    return parser.parse_args()


@Gooey(program_name="Archive Manager", navigation="TABBED")
def main():
    args = parse_args()

    if args.process == "Extract":
        dest_folder = os.path.basename(args.input_file).split(".")[0]
        with ZipFile(args.input_file) as output:
            output.extractall(os.path.join(args.output_folder, dest_folder), pwd=bytes(str(args.password), "utf-8"))
    else:
        with ZipFile(os.path.join(args.output_file + ".zip"), 'w') as zipped:
            abs_path = os.path.abspath(args.input_folder)
            for root, directories, files in os.walk(args.input_folder):
                for filename in files:
                    abs_file_name = os.path.abspath(os.path.join(root, filename))
                    arcname = abs_file_name[len(abs_path) + 1:]
                    zipped.write(abs_file_name, arcname)


if __name__ == "__main__":
    main()
