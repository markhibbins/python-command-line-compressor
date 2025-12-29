#!/usr/bin/env python3

import argparse
import glob
import sys
import gzip
import shutil
from pathlib import Path
from typing import List

class CommandLineCompressor:

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def process_files(self, file_patterns: List[str]) -> None:
        matched_files = []

        # Expand wildcards for each pattern
        for pattern in file_patterns:
            matches = glob.glob(pattern, recursive=False)
            if matches:
                matched_files.extend(matches)
            else:
                print(f"Warning: No files matched pattern '{pattern}'", file=sys.stderr)

        if not matched_files:
            print("Err"
                  "or: No files found to process", file=sys.stderr)
            return

        # Remove duplicates while preserving order
        matched_files = list(dict.fromkeys(matched_files))

        if self.verbose:
            print(f"Found {len(matched_files)} file(s) to process:")
            for file in matched_files:
                print(f"  - {file}")

        # Process each file
        for file_path in matched_files:
            self.compress_file(file_path)

    def compress_file(self, file_path: str) -> None:
        path = Path(file_path)

        if not path.exists():
            print(f"Error: File '{file_path}' does not exist", file=sys.stderr)
            return

        if not path.is_file():
            print(f"Error: '{file_path}' is not a file", file=sys.stderr)
            return

        if self.verbose:
            print(f"Processing: {file_path}")

        # TODO: Implement actual compression logic here
        try:
            # Placeholder for compression implementation
            print(f"Compressing: {file_path}")
            with open(f"{file_path}", 'rb') as f_in:
                with gzip.open(f"{file_path}.gz", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)  # type: ignore[arg-type]

        except Exception as e:
            print(f"Error compressing '{file_path}': {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Compress files from the command line",
        epilog="Examples:\n"
               "  %(prog)s file.txt\n"
               "  %(prog)s *.txt\n"
               "  %(prog)s file1.txt file2.txt\n"
               "  %(prog)s data/*.log",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'files',
        nargs='+',
        help='File(s) to compress (supports wildcards like *.txt)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Create compressor instance and process files
    compressor = CommandLineCompressor(verbose=args.verbose)
    compressor.process_files(args.files)


if __name__ == '__main__':
    main()