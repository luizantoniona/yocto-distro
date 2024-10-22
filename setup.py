import os
import shutil

machine = ""
image_name = ""
distro = ""

build_dir = "./build"
source_dir = "./source"

conf_dir = os.path.join(build_dir, "conf")

template_local_conf = os.path.join(
    source_dir, "templates", "local.conf"
)

template_bblayers_conf = os.path.join(
    source_dir, "templates", "bblayers.conf"
)

layers = [
    os.path.join(source_dir, "meta"),
    os.path.join(source_dir, "meta-layer"),
    '"',
]

os.makedirs(conf_dir, exist_ok=True)

shutil.copy(template_local_conf, conf_dir)
shutil.copy(template_bblayers_conf, conf_dir)

local_conf_path = os.path.join(conf_dir, "local.conf")
with open(local_conf_path, "a") as local_conf:
    local_conf.write("\n")
    local_conf.write(f"MACHINE = {machine}\n")
    local_conf.write(f"DISTRO = {distro}\n")
    local_conf.write(f"IMAGE_INSTALL += {image_name}\n")

bblayers_conf_path = os.path.join(conf_dir, "bblayers.conf")
with open(bblayers_conf_path, "a") as bblayers_conf:
    for layer in layers:
        bblayers_conf.write(f"  {layer}\n")

print(
    f"Configuration setup complete. You can now build using the build directory at {build_dir}"
)
