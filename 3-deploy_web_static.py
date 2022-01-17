#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
"""
from fabric.api import env, run, put, local
from datetime import datetime

web01, web02 = '34.138.29.20', '34.74.165.238'
env.hosts = [web01, web02]


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    dt = datetime.now()
    dt_format = dt.strftime("%Y%m%d%H%M%S")
    archive = "web_static_" + dt_format + ".tgz"

    local("mkdir -p versions")

    try:
        local('tar -cvzf versions/{} web_static'.format(archive))
        return 'versions/{}'.format(archive)
    except:
        return None


def do_deploy(archive_path):
    """ do_deploy docstring """
    from os.path import isfile
    if not isfile(archive_path):
        return False

    try:

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


def deploy():
    """ do_deploy docstring """
    path_name = do_pack()
    if path_name is None:
        return False
    return do_deploy(path_name)
