import os
import sys
from collections import defaultdict
from display import display_charts


def analyze_partition(partition, target_extension):
    total_files = 0
    total_directories = 0
    extension_count = defaultdict(int)
    extension_size = defaultdict(int)

    # Iterate through the directory and its subdirectories
    for root, dirs, files in os.walk(partition):
        total_directories += 1
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)

            # files with extensions
            if '.' in file:
                _, file_extension = os.path.splitext(file)
                extension_count[file_extension] += 1
                extension_size[file_extension] += os.path.getsize(file_path)

            # files without extensions
            else:
                extension_count["no extension"] += 1
                extension_size["no extension"] += os.path.getsize(file_path)

    # Separate extensions for sorting by count and size
    extensions_by_count = sorted(extension_count.items(), key=lambda dict: dict[1], reverse=True)
    extensions_by_size = sorted(extension_size.items(), key=lambda dict: dict[1], reverse=True)
    ebc_copy = extensions_by_count.copy()

    # Add "others" category for extensions not in the top 15
    other_count = sum(ext[1] for ext in extensions_by_count[15:])
    other_size = sum(ext[1] for ext in extensions_by_size[15:])
    extensions_by_count = extensions_by_count[:15] + [("Other", other_count)]
    extensions_by_size = extensions_by_size[:15] + [("Other", other_size)]

    # Check if a target extension is specified
    if target_extension:
        target_extension = target_extension.lower()
        if target_extension in extension_count:
            print(f"\nTarget Extension '{target_extension}' exists in the partition.")
        else:
            print(f"\nTarget Extension '{target_extension}' does not exist in the partition.")

    print(f"Total Directories: {total_directories}")
    print(f"Total Files: {total_files}")

    # Display extension count and size
    print("\nExtensions by Count:")
    for ext, count in extensions_by_count:
        print(f"{ext}: {count} files")

    print("\nExtensions by Size:")
    for ext, size in extensions_by_size:
        print(f"{ext}: {size / (1024 * 1024):.2f} MB")

    return extensions_by_count, extensions_by_size, total_directories, total_files, ebc_copy


if __name__ == "__main__":

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python main.py <partition> or python main.py <partition> <extension>")
        sys.exit(1)

    partition = sys.argv[1] + ":\\"
    target_extension = None

    if len(sys.argv) == 3:
        target_extension = sys.argv[2]

    extensions_by_count, extensions_by_size, total_directories, total_files, ebc_copy = (
        analyze_partition(partition, target_extension))

    display_charts(extensions_by_count, extensions_by_size, total_directories, total_files, ebc_copy)
