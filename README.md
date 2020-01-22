## stacker


A rough prototype for a tool to generate Dockerfiles from templates and scripts for stacks. Be careful, there are rough edges!

### Usage

- clone the github repo to your local, cd to  stacker/stacker/
- For now, use the following command to generate dockerfiles

```bash
python stacker.py --generate 
```
This command will generate all possible dockerfiles for all OSes and frameworks as defined in the spec file.

### Core components


- specs/dlrs.yaml

A loosely defined specification file

```yaml

---
version: "0.6.0"
description: "Deep Learning Reference Stack"
license: |
  # SPDX-License-Identifier: MIT
  # Copyright (c) 2019 Intel Corporation

stack:
  dlrs:
    version: "0.6.0"
    tag: dlrs
    ubuntu:
      version: "18.10"
      tag: ubuntu
      os_pkgs:
        - openssh-server
        - openssh-client
        - wget
        - curl
        - python37
      python:

```
- slices/<component>.dockerfile

Each component is defined as dockerfiles templates

Eg. A tensorflow dockerfile cane be something like:

```dockerfile
RUN pip install tensorflow=={{tf_version}}
```

here `{{tf_version}}` is a variable that would be dynamically injected
from the spec file value `spec.stack.dlrs.ubuntu.tensorflow.version`

Another template is for the OS

```dockerfile
FROM {{os}}
RUN {{pkg_install}}  
```

Here there are 2 place holder variables `{{os}}` and `{{pkg_install}}`
Again, OS and system packages would be injected dynamically based on the spec file

### Features

- parse spec file - DONE
- parse slices of dockerfiles per app - DONE
- update dockerfile based on the yaml file values - DONE
- enable elementary cli support - DONE

 **TODO**

- give option to build dockerimages from generated dockerfiles
- convert dockerfiles to singularity recepies
- lint dockerfiles
- resize images

### Core principles

- Maintainable and upgradable solution
- Use Spec files to define configuaration values
- Use Dockerfiles as templates which can accept substitution from the spec files
- Limit use of shell scripts/custom templates use Dockerfiles where possible
- Use official [Docker](https://github.com/docker/docker-py) and [Singularity](https://github.com/singularityhub/singularity-cli) clients where possible


