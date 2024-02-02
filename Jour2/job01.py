import mysql.connector

# Paramètres de connexion à la base de données
db_config = {
    'user': 'root',  # Remplacez par votre nom d'utilisateur MySQL
    'password': 'Pompom42650',  # Remplacez par votre mot de passe MySQL
    'host': 'localhost',
    'database': 'LaPlateforme'
}

# Connexion à la base de données
try:
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Requête pour récupérer tous les étudiants
    query = 'SELECT * FROM etudiant'

    # Exécution de la requête
    cursor.execute(query)

    # Affichage des résultats
    for (id, nom, prenom, age, email) in cursor:
        print(f'ID: {id}, Nom: {nom}, Prénom: {prenom}, Âge: {age}, Email: {email}')

    cursor.close()
    db.close()
    
except mysql.connector.Error as err:
    print(err)