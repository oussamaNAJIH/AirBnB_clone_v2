#!/usr/bin/python3
"""
Write a Fabric script that creates and distributes an archive to
your web servers using the function deploy
"""
from fabric.api import *
from datetime import datetime
import os
env.hosts = ['100.25.102.204', '54.236.41.224']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_extension = file_name.split(".")[0]
        release_path = "/data/web_static/releases/"
        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')
        # Create the release directory
        run('mkdir -p {}{}/'.format(release_path, no_extension))
        # Extract the contents to the release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(
            file_name, release_path, no_extension))
        # Remove the temporary archive file
        run('rm /tmp/{}'.format(file_name))
        # Move contents from web_static subdirectory to release directory
        run('mv {}/web_static/* {}/'.format(
            release_path + no_extension, release_path + no_extension))
        # Remove the web_static directory within the release directory
        run('rm -rf {}/web_static'.format(release_path + no_extension))
        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')
        # Create a new symbolic link
        run('ln -s {}/ /data/web_static/current'.format(
            release_path + no_extension))
        return True
    except Exception as e:
        print("Error: {}".format(str(e)))
        return False


def deploy():
    """
    call the do_pack() and do_deploy(archive_path) functions
    """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
