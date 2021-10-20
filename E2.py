import pandas as pd
from typing import Dict, List

# Récupère les lignes et modifie les noms des colonnes
def get_lignes(chemin: str) -> pd.DataFrame:
    data = pd.read_excel(chemin)
    data = data.drop(columns=['Identifiant', 'Famille commerciale'])
    data = data.rename(columns={
        "Nom court": "nom_ligne",
        "Nom long": "chemin"
    })
    lignes = data.values.tolist()
    return lignes

# Récupère les arrêts et modifie les noms des colonnes
def get_arrets(chemin: str) -> pd.DataFrame:
    data = pd.read_csv(chemin)
    data = data.drop(columns=["Ligne (ID)", "Ordre", "Montée autorisée", "Descente autorisée", "Parcours (libellé court)"])
    data = data.rename(columns={
        "Parcours (ID)": "id_parcours",
        "Ligne (nom court)": "nom_ligne",
        "Point d'arrêt (ID)": "id_arret",
        "Point d'arrêt (nom)": "nom_arret",
        "Nombre personne": "nb_personne"
    })
    return data

# Formatte le dataframe fournit comme voulu par l'exercice
def format_lignes(lignes: List[List[str]]) -> List[Dict]:
    results = []
    for ligne in lignes:
        arrets = ligne[1].split("<>")
        results.append({
            "nom_ligne": ligne[0],
            "premier_arret": arrets[0].strip(),
            "dernier_arret": arrets[-1].strip()
        })
    
    return results

# Formatte le dataframe fournit comme voulu par l'exercice
def format_arrets(arrets: List[List[str]]) -> List[Dict]:
    results = []
    for arret in arrets:
        results.append({
            "id_parcours": arret[0],
            "nom_ligne": arret[1],
            "id_arret": arret[2],
            "nom_arret": arret[3],
            "nb_personne": arret[4]        
        })

    return results

# Retourne la liste des noms des arrêts d'une ligne donnée
def get_liste_arrets(nom_ligne: str) -> List[str]:
    # Préparation de la donnée
    data = get_arrets('DOCS/nomArret.csv')
    data = format_arrets(data)

    results = []
    for d in data:
        if d['nom_ligne'] == nom_ligne:
            results.append(d['nom_arret'])

    print(results)


# Formatte les données pour min et max
def get_stats_arrets(nom_ligne: str, arrets: pd.DataFrame):
    arrets_by_ligne = arrets[arrets.nom_ligne == nom_ligne]
    arret_min = arrets_by_ligne.loc[arrets_by_ligne.nb_personne == arrets_by_ligne.nb_personne.min()]
    arret_max = arrets_by_ligne.loc[arrets_by_ligne.nb_personne == arrets_by_ligne.nb_personne.max()]
    return arret_max, arret_min, arrets_by_ligne

if __name__ == '__main__':
    ligne = input('Entrez un numéro de ligne : ')
    arrets = get_arrets('DOCS/nomArret.csv')
    arret_max, arret_min, arrets_list = get_stats_arrets(ligne, arrets)
    arret_max, arret_min, arrets_list = arret_max.values.tolist(), arret_min.values.tolist(), arrets_list.values.tolist()

    print(f"Liste d'arrêts : {format_arrets(arrets_list)}")
    print(f"Minimum : {format_arrets(arret_min)}")
    print(f"Maximum : {format_arrets(arret_max)}")