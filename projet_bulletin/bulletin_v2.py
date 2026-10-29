# Projet : Bulletin de notes d'un étudiant - Itération v2
# Auteur : Lydie Ouattara
# Date : 29/10/2026
# Description : demande les trois notes et affiche la moyenne pondérée.

# Coefficients de chaque matière
coef_algo = 2
coef_python = 3
coef_methodo = 1

# Saisies de l'utilisateur (conversion en nombres décimaux)
nom_etudiant = input("Nom de l'étudiant : ")
note_algo = float(input("Note d'Algorithmique (/20) : "))
note_python = float(input("Note de Python (/20) : "))
note_methodo = float(input("Note de Méthodologie (/20) : "))

# Moyenne pondérée = somme(note x coef) / somme(coef)
somme_ponderee = note_algo * coef_algo + note_python * coef_python + note_methodo * coef_methodo
somme_coef = coef_algo + coef_python + coef_methodo
moyenne = somme_ponderee / somme_coef

# Affichage du résultat
print(f"Moyenne pondérée de {nom_etudiant} : {moyenne}")
