print("Bonjour, comment vous appelez-vous ?")
prenom = input()
print("Enchanté", prenom )

print("Votre bien est-il neuf ?")
neuf = input()

if (neuf == "oui"):
  print("Avez-vous acheté votre bien il y a moins de deux ans ?")

  date = input()

  if (date == "oui"):
    print("Vous pouvez faire jouer votre garantie")

elif (neuf =="non"):
  print("désolé vous ne pouvez pas faire jouer la garantie !")

else:
  print("pas compris ")




