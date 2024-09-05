from base_d import connect
import requests

def rech_ville_uti(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT villes.id, villes.nom
        FROM villes
        INNER JOIN utilisateurs_villes ON villes.id = utilisateurs_villes.ville_id
        WHERE utilisateurs_villes.utilisateur_id = ? AND villes.nom = ?
    ''', (utilisateur_id, nom_ville))
    
    villes = cursor.fetchall()
    conn.close()
    
    if len(villes) == 0:  
        return False
    else:
        return True

def ajouter_ville_utilisateur(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id FROM villes WHERE nom = ?', (nom_ville,))
        ville = cursor.fetchone()

        if not rech_ville_uti(utilisateur_id, nom_ville):
            if ville is None:
                cursor.execute('INSERT INTO villes (nom) VALUES (?)', (nom_ville,))
                ville_id = cursor.lastrowid
            else:
                ville_id = ville[0]

            cursor.execute('INSERT INTO utilisateurs_villes (utilisateur_id, ville_id) VALUES (?, ?)', (utilisateur_id, ville_id))
            conn.commit()
            print(f"\nLa ville '{nom_ville}' a été ajoutée avec succès.")
            return 1
        else:
            print(f"\nLa ville '{nom_ville}' est déjà enregistrée pour cet utilisateur.")
            return 0
    finally:
        conn.close()

def supprimer_ville_utilisateur(utilisateur_id, nom_ville):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM villes WHERE nom = ?', (nom_ville,))
    ville = cursor.fetchone()

    if ville is not None:
        ville_id = ville[0]
        cursor.execute('DELETE FROM utilisateurs_villes WHERE utilisateur_id = ? AND ville_id = ?', (utilisateur_id, ville_id))
        conn.commit()
        print(f"\nLa ville '{nom_ville}' a été supprimée de l'utilisateur.")
    else:
        print(f"\nLa ville '{nom_ville}' n'existe pas.")

    conn.close()

def afficher_villes_utilisateur(utilisateur_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT villes.id, villes.nom
        FROM villes
        INNER JOIN utilisateurs_villes ON villes.id = utilisateurs_villes.ville_id
        WHERE utilisateurs_villes.utilisateur_id = ?
    ''', (utilisateur_id,))
    
    villes = cursor.fetchall()
    conn.close()
    
    if villes == []:
        print("\nAucune ville enregistrée.")
        return None

    print("\nVilles enregistrées :")
    for i in range(len(villes)):
        print(f"{i + 1}: {villes[i][1]}")
    
    choix = int(input("Saisir le numéro de la ville pour voir la météo : "))
    nom_ville = villes[choix - 1][1]

    return nom_ville