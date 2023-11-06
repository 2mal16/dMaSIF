#!/usr/bin/env bash

set -e

cd data_preprocessing
mkdir -p tmp pdbs npys
if [[ -z "${DMASIF_PDB_LIST}" ]]; then
  DMASIF_PDB_LIST="pdb_dmasif_list_train.txt"
else
  DMASIF_PDB_LIST="${DMASIF_PDB_LIST}"
fi

echo ${DMASIF_PDB_LIST}

python download_pdb.py --pdb_list /inputs/${DMASIF_PDB_LIST}
# python download_pdb.py --pdb_list /inputs/pdb_dmasif_list_train.txt
cd ..
cp -r /app/MaSIF_colab/models/* /app/dMaSIF/models/
# python -W ignore -u main_training.py --experiment_name dMaSIF_site_3layer_16dims_9A_100sup_epoch64 --pdb_list /inputs/pdb_masif_list.txt --batch_size 64 --embedding_layer dMaSIF --site True --single_protein True --random_rotation True --radius 9.0 --n_layers 3
python -W ignore -u main_inference.py --experiment_name dMaSIF_site_3layer_16dims_9A_100sup_epoch64 --site True --embedding_layer dMaSIF --emb_dims 16 --radius 9.0 --n_layers 3 --pdb_list /inputs/${DMASIF_PDB_LIST} --single_protein True
# python -W ignore -u main_inference.py --experiment_name dMaSIF_site_3layer_16dims_9A_100sup_epoch64 --site True --embedding_layer dMaSIF --emb_dims 16 --radius 9.0 --n_layers 3 --pdb_list /inputs/pdb_masif_list_train.txt --single_protein True

