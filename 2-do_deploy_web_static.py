#!/usr/bin/python3
"""Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""
from fabric.api import env, put, run
env.user = 'ubuntu'
web01, web02 = '34.138.29.20', '34.74.165.238'
env.hosts = [web01, web02]


def do_deploy(archive_path):
    """ do_deploy docstring """
    from os.path import isfile
    if not isfile(archive_path):
        return False

    try:
        # Upload archive to /tmp/
        put(archive_path, "/tmp/")
        archive = archive_path.split('/')[1]
        output = "/data/web_static/releases/{}".format(archive.split('.')[0])
        run("mkdir -p {}/".format(output))

        run("tar -xzf /tmp/{} -C {}/".format(archive, output))

        run("rm -rf /tmp/{}".format(archive))
        run("mv {}/web_static/* {}".format(output, output))

        run("rm -rf /data/web_static/current")

        run("ln -s {}/ /data/web_static/current".format(output))
        print("New version deployed!")
        return True
    except:
        return False
