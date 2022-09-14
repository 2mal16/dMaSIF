ARG CUDA="10.2"
ARG CUDNN="7"

FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu18.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/3bf863cc.pub

RUN apt-get update -y \
    && apt-get install -y apt-utils git curl ca-certificates bzip2 cmake tree htop bmon iotop g++ \
    && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev wget

RUN cd / && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x /Miniconda3-latest-Linux-x86_64.sh \
    && /Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda \
    && rm /Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda/bin:$PATH

RUN /miniconda/bin/conda install -y conda-build \
    && /miniconda/bin/conda create -y --name py37 python=3.7 \
    && /miniconda/bin/conda clean -ya

ENV CONDA_DEFAULT_ENV=py37
ENV CONDA_PREFIX=/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

ENV PATH=/usr/local/cuda/bin:$PATH
ENV CPATH=/usr/local/cuda/include:$CPATH
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/usr/local/cuda/lib:$DYLD_LIBRARY_PATH

RUN pip install torch==1.6.0 && \
    pip install torch-cluster==1.5.8 -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-geometric==1.6.1 -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-scatter==2.0.5 -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-sparse==0.6.8 -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-spline-conv==1.2.0 -f https://data.pyg.org/whl/torch-1.6.0+cu102.html

RUN apt update && apt install -y nano gcc-8

ADD ./requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /var/run/sshd
RUN echo 'root:pw' | chpasswd
RUN sed -i 's/#*PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

ADD ssh_keys.tar.gz /tmp/
RUN tar xvfz /tmp/ssh_keys.tar.gz
RUN mkdir -p /root/.ssh \
    && mv /tmp/ssh_keys/authorized_keys /root/.ssh/authorized_keys \
    && chown root:root /root/.ssh/authorized_keys \
    && chmod 600 /root/.ssh/authorized_keys \
    && stat /root/.ssh/authorized_keys \
    && rm -rf /tmp/ssh_keys ssh_keys.tar.gz

RUN git clone https://github.com/FreyrS/dMaSIF.git

WORKDIR /dMaSIF

VOLUME dmasif

CMD [""]