import sqlite3

def connect():
    return sqlite3.connect('ma_base_de_donnees.db')

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            mot_de_passe TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS villes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilisateurs_villes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            utilisateur_id INTEGER,
            ville_id INTEGER,
            FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id),
            FOREIGN KEY (ville_id) REFERENCES villes(id)
        )
    ''')
    
    conn.commit()
    conn.close()

from base_d import connect, create_tables
from utilisateurs import ajouter_utilisateur, supprimer_utilisateur_par_nom, rechercher_id_utilisateur
from villes import ajouter_ville_utilisateur, supprimer_ville_utilisateur, afficher_villes_utilisateur
from meteo import obtenir_meteo_ville

create_tables()

def afficher_message_accueil():
    print("=======================================")
    print("      Bienvenue dans l'App Météo      ")
    print("=======================================")

afficher_message_accueil()

choix = int(input("\nSaisir :\n1 - Utiliser sans vous connecter\n2 - Se connecter\nVotre choix : "))

if choix == 1:
    while True:
        ville = input("\nSaisir le nom de la ville :\nou 'arret' pour arrêter le programme : ").strip().lower()
        if ville != "arret":
            obtenir_meteo_ville(ville, "b9fc7ccd767c8f02d78333045699b865")
        else:
            exit()

elif choix == 2:
    choix2 = int(input("\nVoulez-vous :\n1 - Vous connecter\n2 - Créer un nouveau compte\nVotre choix : "))
    
    if choix2 == 1:
        j = 0
        while j == 0:
            nom = input("\nSaisir votre nom : ")
            mot_de_passe = input("Saisir votre mot de passe : ")
            u_id = rechercher_id_utilisateur(nom, mot_de_passe)
            if u_id is not None:
                j = 1
            else:
                print("\nUtilisateur non trouvé ou mot de passe incorrect, veuillez réessayer.")
                
    elif choix2 == 2:
        nom = input("\nSaisir votre nom : ")
        mot_de_passe = input("Saisir votre mot de passe : ")
        ajouter_utilisateur(nom, mot_de_passe)
        print("\nCompte créé avec succès.")
        u_id = rechercher_id_utilisateur(nom, mot_de_passe)
    
    
    choice = input(f"\nSaisir :\nRecherche - Rechercher la météo d'une ville\nAjout - Ajouter une ville parmi celles enregistrées par {nom}\nSuppression - Supprimer une ville parmi celles enregistrées par {nom}\nAffichage - Afficher la météo de toutes les villes enregistrées par {nom}\nArret - Arrêter le programme\nVotre choix : ").lower()
        
    while choice in ["recherche", "ajout", "suppression", "affichage", "arret"]:
        if choice == "recherche":
            ville = input("\nSaisir le nom de la ville à rechercher : ").lower()
            obtenir_meteo_ville(ville, "b9fc7ccd767c8f02d78333045699b865")
        
        elif choice == "ajout":
            ville = input("\nSaisir le nom de la ville à ajouter : ").lower()
            if ajouter_ville_utilisateur(u_id, ville) == 1:
                print(f"\nLa ville '{ville}' a été ajoutée avec succès.")
            else:
                print(f"\nLa ville '{ville}' existe déjà.")    
        
        elif choice == "suppression":
            ville = input("\nSaisir le nom de la ville à supprimer : ").lower()
            supprimer_ville_utilisateur(u_id, ville)
    
        elif choice == "affichage":
            a = afficher_villes_utilisateur(u_id)
            if a is None:
                print("\nAucune ville enregistrée.")
            else:
                obtenir_meteo_ville(a, "b9fc7ccd767c8f02d78333045699b865")
        
        elif choice == "arret":
            exit()
        else:
            print("\nErreur de saisie. Veuillez réessayer.")    
            
        choice = input(f"\nSaisir :\nRecherche - Rechercher la météo d'une ville\nAjout - Ajouter une ville parmi celles enregistrées par {nom}\nSuppression - Supprimer une ville parmi celles enregistrées par {nom}\nAffichage - Afficher la météo de toutes les villes enregistrées par {nom}\nArret - Arrêter le programme\nVotre choix : ").lower()    
