import os

machine = "raspberrypi4"
distro = "custom-distro"

build_dir = "./build"
source_dir = "workdir/source"

conf_dir = os.path.join(build_dir, "conf")
template_local_conf = os.path.join(source_dir, "templates", "local.conf")
template_bblayers_conf = os.path.join(source_dir, "templates", "bblayers.conf")

layers = [
    os.path.join(source_dir, "meta-layer"),
    os.path.join(source_dir, "openembedded-core/meta"),
    os.path.join(source_dir, "meta-openembedded/meta-oe"),
    os.path.join(source_dir, "meta-raspberrypi"),
]

os.makedirs(conf_dir, exist_ok=True)

local_conf_path = os.path.join(conf_dir, "local.conf")
with open(local_conf_path, "w") as local_conf:
    local_conf.writelines(
        [
            f'MACHINE = "{machine}"\n',
            f'DISTRO = "{distro}"\n',
            'PACKAGE_CLASSES = "package_rpm"\n',
            'EXTRA_IMAGE_FEATURES = "debug-tweaks ssh-server-openssh"\n',
            'IMAGE_INSTALL:append = " python3 git"\n',
            'ENABLE_UART = "1"\n',
            'GPU_MEM = "128"\n',
            'DL_DIR ?= "${TOPDIR}/downloads"\n',
            'SSTATE_DIR ?= "${TOPDIR}/sstate-cache"\n',
            'INHERIT += "rm_work"\n',
        ]
    )

bblayers_conf_path = os.path.join(conf_dir, "bblayers.conf")
with open(bblayers_conf_path, "w") as bblayers_conf:
    bblayers_conf.write('BBPATH = "${TOPDIR}"\n')
    bblayers_conf.write('BBFILES ?= ""\n\n')
    bblayers_conf.write('BBLAYERS ?= " \\\n')
    for layer in layers:
        bblayers_conf.write(f"{layer} \\\n")
    bblayers_conf.write('"\n')

print(f"Configuration setup complete. You can now build using the build directory at {build_dir}")
