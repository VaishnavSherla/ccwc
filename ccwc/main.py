import argparse
import sys

def count_bytes(filename):
    with open(filename, 'rb') as f:
        return len(f.read())

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(1 for _ in f)

def count_words(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(len(line.split()) for line in f)

def count_characters(filename):
    with open(filename, 'rb') as f:
        text = f.read().decode('utf-8', errors='ignore')
    return len(text)

def print_results(counts, filename):
    if filename:
        print(f"{counts['lines']:5} {counts['words']:5} {counts['bytes']:5} {filename}")
    else:
        print(f"{counts['lines']:5} {counts['words']:5} {counts['bytes']:5}")

def main():
    parser = argparse.ArgumentParser(description="A simple implementation of the Unix `wc` command.")
    parser.add_argument('filename', nargs='?', type=str, help="The file to process. If not provided, reads from stdin.")
    
    parser.add_argument('-c', '--bytes', action='store_true', help="Count bytes")
    parser.add_argument('-l', '--lines', action='store_true', help="Count lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count words")
    parser.add_argument('-m', '--chars', action='store_true', help="Count characters")

    args = parser.parse_args()

    filename = args.filename

    if args.bytes:
        if filename:
            count = count_bytes(filename)
            print(f"{count} {filename}")
        else:
            # Read stdin in binary mode and count bytes
            count = len(sys.stdin.buffer.read())
            print(f"{count} ")

    elif args.lines:
        if filename:
            count = count_lines(filename)
            print(f"{count} {filename}")
        else:
            # Read stdin line by line
            count = sum(1 for _ in sys.stdin)
            print(f"{count} ")

    elif args.words:
        if filename:
            count = count_words(filename)
            print(f"{count} {filename}")
        else:
            # Read stdin line by line and count words
            count = sum(len(line.split()) for line in sys.stdin)
            print(f"{count} ")

    elif args.chars:
        if filename:
            count = count_characters(filename)
            print(f"{count} {filename}")
        else:
            # Read stdin in binary mode and decode to UTF-8
            text = sys.stdin.buffer.read().decode('utf-8', errors='ignore')
            count = len(text)
            print(f"{count} ")
    
    else:
        if filename:
            counts = {
                'bytes': count_bytes(filename),
                'lines': count_lines(filename),
                'words': count_words(filename),
            }
            print_results(counts, filename)
        else:
            # Read stdin in binary mode and calculate all counts
            raw_data = sys.stdin.buffer.read()
            text = raw_data.decode('utf-8', errors='ignore')
            counts = {
                'bytes': len(raw_data),
                'lines': text.count('\n') + (not text.endswith('\n')),  # Handle cases where the last line might not end with '\n'
                'words': len(text.split()),
            }
            print_results(counts, None)

if __name__ == "__main__":
    main()
