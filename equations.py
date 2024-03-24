
         ##TP DE MATHS DU GROUPE 1

import tkinter as tk
from fractions import Fraction

def gauss_solver(systeme, m, n):
    # Vérifier si le système contient des équations identiques
    for i in range(m):
        for j in range(i+1, m):
            if all(systeme[i][k] == systeme[j][k] for k in range(n+1)):
                raise ValueError("Le système contient des équations identiques.")

    for i in range(m):
        # Si le pivot est nul, on permute les lignes
        if systeme[i][i] == 0:
            for j in range(i+1, m):
                if systeme[j][i] != 0:
                    systeme[i], systeme[j] = systeme[j], systeme[i]
                    break
            else:
                raise ValueError("Le système est indéterminé.")
        
        for j in range(i+1, m):
            ratio = systeme[j][i] / systeme[i][i]
            for k in range(n+1):
                systeme[j][k] -= ratio * systeme[i][k]

    # Vérifier si le système a une infinité de solutions
    for i in range(m):
        if all(coef == 0 for coef in systeme[i][:n]) and systeme[i][n] != 0:
            raise ValueError("Le système n'a pas de solution.")
        elif all(coef == 0 for coef in systeme[i]):
            return "infinité de solutions"
            # Si le nombre d'équations est inférieur au nombre d'inconnues
    if m < n:
        return "infinité de solutions"

    solution = [0] * n
    for i in range(m-1, -1, -1):
        solution[i] = systeme[i][n] / systeme[i][i]
        for j in range(i-1, -1, -1):
            systeme[j][n] -= systeme[j][i] * solution[i]

    return solution

def solve_systeme():
    systeme = []
    for i in range(m):
        ligne = []
        for j in range(n+1):
            try:
                entree = entries[i][j].get()
                if '/' in entree:  # Vérifie si l'entrée est une fraction
                    entree = Fraction(entree)
                else:  # Si ce n'est pas une fraction, on suppose que c'est un entier
                    entree = int(entree)  # Convertit l'entrée en entier
                ligne.append(entree)
            except ValueError:  # Si la conversion en entier échoue, une erreur est levée
                afficher_erreur("Veuillez entrer uniquement des entiers ou des fractions.")
                return
        systeme.append(ligne)
    try:
        solution = gauss_solver(systeme, m, n)
        if solution == "infinité de solutions":
            label_text = tk.Label(root_equations, text="Le système a une infinité de solutions.")
            label_text.grid(row=m + 16 + n, column=0, columnspan=n+1)
        else:
            solution_row_start = m + 16 + n  
            label_text = tk.Label(root_equations, text="Les solutions de l'équation sont :")
            label_text.grid(row=solution_row_start - 1, column=0, columnspan=n+1)
            for i in range(n):
                label_resultat = tk.Label(root_equations, text=f'X{i+1} = {solution[i]}')
                label_resultat.grid(row=solution_row_start + i, column=0, columnspan=n+1)
    except ValueError as e:
        afficher_erreur(e)



def afficher_erreur(erreur):
    """Affiche l'erreur dans une nouvelle fenêtre."""
    root_erreur = tk.Tk()
    root_erreur.title("Erreur")
    root_erreur.geometry("400x100")

    label_erreur = tk.Label(root_erreur, text="Une erreur s'est produite lors de l'exécution du programme.")
    label_erreur.grid(row=0, column=0)

    label_erreur = tk.Label(root_erreur, text=str(erreur))
    label_erreur.grid(row=1, column=0)

    root_erreur.mainloop()

def get_m_n():
    global m, n
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        if m == 0 or n == 0:
            raise ValueError("Veuillez entrer des entiers différents de 0 !! ")
        if m < 0 or n <0:
            raise ValueError("Veuillez entrer des entiers positifs !!")
        afficher_equations()
    except ValueError as e:
        afficher_erreur(e)


