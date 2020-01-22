=======
stacker
=======


Tool to generate Dockerfiles from templates and scripts for stacks.


* Free software: MIT license


Features
--------

- parse spec file - DONE
- parse slices of dockerfiles per app - DONE
- update dockerfile based on the yaml file values - DONE
- generate combined dockerfile - DONE
- convert dockerfiles to singularity recepies 

 **TODO**
- assemble dockerfiles from slices
- lint dockerfiles

- build images
- resize images


Core principles
---------------

- Maintainable and upgradable solution
- Use Spec files to define configuaration values
- Use Dockerfiles as templates which can accept substitution from the spec files
- Limit use of shell scripts/custom templates use Dockerfiles where possible
- Use official [Docker](https://github.com/docker/docker-py) and [Singularity](https://github.com/singularityhub/singularity-cli) clients where possible


