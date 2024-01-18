#!/usr/bin/python3

""" Fabric Module to generate .tgz archive from contents of specific folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir versions")

        # Generate archive path
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(time_format)

        # Compress web_static contents into the archive
        local("tar -czvf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None
