import os
import time

import matplotlib.pyplot as plt


def display_charts(extensions_by_count, extensions_by_size, total_directories, total_files, ebc_copy):
    # Plot pie chart for total number of files and directories
    plt.pie([total_directories, total_files], labels=['Directories', 'Files'], autopct='%1.1f%%')
    plt.title('Total Number of Directories and Files')
    plt.show()

    # Plot horizontal bar chart for top 15 extensions by count
    plt.figure(figsize=(9, 7))
    plt.barh([ext[0] for ext in extensions_by_count], [ext[1] for ext in extensions_by_count])
    plt.xlabel('File Count')
    plt.title('Top Extensions by Count')
    plt.savefig('horizontal_bar_chart_count.png')
    plt.show()

    # Plot vertical bar chart for top 15 extensions by size
    plt.figure(figsize=(9, 7))
    plt.bar([ext[0] for ext in extensions_by_size], [ext[1] / (1024 * 1024) for ext in extensions_by_size])
    plt.ylabel('Size (MB)')
    plt.title('Top Extensions by Size')
    plt.xticks(rotation=45, ha="right")
    plt.savefig('vertical_bar_chart_size.png')
    plt.show()

    # Plot pie chart for percentage of top 8 extensions by count
    plt.pie([ext[1] for ext in extensions_by_count[:8]], labels=[ext[0] for ext in extensions_by_count[:8]],
            autopct='%1.1f%%')
    plt.title('Percentage of Top 8 Extensions by Count')
    plt.savefig('pie_chart_count.png')
    plt.show()

    # Plot pie chart for percentage of top 8 extensions by size
    plt.pie([ext[1] / (1024 * 1024) for ext in extensions_by_size[:8]],
            labels=[ext[0] for ext in extensions_by_size[:8]], autopct='%1.1f%%')
    plt.title('Percentage of Top 8 Extensions by Size')
    plt.savefig('pie_chart_size.png')
    plt.show()

    # Plot horizontal bar chart for each letter of the alphabet (top 15 extensions by count)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        extensions_by_letter = [(ext, count) for ext, count in ebc_copy if ext.startswith('.' + letter)]
        if extensions_by_letter:
            top_extensions_by_letter = sorted(extensions_by_letter, key=lambda x: x[1], reverse=True)[:15]
            plt.figure(figsize=(10, 8))
            plt.barh([ext[0] for ext in top_extensions_by_letter], [ext[1] for ext in top_extensions_by_letter])
            plt.xlabel('File Count')
            plt.title(f'Top Extensions Starting with {letter} by Count')
            plt.savefig(f'.\\alphabetic_charts\\horizontal_bar_chart_{letter}.png')

            plt.close()
