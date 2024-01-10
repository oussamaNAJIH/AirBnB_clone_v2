#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
     return the archive path if the archive has been correctly generated
    """
    time_string = "{}{}{}{}{}{}".format(datetime.isoformat("%Y%m%d%H%M%S"))
    archive_name = "web_static_{}.tgz".format(time_string)
    local("makdir versions")
    archive = local("tar -ca versions/{} web_static".format(archive_name))
    if archive:
        return archive
    else:
        return None
