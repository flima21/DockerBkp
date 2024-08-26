import docker
import os
from datetime import datetime
from shutil import make_archive

# date today
TODAY = datetime.now().strftime('%Y%m%d%H%M%S')
DEBUG = False

# instance docker
instance = docker.from_env()

containers = instance.containers.list() # all containers
volumes = instance.volumes.list() # all volumes

for c in containers:
    if DEBUG == False:
        c.commit(repository=f"{c.name}_bkp_{TODAY}",tag=TODAY)

    else: 
        print(c.name)

for v in volumes:
    if DEBUG == False:
        make_archive(f"VolumesBkp/Volume{v.name}{TODAY}",'zip',root_dir=v.attrs.get('Mountpoint'))            
    else:
        print(v.name)
        print(v.attrs)
instance.close()

print(f"BKP CREATED IN {os.getcwd()}")