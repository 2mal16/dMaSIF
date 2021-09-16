ARG CUDA="10.2"
ARG CUDNN="7"

FROM nvidia/cuda:${CUDA}-cudnn${CUDNN}-devel-ubuntu16.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# install basics
RUN apt-get update -y \
    && apt-get install -y apt-utils git curl ca-certificates bzip2 cmake tree htop bmon iotop g++ \
    && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev wget 

# Install Miniconda
RUN cd / && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x /Miniconda3-latest-Linux-x86_64.sh \
    && /Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda \
    && rm /Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/miniconda/bin:$PATH

# Create a Python 3.6 environment
RUN /miniconda/bin/conda install -y conda-build \
    && /miniconda/bin/conda create -y --name py37 python=3.7 \
    && /miniconda/bin/conda clean -ya

ENV CONDA_DEFAULT_ENV=py37
ENV CONDA_PREFIX=/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

# set cuda path 
ENV PATH=/usr/local/cuda/bin:$PATH
ENV CPATH=/usr/local/cuda/include:$CPATH
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
ENV DYLD_LIBRARY_PATH=/usr/local/cuda/lib:$DYLD_LIBRARY_PATH

# install pytorch
# RUN pip install torch==1.6.0+cu102 && pip install torch-cluster==1.5.8+cu102 && \
#     pip install torch-geometric==1.6.1+cu102 && pip install torch-scatter==2.0.5+cu102 && \
#     pip install torch-sparse==0.6.8+cu102 && pip install torch-spline-conv==1.2.0+cu102

# alternatively install pytorch
RUN pip install torch -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-cluster -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-geometric -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-scatter -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-sparse -f https://data.pyg.org/whl/torch-1.6.0+cu102.html && \
    pip install torch-spline-conv -f https://data.pyg.org/whl/torch-1.6.0+cu102.html

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

# Install dependancies
RUN pip install -r requirements.txt


CMD [""]
# Execute the dockerfile building command on terminal
# sudo docker build -t gioannak:dmasif .
