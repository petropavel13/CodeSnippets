#!/usr/local/bin/python3

import os
import shutil


SNIPPETS_EXT = ".codesnippet"
CURRENT_DIR = os.getcwd()
XCODE_SNIPPETS_DIR = os.path.expanduser('~') + "/Library/Developer/Xcode/UserData/CodeSnippets/"


def create_snippets_folder_if_needed():
    if not os.path.exists(XCODE_SNIPPETS_DIR):
        print(f"There is no {XCODE_SNIPPETS_DIR} directory, creating...")
        os.makedirs(XCODE_SNIPPETS_DIR)


def get_snippets(path):
    return [os.path.join(path, f) for f in os.listdir(path) 
            if os.path.isfile(os.path.join(path, f)) and SNIPPETS_EXT in f]


def diff_snippets(new_snippets, old_snippets):
    file_names = [os.path.basename(f) for f in old_snippets]
    return [f for f in new_snippets if os.path.basename(f) in file_names]


def ask_for_overriding():
    answer = " "
    attempt = 0

    while (answer not in "yn"):
        if attempt == 3:
            break

        attempt += 1
        answer = input("Do you want to override them: (y/n)? ")

        if answer not in "yn":
            print("Answer should be 'n' or 'y'")

    return answer == "y"


def copy_files(files):
    for file in files:
        file_name = os.path.basename(file)
        shutil.copyfile(file, XCODE_SNIPPETS_DIR + file_name)


def move_snippets(snps, override=[]):
    is_overriding = False

    if override:
        print(f"There some duplicates in the {XCODE_SNIPPETS_DIR}")
        print("Files:\n- " + "\n- ".join(override))
        is_overriding = ask_for_overriding()

    if is_overriding:
        copy_files(snps)

    else:
        unique = [f for f in snps if f not in override]
        copy_files(unique)

    return 0


def main():
    create_snippets_folder_if_needed()

    snippets = get_snippets(CURRENT_DIR)
    current_snippets = get_snippets(XCODE_SNIPPETS_DIR)
    overriding_snippets = diff_snippets(snippets, current_snippets)

    result = move_snippets(snippets, override=overriding_snippets)

    if result == 0:
        print("Snippets were copied successfully")

    exit(result)


if __name__ == "__main__":
    main()
