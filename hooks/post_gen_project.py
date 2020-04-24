#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def remove_open_source_files():
    file_names = ["LICENSE"]
    for file_name in file_names:
        os.remove(file_name)


def remove_dockerfile():

    dockerfile_stages = "{{ cookiecutter.dockerfile_stages }}"
    files_single = ["Dockerfile-single", "Makefile-docker-single"]
    files_multi = ["Dockerfile-multi", "Makefile-docker-multi"]

    if dockerfile_stages == "single":
        for fn in files_multi:
            os.remove(fn)

        for fn in files_single:
            os.rename(fn, fn[:len(fn)-len("-single")])  # Cut off -single

    elif dockerfile_stages == "multi":
        for fn in files_single:
            os.remove(fn)

        for fn in files_multi:
            os.rename(fn, fn[:len(fn)-len("-multi")])  # Cut off -multi


def main():
    "License"
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_open_source_files()

    "Docker files"
    remove_dockerfile()


if __name__ == "__main__":
    main()