def afficher_equations():
    global root_equations,entries
    root_equations = tk.Tk()
    root_equations.title("Equations")
    root_equations.geometry("700x300")
    entries = []
    for i in range(m):
        entries_ligne = []
        for j in range(n):
            entry = tk.Entry(root_equations, width=5)
            entry.grid(row=i+13, column=4*j, sticky='e')
            entries_ligne.append(entry)
            label_variable = tk.Label(root_equations, text=f'X{j+1}')
            label_variable.grid(row=i+13, column=4*j+1, sticky='w')
            if j < n-1:
                label_plus = tk.Label(root_equations, text=' +')
                label_plus.grid(row=i+13, column=4*j+2)
        label_egal = tk.Label(root_equations, text='=')
        label_egal.grid(row=i+13, column=4*n)  
        entry_constante = tk.Entry(root_equations, width=5)
        entry_constante.grid(row=i+13, column=4*n+1)  
        entries_ligne.append(entry_constante)
        entries.append(entries_ligne)
    bouton_resolution = tk.Button(root_equations, text="Résoudre", command=solve_systeme,bg='green')
    bouton_resolution.grid(row=m+15, column=1, columnspan=n+1)
    bouton_aide = tk.Button(root_equations, text="Aide", command=afficher_aide_2,bg = 'brown')
    bouton_aide.grid(row=0, column=0)
    #bouton_quitter = tk.Button(root_equations, text="Quitter", command=root_equations.quit,bg='red')
    #bouton_quitter.grid(row=m+15, column=3,columnspan=n+9)
    label_espacement = tk.Label(root, text="")
    label_espacement.grid(row=1)
    label_erreur.grid(row=m+8, column=0)
    label_espacement = tk.Label(root_equations, text="")
    label_espacement.grid(row=m+14)
    
    
#afficher l'aide dans la fenetre de resolution 
def afficher_aide_2():
  """Affiche l'aide dans une nouvelle fenêtre."""
  root_aide = tk.Tk()
  root_aide.title("Aide")
  root_aide.geometry("700x100")
  label_instruction_2 = tk.Label(root_aide, text="* Veuillez entrer les coefficients de chaque équation.")
  label_instruction_2.grid(row=0, column=0, sticky='w')
  label_instruction_3 = tk.Label(root_aide, text="* Par defaut , les cases vides prendront la valeurs 0.")
  label_instruction_3.grid(row=1, column=0, sticky='w')
  root_aide.mainloop()
    
def afficher_aide():
  """Affiche l'aide dans une nouvelle fenêtre."""
  root_aide = tk.Tk()
  root_aide.title("Aide")
  root_aide.geometry("700x100")

  label_aide = tk.Label(root_aide, text="Ce programme permet de résoudre des systèmes d'équations linéaires.")
  label_aide.grid(row=0, column=0)

  label_aide = tk.Label(root_aide, text="Pour utiliser le programme, vous devez entrer le nombre d'équations et le nombre de variables.")
  label_aide.grid(row=1, column=0)

  label_aide = tk.Label(root_aide, text="Une fois que vous avez entré ces informations, vous pouvez entrer les coefficients de chaque équation.")
  label_aide.grid(row=2, column=0)

  label_aide = tk.Label(root_aide, text="Le programme résoudra ensuite le système d'équations et affichera les solutions.")
  label_aide.grid(row=3, column=0)

  root_aide.mainloop()


root = tk.Tk()
root.title("Résolveur de systèmes d'équations linéaires")
root.geometry("900x400")

label_text = tk.Label(root,text = " BIENVENUE DANS LE RESOLVEUR DE SYSTEMES D'EQUATIONS LINEAIRES ")
label_text.grid(row=0,column=1)

label_espacement = tk.Label(root, text="")
label_espacement.grid(row=1)

# Ajout du label d'instruction
label_instruction = tk.Label(root, text="* Veuillez entrer le nombres d'equations et le nombres de variables de votre système.")
label_instruction.grid(row=2, column=1)

label_espacement = tk.Label(root, text="")
label_espacement.grid(row=3)

entry_m = tk.Entry(root)
entry_m.grid(row=4, column=1)

entry_n = tk.Entry(root)
entry_n.grid(row=5, column=1)

label_m = tk.Label(root, text="Nombre d'équations :")
label_m.grid(row=4, column=0)

label_n = tk.Label(root, text="Nombre de variables :")
label_n.grid(row=5, column=0)
   
label_espacement = tk.Label(root, text="")
label_espacement.grid(row=5)

label_espacement = tk.Label(root, text="")
label_espacement.grid(row=6)

bouton_m_n = tk.Button(root, text="Soumettre", command=get_m_n,bg='green')
bouton_m_n.grid(row=7, column=1)



bouton_quitter = tk.Button(root, text="Quitter", command=root.quit,bg='red')
bouton_quitter.grid(row=7, column=7)

label_espacement = tk.Label(root, text="")
label_espacement.grid(row=11)
m = n = 0
label_erreur = tk.Label(root, text="")

bouton_aide = tk.Button(root, text="Aide", command=afficher_aide,bg = 'brown')
bouton_aide.grid(row=0, column=0)

root.mainloop()

##TP DE MATHS DU GROUPE 1
