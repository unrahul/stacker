from parser import spec
from pathlib import Path

from jinja2 import Template

docker_templates = {}
path = Path.cwd().joinpath("slices")
for file in path.iterdir():
    print(file)
    docker_templates[file.name] = file.read_text()

dockerfile = ""
os = "ubuntu"
framework = "tensorflow"
dlrs = spec["stack"]["dlrs"]
if os == "ubuntu":
    os_version = dlrs[os]["version"]
    pkgs = dlrs[os]["apt"]
    tf_version = dlrs[os]["tensorflow"]["mkl"]["version"]
    hvd_version = dlrs[os]["horovod"]["version"]
    torch_version = dlrs[os]["pytorch"]["mkl"]["version"]
if framework == "tensorflow":
    dockerfile = (
        docker_templates["os.slice.dockerfile"]
        + "\n\n"
        + docker_templates["tensorflow.dockerfile"]
    )

dockerfile = Template(dockerfile)
dockerfile = dockerfile.render(
    os="{}:{}".format(os, os_version),
    pkg_install="apt-get install -y {}".format(",".join(pkgs)),
    version=tf_version,
)
print(dockerfile)
