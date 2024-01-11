#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""
from fabric.api import *
import os
env.hosts = ['100.25.102.204', '54.236.41.224']


def do_clean(number=0):
    """
    Delete unnecessary archives in versions and releases folders
    """
    number = int(number)
    if number < 1:
        number = 1

    try:
        local_archives = sorted(os.listdir("versions"), reverse=True)
        local_archives = local_archives[number:]
        for archive in local_archives:
            local("rm -f versions/{}".format(archive))

        run_archives = run("ls -1 /data/web_static/releases/").split()
        run_archives = sorted(run_archives, reverse=True)
        run_archives = run_archives[number:]
        for archive in run_archives:
            run("rm -rf /data/web_static/releases/{}".format(archive))
    except Exception as e:
        print("Error: {}".format(str(e)))
