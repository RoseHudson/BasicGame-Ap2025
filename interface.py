import tkinter as tk


class Interface:
    def __init__(self, taille_de_fenetre, details_initiaux):
        self.details_initiaux = details_initiaux
        self.fenetre = tk.Tk()
        self.fenetre.title(details_initiaux.nom)
        self.fenetre.geometry(taille_de_fenetre)

    def ajouter_message(self):
        message_initial = tk.Label(self.fenetre, text=self.details_initiaux.retourner_info(), font=('Arial', 14))
        message_initial.pack(expand=True)

        bouton_de_connexion = tk.Button(self.fenetre, text="Se connecter", command=self.fenetre_de_connexion)
        bouton_de_connexion.pack(pady=5)
        bouton_insciption = tk.Button(self.fenetre, text="S'inscrire", command=self.fenetre_inscription)
        bouton_insciption.pack(pady=5)

        
    def fenetre_de_connexion(self):
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        message_de_connexion = tk.Label(self.fenetre, text="Veuillez entrer vos informations de connexion", font=('Arial', 14))
        message_de_connexion.pack(pady=10)

        etiquette_nom = tk.Label(self.fenetre, text="Nom d'utilisateur:")
        etiquette_nom.pack(pady=2)  
        entrez_nom = tk.Entry(self.fenetre, width=30)
        entrez_nom.pack(pady=2)

        etiquette_pass = tk.Label(self.fenetre, text="Mot de passe: ")
        etiquette_pass.pack(pady=2)
        entrez_pass = tk.Entry(self.fenetre, width=30, show="*")
        entrez_pass.pack(pady=2)

        bouton_de_connexion = tk.Button(self.fenetre, text="Se connecter", command=self.message_de_connexion)
        bouton_de_connexion.pack(pady=5)

    def fenetre_inscription(self):
        for widget in self.fenetre.winfo_children():
            widget.destroy()

        message_inscription = tk.Label(self.fenetre, text="Veuillez saisir vos informations pour vous inscrire à votre compte Battle Bots", font=('Arial', 14))
        message_inscription.pack(pady=10)

        etiquette_nom = tk.Label(self.fenetre, text="Nom d'utilisateur:")
        etiquette_nom.pack(pady=2)  
        entrez_nom = tk.Entry(self.fenetre, width=30)
        entrez_nom.pack(pady=2)

        etiquette_nom = tk.Label(self.fenetre, text="Nom d'utilisateur:")
        etiquette_nom.pack(pady=2)  
        entrez_nom = tk.Entry(self.fenetre, width=30)
        entrez_nom.pack(pady=2)

        etiquette_nom = tk.Label(self.fenetre, text="Nom d'utilisateur:")
        etiquette_nom.pack(pady=2)  
        entrez_nom = tk.Entry(self.fenetre, width=30)
        entrez_nom.pack(pady=2)

        etiquette_pass = tk.Label(self.fenetre, text="Mot de passe: ")
        etiquette_pass.pack(pady=2)
        entrez_pass = tk.Entry(self.fenetre, width=30, show="*")
        entrez_pass.pack(pady=2)

        bouton_de_connexion = tk.Button(self.fenetre, text="Se connecter", command=self.message_de_connexion)
        bouton_de_connexion.pack(pady=5)

    def message_de_connexion(self):
        print("Bouton de connexion cliqué")

    def message_inscription(self):
        print("bouton d'inscription cliqué")
        
    def gerer_le_jeu(self):
        self.fenetre.mainloop()