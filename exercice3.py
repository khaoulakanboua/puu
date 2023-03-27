class CompteBancaire :
    
      def __init__(self,nom_titulaire,solde):
        self.nom_titulaire=nom_titulaire
        self.solde=solde
      def depot(self,montant) :
        self.solde+=montant
      def retrait(self,montant) :
        if self.solde < montant:
         print("solde insuffisant")
        else:
         self.solde-=montant
      def affiche_solde(self) :
        print(f"le solde du compte de {self.nom_titulaire} est de : {self.solde}")
           
compte=CompteBancaire("Khaoula",100)
compte.depot(100)
compte.retrait(200)
compte.affiche_solde()
