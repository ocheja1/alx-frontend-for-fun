#!/usr/bin/env python
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('markdown_file', help='The name of the Markdown file')
    parser.add_argument('output_file', help='The name of the output HTML file')
    args = parser.parse_args()

    markdown_file = args.markdown_file
    output_file = args.output_file

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    else:
        # In this section, you can convert the Markdown file to HTML and write it to the output file.
        # You may use a library like 'markdown2html' for this purpose.

        # For demonstration purposes, let's create a simple HTML file from the Markdown content.
        with open(markdown_file, 'r') as markdown_file:
            markdown_content = markdown_file.read()
            html_content = f"<html><body>{markdown_content}</body></html>"

        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    else:
        main()
