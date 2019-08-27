#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rdkit.Chem import SDMolSupplier
from whales_descriptors import do_whales, gen_conf

# load precalculated conformers from an SD file
molfile = 'mols.sdf'
mols1 = [m for m in SDMolSupplier(molfile)]

# you can also generate conformers from SMILES strings
smls = ['Cc1nc(-c2ccc(NC(=O)c3ccco3)cc2)cs1',
        'NC(=O)c1ccc(NC(=O)C2CCN(S(=O)(=O)Cc3ccccc3)CC2)cc1',
        'CC(=O)Nc1ccc(C(=O)CSc2nnc(-c3ccccc3)n2-c2ccccc2)cc1']
mols2 = [gen_conf.main(s) for s in smls]

# combine both sources
mols = mols1 + mols2

# calculate descriptors from the supplier molecules
x, labels = do_whales.main(mols, charge_threshold=0, do_charge=True, property_name='')
x.columns = labels
x.describe()
