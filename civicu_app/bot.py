#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is a simple command line bot that will respond to basic greetings.

For example, here is an example of a conversation with this bot:

$ bot Hello
Hi, how are you?
$ bot Hi
Hi, how are you?


To install the command 'bot', run `python setup.py install`.
"""

from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
import os
import requests

from civicu_app import __version__

__author__ = "Ashley Riehl"
__copyright__ = "Ashley Riehl"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def recognize_greeting(statement):
    """Recognizes if string statement starts with Hi or Hey or any other greeting.

    Args:
        statement (str): a string from the commandline from the user
    Returns:
        bool: True if statement is a greeting, False otherwise

    >>> recognize_greeting('hi')
    True
    """
    statement = statement.lower()
    if statement.startswith('hi') or statement.startswith('hello'):
        return True
        print('Hi, how are you?')
    else:
        return False

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser() #description="Just a greeting recognizer"
    parser.add_argument(
        '--version',
        action='version',
        version='civicu_app {ver}'.format(ver=__version__))
    parser.add_argument(
        '--v'
        'upload'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_known_args(args)

def upload(filename):
    base_dir = os.path.join(os.getenv('HOME'), 'Desktop')
    url ='http://localhost:8000/labelgame/api/v1/images/'
    with open(os.path.join(base_dir, filename), 'rb') as fin:
        print(fin.name)
        POST_data = {'caption': 'baby ghost', 'uploaded_by': 1, 'date_taken': '2017-02-17'}
        files = {'img_file': (filename, fin), 'filename': filename}
        resp = requests.post(url, data=POST_data, files=files)

# class Match:
#
#     ___init__(self, groups):
#         self.group_list = groups or []
#
#     def groups():
#         return self.group_list
#
# class Matcher:
#     """A pseudo-regex object with only a match method, and a hard-coded decision tree (FSM)."""
#
#     def match(statement):
#         """ Return a Match object with a 1-len list of "groups" containing the name that the user addressed """
#         words = statement.lower().strip().split()
#         if not len(words):
#             return Match([])
#         w0 = words[0]
#         if len(w0) > 1 and w0[0] == 'h':
#             if w0[1] == 'i':
#                 return Match(words[1] if len(words) > 1 else [''])
#             if len(w0) > 2 and w0[1] == 'e' and w0[2] == 'y':
#                 return Match(words[1] if len(words) > 1 else [''])
#         return []

def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args, unknown = parse_args(args)
    # setup_logging(args.loglevel)
    # _logger.debug("Starting crazy calculations...")
    print("{}".format(recognize_greeting(' '.join(unknown))))
    # _logger.info("Script ends here")


WALLPAPER_PATH = os.path.join(os.path.expanduser('~'), 'Pictures', 'wallpaper')

def change_wallpaper(new_path=WALLPAPER_PATH, wallpaper_path=WALLPAPER_PATH, backup=False):
    new_path, wallpaper_path = os.path.abspath(new_path), os.path.abspath(wallpaper_path)
    with open(new_path, 'rb') as fin:
        newimage = fin.read()
    if new_path != wallpaper_path:
        with open(wallpaper_path, 'rb') as fin:
            oldimage = fin.read()
        if newimage != oldimage:
            with open(wallpaper_path, 'wb') as fout:
                fout.write(newimage)
            return newimage

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
