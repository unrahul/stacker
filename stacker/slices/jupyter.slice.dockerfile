FROM stacks-clearlinux/stacks-clearlinux
ENV VERSION=2.1.0

RUN swupd bundle-add python-basic
RUN pip install jupyterlab