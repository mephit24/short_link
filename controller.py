import sqlite3
from zlib import crc32
from db import write_pair_link_to_db
import logging

def short_link_generating(long_link):
    short_link = crc32(long_link.encode())
    short_link = hex(short_link)
    return short_link[2:7]

def create_pair_links(long_link, custom=None):
    if not custom:
        short_link = short_link_generating(long_link)
    else:
        short_link = custom
    try:
        write_pair_link_to_db(long_link, short_link)
    except sqlite3.IntegrityError:
        logging.warning("Link already exist.")
