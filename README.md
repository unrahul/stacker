### stacker

A python based tool to **generate** Dockerfiles, lint and possibly build optimized docker images. In future phases write a parser / generator to convert the dockerfiles to singularity recipie file.

## Core principles

- Maintainable and upgradable solution
- Use Spec files to define configuaration values
- Use Dockerfiles as templates which can accept substitution from the spec files
- Limit use of shell scripts/custom templates use Dockerfiles where possible
- Use official [Docker](https://github.com/docker/docker-py) and [Singularity](https://github.com/singularityhub/singularity-cli) clients where possible


