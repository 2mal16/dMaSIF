ARG CUDA="11.3.1"
ARG CUDNN="8"

FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu18.04

ARG CUDA

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/3bf863cc.pub

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    build-essential \
    apt-utils \
    tmux \
    git \
    curl \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    libxml2-dev \
    zip \
    bzip2 \
    cmake \
    tree \
    htop \
    bmon \
    iotop \
    g++ \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    make \
    nano \
    gcc-8 \
    openssh-server \
    libssl-dev \
    libcurl4-openssl-dev

RUN cd / && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x /Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda \
    && rm /Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda/bin:$PATH

RUN /miniconda/bin/conda install -y conda-build \
    && /miniconda/bin/conda create -y --name py37 python=3.7 \
    && /miniconda/bin/conda clean -ya

ENV CONDA_DEFAULT_ENV=py37
ENV CONDA_PREFIX=/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

ENV PATH=/usr/local/cuda-${CUDA}/bin:$PATH
ENV CPATH=/usr/local/cuda-${CUDA}/include:$CPATH
ENV LD_LIBRARY_PATH=/usr/local/cuda-${CUDA}/lib64:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/usr/local/cuda-${CUDA}/lib:$DYLD_LIBRARY_PATH

RUN pip install torch==1.10.2 --extra-index-url https://download.pytorch.org/whl/cu113 &&\
    pip install torch-cluster==1.5.9 -f https://data.pyg.org/whl/torch-1.10.2+cu113.html && \
    pip install torch-geometric==1.7.2 -f https://data.pyg.org/whl/torch-1.12.0+cu113.html &&\
    pip install torch-scatter==2.0.9 -f https://data.pyg.org/whl/torch-1.10.2+cu113.html && \
    pip install torch-sparse==0.6.12 -f https://data.pyg.org/whl/torch-1.10.2+cu113.html && \
    pip install torch-spline-conv==1.2.1 -f https://data.pyg.org/whl/torch-1.10.2+cu113.html


ARG DMASIF_REPO_PATH=docker/dmasif
WORKDIR /tmp
COPY ${DMASIF_REPO_PATH}/requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
RUN git clone https://github.com/rlabduke/reduce.git
WORKDIR reduce
RUN make install

RUN mkdir /app
WORKDIR /app

RUN git clone https://github.com/casperg92/MaSIF_colab.git
RUN git clone https://github.com/2mal16/dMaSIF.git
WORKDIR dMaSIF

COPY ${DMASIF_REPO_PATH}/docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

CMD ["python main_inference.py --pdb_list ${PDB_LIST_PATH}"]
