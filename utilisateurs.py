# user.py
from base_d import connect

def ajouter_utilisateur(nom, mot_de_passe):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO utilisateurs (nom, mot_de_passe) VALUES (?, ?)', (nom, mot_de_passe))
    conn.commit()
    conn.close()

def supprimer_utilisateur_par_nom(nom):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM utilisateurs WHERE nom = ?', (nom,))
    conn.commit()
    conn.close()

def rechercher_id_utilisateur(nom, mot_de_passe):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM utilisateurs WHERE nom = ? AND mot_de_passe = ?', (nom, mot_de_passe))
    utilisateur = cursor.fetchone()
    conn.close()

    if utilisateur is None:
        print("Utilisateur non trouvé ou mot de passe incorrect.")
        return None
    else:
        return utilisateur[0]
