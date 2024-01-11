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

    else:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Extract the contents to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        folder_name = archive_filename.split('.')[0]
        releases_path = '/data/web_static/releases/{}/'.format(folder_name)
        run('sudo mkdir -p {}'.format(releases_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, releases_path))

        # Move the contents to the proper location
        run('sudo mv {}web_static/* {}'.format(releases_path, releases_path))

        # Remove the temporary files
        run('sudo rm -rf {}web_static'.format(releases_path))
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Update the symbolic link
        current_path = '/data/web_static/current'
        run('sudo rm -rf {}'.format(current_path))
        run('sudo ln -s {} {}'.format(releases_path, current_path))
        return True
