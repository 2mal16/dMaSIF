ARG CUDA="10.2"
ARG CUDNN="7"

FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu18.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

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

RUN git clone https://github.com/FreyrS/dMaSIF.git
WORKDIR /dMaSIF

RUN sed -i "s/torch==1.6.0//g" requirements.txt && \
    sed -i "s/torch-cluster==1.5.8//g" requirements.txt && \
    sed -i "s/torch-geometric==1.6.1//g" requirements.txt && \
    sed -i "s/torch-scatter==2.0.5//g" requirements.txt && \
    sed -i "s/torch-sparse==0.6.8//g" requirements.txt && \
    sed -i "s/torch-spline-conv==1.2.0//g" requirements.txt && \
    sed -i "/^$/d" requirements.txt

RUN apt update && apt install -y vim

RUN apt update && apt install -y gcc-8

RUN pip install -r requirements.txt

VOLUME dmasif

CMD [""]