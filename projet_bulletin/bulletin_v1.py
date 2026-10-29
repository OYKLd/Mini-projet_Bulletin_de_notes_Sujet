# Projet : Bulletin de notes d'un étudiant - Itération v1
# Auteur : Lydie Ouattara
# Date : 29/10/2026
# Description : demande le nom et une note, puis affiche cette note multipliée par son coefficient.

# Coefficient de la matière (rangé dans une variable explicite)
coef_python = 3

# Saisies de l'utilisateur
nom_etudiant = input("Nom de l'étudiant : ")
note_python = float(input("Note de Python (/20) : "))  # conversion texte -> nombre

# Calcul de la note pondérée
note_ponderee = note_python * coef_python

# Affichage du résultat
print(f"{nom_etudiant} : {note_python} x coef {coef_python} = {note_ponderee}")
