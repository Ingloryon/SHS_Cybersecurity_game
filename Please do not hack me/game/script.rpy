# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define B = Character("Bob", color="#ff6633")
define B_shout = Character("Bob", color="#ff6633",what_size=54)
define Al = Character("Alice", color="#99ff33")
define Ad = Character("Andrew", color="#cc9900")
define G = Character("Gabriel", color="#0099ff")
define S = Character("Sarah", color="#6600ff")
define P = Character("Mrs.Parker", color="#660033")

#Scale Gabriel
image gabriel_angry= im.FactorScale("gabriel_angry.png", 0.25)
image gabriel_confused= im.FactorScale("gabriel_confused.png", 0.25)
image gabriel_cry= im.FactorScale("gabriel_cry.png", 0.25)
image Gabriel_flustered= im.FactorScale("Gabriel_flustered.png", 0.25)
image gabriel_happy= im.FactorScale("gabriel_happy.png", 0.25)
image gabriel_nervous= im.FactorScale("gabriel_nervous.png", 0.25)
image gabriel_normal= im.FactorScale("gabriel_normal.png", 0.25)
image gabriel_sad= im.FactorScale("gabriel_sad.png", 0.25)
image gabriel_shocked= im.FactorScale("gabriel_shocked.png", 0.25)
#Scale Alice
image alice_smile= im.FactorScale("alice_smile.png", 0.25)
#Scale Andrew
image andrew_normal= im.FactorScale("andrew_normal.png", 0.25)
#Scale Parker
image parker_normal= im.FactorScale("parker_normal.png", 0.25)


# The game starts here.

label start:

    scene bg_alarm

    "{i}*Drinnnnnnnnnnnnnng*{/i}"

    B "Mmmh... ?
        \nPfff et dire que j’ai déjà mis le réveil le plus tard possible…"
    B "Faut vraiment que je pense à me coucher plus tôt.
        \nBon aller pas le temps de trainer, petite douche et c’est partit."

    scene bg_living_room

    B "Ok je suis prêt
        \nJ’ai pas l’impression d’avoir entendu le réveil de Gabriel, je vais aller rapidement vérifier qu’il est réveillé."
    B_shout "Gabriel! n'oublie pas que tu dois être à l’arrêt de bus dans moins de 20 min!"
    B_shout "Eh Gabriel tu es réveillé ?"

    show gabriel_normal

    G "Ouais ouais, c’est bon t’inquiètes. Je serai au bus à l’heure, je prend juste une douche j’ai pas envie de petit déjeuner ce matin."

    B "Bon ça marche.
        \nD’ailleurs ca te dirait qu’on se mate un film ce soir pour fêter la fin de la semaine ?
        \nJe pensais télécharger le dernier Star Wars."

    G "Heu ouais pourquoi pas mais je devais peut etre voir Loris ce soir. Je te redis."

    B "D’accord, on verra bien ce soir. Aller j’y vais, bon courage pour les cours Gab !"

    #scene Bureau


    return
