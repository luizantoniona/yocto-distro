## Custom Yocto Distribution Project

## How to build:

- Update submodules:
```
git submodule update --remote
```

- Generate conf files:
```
python3 setup.py
```

- Start building enviroment:
```
source source/openembedded-core/oe-init-build-env build
```

- Generate image:
```
bitbake custom-image
```

---

<p align="center">
  <img alt="GitHub count language" src="https://img.shields.io/github/languages/count/luizantoniona/yocto-distro" />
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/luizantoniona/yocto-distro" />
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/luizantoniona/yocto-distro" />
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/luizantoniona/yocto-distro" />
</p