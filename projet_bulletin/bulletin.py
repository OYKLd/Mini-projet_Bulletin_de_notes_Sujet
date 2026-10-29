# Projet : Bulletin de notes d'un étudiant (itération v3, version finale)
# Auteur : Lydie Ouattara
# Date : 29/10/2026
# Description : lit le nom et les trois notes d'un étudiant, puis affiche
#               son bulletin avec la moyenne pondérée.

# --- Coefficients de chaque matière ---
coef_algo = 2
coef_python = 3
coef_methodo = 1

# --- Saisies de l'utilisateur (notes converties en float) ---
nom_etudiant = input("Nom de l'étudiant : ")
note_algo = float(input("Note d'Algorithmique (/20) : "))
note_python = float(input("Note de Python (/20) : "))
note_methodo = float(input("Note de Méthodologie (/20) : "))

# --- Calcul de la moyenne pondérée ---
somme_ponderee = note_algo * coef_algo + note_python * coef_python + note_methodo * coef_methodo
somme_coef = coef_algo + coef_python + coef_methodo
moyenne = somme_ponderee / somme_coef

# --- Affichage du bulletin ---
print()
print("===== BULLETIN DE NOTES =====")
print(f"Étudiant : {nom_etudiant}")
print(f"Algorithmique (coef {coef_algo}) : {note_algo}")
print(f"Python (coef {coef_python}) : {note_python}")
print(f"Méthodologie (coef {coef_methodo}) : {note_methodo}")
print("-----------------------------")
print(f"Moyenne pondérée : {moyenne}")
