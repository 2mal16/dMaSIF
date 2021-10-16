import pymol
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--namemol2','-mol2', help="provide the name of the mol2 file",type=str, default='1.mol2')
	args = parser.parse_args()



	pymol.finish_launching()
	pdb_file =args.namemol2
	pdb_name ="my_pdb"
	pymol.cmd.load(pdb_file, pdb_name)
	pymol.cmd.disable("all")
	pymol.cmd.enable(pdb_name)

	pymol.cmd.save("olala.pdb")

	pymol.cmd.quit()