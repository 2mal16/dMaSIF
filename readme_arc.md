# How to build the image
	docker build -t dmasif:dmasif .

# How to run the container
	docker run --gpus all -it -v /home/geoten/codes/dMaSIF:/dMaSIF 42c bash
                                   
