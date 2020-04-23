import os
from pathlib import Path

from jinja2 import Template

import parser
from utils import write_to_file
from utils import mkdir_p

parser.init()


# parse and assign to vars
spec = parser.spec


def _concat(slice: str) -> str:
    """helper to concatenate each template slice."""
    return "{}\n".format(slice)


def slices_filename_content_hash() -> dict:
    """create a dict of filename: content for slices"""
    docker_slices = {}
    path = Path.cwd().joinpath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "slices")
    )
    for file in path.iterdir():
        docker_slices[file.name] = file.read_text()
    return docker_slices


def concat_slices(component: str = "tensorflow", flavor: str = "mkl") -> str:
    """concatenate templates based on the what user want"""
    docker_slices = slices_filename_content_hash()
    names = ["os.dockerfile"]
    dockerfile = ""
    if component == "tensorflow" and flavor == "mkl":
        names.append("tensorflow.dockerfile")
        names.append("horovod.dockerfile")
    if component == "pytorch" and flavor == "mkl":
        names.append("pytorch.dockerfile")
        names.append("horovod.dockerfile")
    for name in names:
        dockerfile += _concat(docker_slices[name])
    return "".join(dockerfile)


def insert_template_values(dockerfile: str, kwargs: dict):
    dockerfile = Template(dockerfile)
    dockerfile = dockerfile.render(**kwargs)
    return dockerfile


def generate_dockerfile(os: str, framework: str, file_name: str = "Dockerfile"):
    """generate and write to dir dockerfiles per `os` and `framework`"""
    dlrs = spec["stack"]["dlrs"]
    os_version = dlrs[os]["version"]
    pkgs = dlrs[os]["os_pkgs"]
    tf_version = dlrs[os]["tensorflow"]["mkl"]["version"]
    hvd_version = dlrs[os]["horovod"]["version"]
    torch_version = dlrs[os]["pytorch"]["mkl"]["version"]
    pkg_installer = "apt-get install -y" if os == "ubuntu" else "swupd bundle-add"
    kwargs = {
        "os": "{}:{}".format(os, os_version),
        "pkg_install": "{} {}".format(pkg_installer, " ".join(pkgs)),
        "tf_version": tf_version,
        "hvd_version": hvd_version,
        "torch_version": torch_version,
    }
    dockerfile_template = concat_slices(framework)
    dockerfile = insert_template_values(dockerfile_template, kwargs)
    write_to_file(file_name, dockerfile)


def generate_all_dockerfiles(generate: bool = True, build: bool = False) -> None:
    """generate all dockerfiles for all frameworks and OSes"""
    if generate:
        base_dir = "./dockerfiles"
        for framework in ["pytorch", "tensorflow"]:
            for _os in ["ubuntu", "clearlinux"]:
                save_to_dir = mkdir_p(os.path.join(base_dir, _os, framework))
                save_to_file = os.path.join(save_to_dir, "Dockerfile")
                generate_dockerfile(_os, framework, save_to_file)
    if build:
        # TOOD(unrahul) build the dockerfiles
        pass
