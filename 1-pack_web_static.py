#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Creates a .tgz archive from web_static folder.
    Returns the path to the created archive, or None on failure.
    """
    now = datetime.now()
    time_string = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time_string)
    local("mkdir -p versions")
    archive_path = "versions/{}".format(archive_name)
    command = "tar -czvf {} web_static".format(archive_path)
    result = local(command)
    if result.failed:
        return None
    return archive_path
