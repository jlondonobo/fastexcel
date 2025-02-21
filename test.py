import argparse

import fastexcel


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-c", "--column", type=str, nargs="+", help="the columns to use")
    return parser.parse_args()


def main():
    args = get_args()
    excel_file = fastexcel.read_excel(args.file)
    use_columns = args.column or None

    for sheet_name in excel_file.sheet_names:
        excel_file.load_sheet_by_name(sheet_name, use_columns=use_columns).to_arrow()


if __name__ == "__main__":
    main()
