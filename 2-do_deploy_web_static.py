#!/usr/bin/python3
"""
Fabric script distributes an archive to your web servers
using the function do_deploy
"""
from fabric.api import *
import os
env.hosts = ['100.25.102.204', '54.236.41.224']


def do_deploy(archive_path):
    """
    Returns True if all operations have been done correctly
    otherwise returns False
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_without_ext = archive_path.split("/")[-1].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(archive_without_ext))
        destination = "/data/web_static/releases/{}".format(archive_without_ext)
        source = "/tmp/{}".format(archive_without_ext)
        run("tar -xzvf {} -C {}".format(source, destination))
        run("rm {}".format(source))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(source))
        return True
    except:
        return False
