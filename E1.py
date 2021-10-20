# num_Ligne = str
# nom_Ligne = str
# liste_Arret = list[]
# nb_Personne = decimal

import xlrd
import csv
import pandas as pd

def get_data():
    # Récupèration des données de l'utilisateur
    print('Entrez le numéro de la ligne')
    num_Ligne = input()

    print('Entrez le nom de l\'arrêt')
    nom_Arret = input()

    # Récupérations des dataframes sur les fichiers
    doc_lignes = pd.read_excel('DOCS\listeLignes.xlsx')
    doc_arrets = pd.read_csv('DOCS/nomArret.csv')

    # Récupération des informations sur la ligne que l'utilisateur a demandé
    C4 = doc_lignes.loc[doc_lignes["Nom court"] == num_Ligne]
    print(C4)

    # Récupération des arrêts de la ligne
    C4_lignes = doc_arrets.loc[doc_arrets["Ligne (nom court)"] == num_Ligne]

    # Affichage des arrêts de la ligne avec le plus et le moins de personnes
    print(C4_lignes.max())
    print(C4_lignes.min())


if __name__ == '__main__':
    get_data()