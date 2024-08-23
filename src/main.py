import docker
import os
from datetime import datetime
from shutil import make_archive

# date today
TODAY = datetime.now().strftime('%Y%m%d%H%M%S')

# instance docker
instance = docker.from_env()

containers = instance.containers.list() # all containers
volumes = instance.volumes.list() # all volumes

for c in containers:
    c.commit(repository=f"{c.name}_bkp_{TODAY}",tag=TODAY)

for v in volumes:
    make_archive(f"Volume{v.name}{TODAY}",'zip',root_dir=v.attrs.get('Mountpoint'))            

instance.close()

print(f"BKP CREATED IN {os.getcwd()}")