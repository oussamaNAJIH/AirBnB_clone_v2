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
        archive_without_ext = os.path.basename(archive_path).split(".")[0]
        destination = "/data/web_static/releases/{}".format(archive_without_ext)
        source = "/tmp/{}".format(archive_without_ext)
        # Create the release directory
        run("mkdir -p {}".format(destination))
        # Extract the contents to the release directory
        run("tar -xzvf {} -C {}".format(source, destination))
        # Remove the temporary archive file
        run("rm {}".format(source))
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        # Move contents from web_static subdirectory to release directory
        run('mv {}/web_static/* {}'.format(destination, destination))
        # Remove the web_static directory within the release directory
        run('rm -rf {}/web_static'.format(destination))
        # Create a new symbolic link
        run('ln -s {}/ /data/web_static/current'.format(destination))
        return True
    except Exception as e:
        print("Error: {}".format(str(e)))
        return False
