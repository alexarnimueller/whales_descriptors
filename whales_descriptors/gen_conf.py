from rdkit.Chem import AddHs, RemoveHs, AllChem, MolFromSmiles


def main(smls, seed=42):
    """ Embed a molecule in 3D from a given SMILES string

    :param smls: {str} molecule as SMILES
    :param seed: {int} random seed to use for initialization
    :return: embeded RDKit molecule
    """
    try:
        m = MolFromSmiles(smls)
        m2 = AddHs(m)
        AllChem.EmbedMolecule(m2, useBasicKnowledge=True, maxAttempts=50, randomSeed=seed)
        AllChem.MMFFOptimizeMolecule(m2)
        return RemoveHs(m2)
    except ValueError:
        return None
    except TypeError:
        return None
