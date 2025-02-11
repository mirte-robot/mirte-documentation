#!/bin/env python3

# arg1 = release name
# arg2 = zip file

import sys
import os

# open _build/html_multi/$1/index.html
# find <\!-- VERSIONS START --> and <\!-- VERSIONS END -->, copy lines in between.
# unzip $2
# replace all <!-- VERSIONS PLACEHOLDER --> with copied lines

def main():
    if len(sys.argv) != 3:
        print("Usage: fix_versions.py <release name> <zip file>")
        sys.exit(1)

    release_name = sys.argv[1]
    zip_file = sys.argv[2]
    print(f"Release name: {release_name}")
    print(f"Zip file: {zip_file}")
    

    # open the file
    with open(f"_build/html_multi/{release_name}/index.html", "r") as f:
        lines = f.readlines()

    # find the lines
    start = None
    end = None
    for i, line in enumerate(lines):
        if "<!-- VERSIONS START -->" in line:
            start = i
        if "<!-- VERSIONS END -->" in line:
            end = i

    if start is None or end is None:
        print("Could not find start or end of versions")
        sys.exit(1)
    else:
        print(f"Found start at {start} and end at {end}")
    # copy the lines
    version_lines = lines[start:end+1]
    # unzip the file
    print("removing old directory...")
    os.system(f"rm -rf _build/html_multi/{release_name}")
    print("unzipping...")
    os.system(f"unzip {zip_file} -d _build/html_multi/{release_name}")
    # replace all <!-- VERSIONS PLACEHOLDER --> with the lines
    for root, dirs, files in os.walk(f"_build/html_multi/{release_name}"):
        for file in files:
            if file.endswith(".html"):
                print(f"Replacing in {os.path.join(root, file)}")
                # get the depth of the file
                depth = root.count("/") - 3
                print(f"Depth: {depth}")
                depth_string = "../"*depth
                # add the correct number of ../
                version_depth_lines = [line.replace("<a href=\"", f"<a href=\"{depth_string}") for line in version_lines]
                with open(os.path.join(root, file), "r") as f:
                    file_lines = f.readlines()

                with open(os.path.join(root, file), "w") as f:
                    for line in file_lines:
                        if "<!-- VERSIONS PLACEHOLDER -->" in line:
                            for version_line in version_depth_lines:
                                f.write(version_line)
                        else:
                            f.write(line)

    # remove the zip file
    print("removing zip file...")
    os.system(f"rm {zip_file}")

if __name__ == "__main__":
    main()