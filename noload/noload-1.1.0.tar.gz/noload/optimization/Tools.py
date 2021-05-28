# SPDX-FileCopyrightText: 2020 G2Elab / MAGE
#
# SPDX-License-Identifier: Apache-2.0

import autograd.numpy as np

'''Gestion des contraintes'''
class StructList:
    List = None # Liste regroupant l'ensemble des contraintes scalaires et/ou vectorielles
    shape = [] # liste regroupant les tailles des vecteurs des différentes contraintes (0 si scalaire, à partir de 1 si vectorielle)
    etat = '' # chaîne de caractères indiquant si la liste est déjà aplatie (flattened) ou non (unflattened)

    def __init__(self, List=[], etat='unflattened', shape=[]):
        sh = []
        self.List = List
        self.etat = etat
        if self.etat == 'unflattened': # si la liste n'est pas "aplatie"
            if len(self.List) == 1 and isinstance(self.List[0], (int, float)):  # cas : 1 contrainte scalaire
                shape = [0]
            else:
                for i in range(len(self.List)): # on parcourt les éléments de la liste des contraintes
                    if isinstance(self.List[i], (list, np.ndarray)): # si la contrainte est vectorielle
                        sh.append(len(self.List[i])) # on ajoute à la liste shape la longueur du vecteur de contraintes
                    else:                   # si la contrainte est scalaire
                        sh.append(0) # on ajoute un 0 (signe que la contrainte est scalaire)
                shape = sh
        self.shape = shape

    def flatten(self): # fonction pour "aplatir" une listes de contraintes complexes
        if len(self.List) == 1 and isinstance(self.List[0], (int, float)):  # cas : 1 contrainte scalaire
            return self.List
        res = []
        for i in range(len(self.List)): # on parcourt chaque type de contrainte dans la liste
            if isinstance(self.List[i], (list, np.ndarray)): # si la contrainte est vectorielle
                for j in range(len(self.List[i])): # pour chaque composante de cette contrainte vectorielle
                    res.append(self.List[i][j]) # on ajoute chaque composante au résultat final res
            else: # si la contrainte est scalaire
                res.append(self.List[i]) # on l'ajoute au résultat final res
        self.etat = 'flattened' # on change l'attribut état de la liste pour signifier qu'elle a été aplatie
        return res # on renvoie la liste aplatie

    def unflatten(self): # fonction pour "reformer" une liste de contraintes complexes "aplatie"
        res = []
        i = 0
        for size in self.shape: # on parcourt les éléments de "shape"
            if size == 0:  #si la contrainte est scalaire
                res.append(self.List[i])
                i = i + 1
            else: # si la contrainte est vectorielle
                res.append(self.List[i:i + size])
                i = i + size
        self.etat = 'unflattened' # on change l'attribut état de la liste pour signifier qu'elle a été "reformée"
        return res


if __name__ == "__main__":
    seq = [1, [1], [2,3], 4, [5, 6, 7], np.array([1, 2])] #, [[1], 2, [3, [4]]]]
    print("original:\t", seq)
    seq2 = StructList(seq)
    res = seq2.flatten()
    print("flattened:\t", res)
    print("shape:\t\t", seq2.shape)
    seq3 = StructList(res,'flattened',seq2.shape)
    res2 = seq3.unflatten()
    print("unflattened:", res2)
