# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# COucou
define B = Character("Bob", color="#ff6633")
define B_shout = Character("Bob", color="#ff6633",what_size=54)
define Al = Character("Alice", color="#99ff33")
define Ad = Character("Andrew", color="#cc9900")
define G = Character("Gabriel", color="#0099ff")
define S = Character("Sarah", color="#6600ff")
define P = Character("Mr.Parker", color="#660033")

#Scale Gabriel
image gabriel_angry= im.FactorScale("gabriel_angry.png", 0.25)
image gabriel_confused= im.FactorScale("gabriel_confused.png", 0.25)
image gabriel_cry= im.FactorScale("gabriel_cry.png", 0.25)
image gabriel_flustered= im.FactorScale("Gabriel_flustered.png", 0.25)
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

#Transition define
define slowdissolve = Dissolve(1.5)
define mediumdissolve = Dissolve(1.0)

# The game starts here.

label start:

    # Initialization Relation ->
    $ relation_alice=0
    $ relation_andrew=0
    $ relation_gabriel=0
    $ relation_sarah=0
    $ relation_parker=0

    scene bg_alarm
    with slowdissolve

    "{i}*Drinnnnnnnnnnnnnng*{/i}"

    B "Mmmh... ?
        \nPfff et dire que j’ai déjà mis le réveil le plus tard possible…"
    B "Faut vraiment que je pense à me coucher plus tôt.
        \nBon aller pas le temps de trainer, petite douche et c’est parti."

    scene bg_living_room
    with slowdissolve

    B "Ok je suis prêt
        \nJ’ai pas l’impression d’avoir entendu le réveil de Gabriel, je vais aller rapidement vérifier qu’il est réveillé."
    B_shout "Gabriel! n'oublie pas que tu dois être à l’arrêt de bus dans moins de 20 min!"
    B_shout "Eh Gabriel tu es réveillé ?"

    show gabriel_normal
    with mediumdissolve
    G "Ouais ouais, c’est bon t’inquiète. Je serai au bus à l’heure, je prend juste une douche j’ai pas envie de petit déjeuner ce matin."

    B "Bon ça marche.
        \nD’ailleurs ca te dirait qu’on se mate un film ce soir pour fêter la fin de la semaine ?
        \nJe pensais télécharger le dernier Star Wars."

    G "Heu ouais pourquoi pas mais je devais peut-être voir Loris ce soir. Je te redis."

    B "D’accord, on verra bien ce soir. Allez j’y vais, bon courage pour les cours Gab !"

    hide gabriel_normal

#--------------------------------------------------------------------

    scene bg_job
    with slowdissolve

    show parker_normal
    with mediumdissolve
    P "Bonjour Bob
        \nJ’ai regardé ton rapport sur le projet Johnson, c’est du bon boulot !"

    B "Merci Monsieur Parker."

    P "Du coup, je pensais vous assigner toi et ton équipe sur le nouveau projet
        \nBaker qui débute la semaine prochaine."
    P "Je te laisse informer ton équipe et terminer le débriefing du projet
        \nJohnson aujourd’hui."
    P "Si tu gères ce nouveau projet comme le précédent je pense que j’en toucherai deux mots au prochain conseil de direction."

    B "Merci de me confier ce projet, on m’a dit qu’il était très ambitieux."

    P "Oui en effet, mais je pense que tu as les compétences pour mener ce projet à bien."
    hide parker_normal

#-------------------------------------------------------------------------------

    scene bg_corridor
    with slowdissolve

    show alice_smile
    with mediumdissolve
    Al "Hey hey, salut Bob! Comment tu vas?
        \nAlors comme ça il parait que tu vas être assigné sur le projet Baker ?"

    B "Mais attends comment tu sais déjà ça ?? "

    Al "Héhé, j’ai mes informateurs tu sais ? J’ai embauché pleins de gens pour t’espionner !"

    B "Non mais arrête, elle vient juste de l’annoncer comment tu as fait pour être déjà au courant ?"

    Al "Haha je te fais marcher !
        \nJ’ai parlé hier avec Monsieur Parker et il m’a dit qu’il comptait te mettre sur le dossier."
    Al "Tu as de la chance que je sois déjà trop occupée avec le dossier Adak !"

    B "Oh mince, tu aurais voulu bosser sur le dossier Baker ?"

    Al "Bien sûr que non, je suis bien contente pour toi, tu le mérites ce projet.
        \nAllez, trêve de plaisanteries, j’ai du pain sur la planche!"

    B "Oula oui tu as raison, il faut que je me dépêche aussi sinon l’équipe va m’attendre !
        \nÀ plus tard Alice!"
    hide alice_smile

#-------------------------------------------------------------------------------

    scene bg_job
    with slowdissolve

    B "Ok tout le monde! Monsieur Parker nous a chargé d’un nouveau dossier
        qu’on commence la semaine prochaine."
    B "Il s’agit d’une affaire en collaboration avec la compagnie Baker
        et j’ai l’impression que la compagnie prend ce projet particulièrement
        à coeur donc je compte sur vous pour être une fois de plus au top la semaine prochaine!"
    show andrew_normal
    with mediumdissolve
    B "Bien. Pour commencer Andrew est-ce que tu pourrais aller nous chercher
        les archives du dernier dossier que nous avons traité avec eux ?"
    B "Et début semaine prochaine tu pourrais nous faire un récapitulatif
        des différentes filiales de Baker ainsi que leur situation sur le marché ?"

    Ad "Écoute Bob, je vais te le dire franchement, j’ai l’impression que tu me
        donnes souvent le sale boulot à faire."
    Ad "Je trouve pas ca très productif de ta part et j’aimerais que tu me donnes
        un peu plus de responsabilités sur le projet de la semaine prochaine."

    B "…
        \nAndrew ce n’est pas la première fois que tu te plains des tâches qui te sont assignées."
    B "La dernière fois qu’on en a parlé tu m’as déjà fait comprendre que tu voulais plus de responsabilités."

    B "Tu es très compétent mais je ne vais pas non plus te donner l’organisation du dossier, c’est mon boulot de faire ça."

    Ad "Bob, je te demande pas ton boulot. Laisse moi juste l’opportunité de faire du travail qui sera remarqué.
        On a tous envie d’avoir une partie du mérite attribué au projet, je pense que les autres sont d’accord non ?"

    B "Bon, bon.
        Ce weekend je vais réfléchir aux différentes tâches de la semaine prochaine et je vous propose qu’on reparle tous ensemble de leur répartition lundi matin."
    B "Tout le monde est d’accord avec ça ?"
    hide andrew_normal

    "Bien on dirait que tout le monde est d’accord.
    \nMême Andrew arrête d’objecter."

    menu:
        "Il m’énerve à toujours vouloir se faire remarquer et remettre en cause mes décisions.":
            jump _1_1A

        "Je me demande s’il a raison de se plaindre des tâches que je lui donne...":
            jump _1_1B

    label _1_1A:
        $ flag_1_1 = 0

        jump _1_1_done

    label _1_1B:
        $ flag_1_1 = 1

        B "Je devrais peut être demander à Alice ce qu’elle en pense."

        jump _1_1_done

    label _1_1_done:

#-------------------------------------------------------------------------------
    scene bg_computer_mail
    with slowdissolve

    B "Bon voyons les messages du jour…"

    "[La boîte mail est pleine de spams et de tentatives de connexions au compte Roll20]"

    B "Tiens, quelqu’un a cherché à se connecter à mon compte Roll20 ?
        \nJe ne me souviens même plus à quoi ce compte pouvait bien servir."

    show andrew_normal
    with mediumdissolve

    Ad "Bob, j’ai trouvé des informations intéressantes sur la compagnie Baker. Tu peux venir voir ?"

    menu:
        "Oh tu as quand même été chercher les archives au final ? C’est sympa, je viens regarder ça avec toi!":
            jump _1_2A

        "Ok, attends 5 minutes je termine ce que je fais et j’arrive.":
            jump _1_2B

    label _1_2A:
        $ flag_1_2 = 0

        hide andrew_normal

        jump _1_2_done

    label _1_2B:
        $ flag_1_2 = 1

        hide andrew_normal

        B "Cette histoire de compte m’a l’air vraiment étrange, je ferais mieux de vérifier tout ça."

        "[Bob tape Roll20 dans barre recherche, et va sur le site]"

        scene bg_computer_roll20
        with slowdissolve

        B "Qu’est-ce que j’avais bien pu mettre comme identifiants?
            \nMmmh, probablement un de ceux que je mets un peu partout."
        B "…\nAhah, c'était ça, parfait."
        B "Je vais supprimer mon compte, je l’utiliserai sans doute plus jamais et ça résoudra le problème par la même occasion."

        jump _1_2_done

    label _1_2_done:

#-------------------------------------------------------------------------------

    scene bg_living_room
    with slowdissolve

    "[Après une journée de travail bien remplie…]"

    show gabriel_normal
    with mediumdissolve

    B "Alors Gabriel, comment s’est passé ta journée aujourd’hui ?"

    hide gabriel_normal
    show gabriel_angry
    with mediumdissolve

    G "Comme d’habitude, avec cette grognasse de proviseure, même si je ne fais rien c’est toujours de ma faute.
        \nJ’en ai marre."

    menu:
        "Hey ne soit pas grossier ! Tu sais que les études c’est important quand même!":
            jump _1_3A

        "C’est vrai que j’ai entendu dire que cette nouvelle proviseure adorait punir les élèves par pur plaisir.":
            jump _1_3B

    label _1_3A:
        $ flag_1_3 = 0

        G "*Pff… Tous les mêmes ces boomers.*"

        hide gabriel_angry

        $ relation_gabriel=relation_gabriel-1

        jump _1_3_done

    label _1_3B:
        $ flag_1_3 =1

        hide gabriel_angry
        show gabriel_flustered
        with mediumdissolve

        G "C’est ça rigole mais en attendant la salle de retenue n’a jamais été aussi pleine!"

        hide gabriel_flustered

        $ relation_gabriel=relation_gabriel+1

        jump _1_3_done

    label _1_3_done:

    show gabriel_normal
    with mediumdissolve

    B "Et sinon qu’as-tu de prévu ce week-end ?
        \nN’oublie pas que ta mère vient te chercher demain matin."

    G "Oh non, je devais aller à un concert avec Loris demain et maman sera jamais d’accord..."
    G "S’il te plaît papa, j’ai vraiment super envie d’y aller, tu peux pas essayer de convaincre maman pour moi ?"

    menu:
        "Gabriel, on en a déjà parlé ce n’est pas à moi de discuter les décisions de ta mère.":
            jump _1_4A

        "D’accord, je vais voir ce que je peux faire.":
            jump _1_4B

    label _1_4A:
        $ flag_1_4 = 0

        B "Demain tu iras chez elle point final.
            \nSi elle ne veut pas que tu ailles à ce concert c’est qu’elle a ses raisons"

        hide gabriel_normal
        show gabriel_angry
        with mediumdissolve

        G "*Marmonne*"
        "[Gabriel s’en va]"

        hide gabriel_angry

        $ relation_gabriel=relation_gabriel-1
        $ relation_sarah=relation_sarah+1

        jump _1_4_done

    label _1_4B:
        $ flag_1_4 = 1

        G "Mais tu as intérêt à être super sage à ce concert sinon ta mère va me tuer."

        G "Papa t’es le meilleur ! Merci!"
        "[Gabriel s’en va]"

        hide gabriel_normal

        B "*Soupire*"
        "[Compose le numéro de Sarah sur son portable]"
        B "Salut Sarah, c’est moi."

        S "Salut Bob! Tout va bien ?
            \nUn soucis avec Gabriel?"

        B "Non non ne t’inquiète pas, c’est rien de grave.
            \nC’est juste que Gabriel m’a dit qu’il devait aller à un concert demain avec Loris et il est vraiment déçu."

        menu:
            "Je me disais qu’on pourrait peut être faire une exception pour ce week-end et qu’il pourrait rester chez moi un jour de plus qu’est ce que tu en penses ?":
                jump _1_4B1A

            "Pourquoi tu ne veux pas qu’il y aille ? Après tout, il est grand maintenant.":
                jump _1_4B1B

        label _1_4B1A:
            jump _1_4B1_done

        label _1_4B1B:
            jump _1_4B1_done

        label _1_4B1_done:

        S "Tu es vraiment pas croyable.
            \nTu ne pourrais pas prendre mon parti pour une fois ?"
        S "À chaque fois que tu en a l’opportunité, tu me rappelles pourquoi j’ai demandé le divorce c’est dingue!
        Mon week-end, ma décision."
        S "Et dire oui tout le temps à ton fils ne fera pas de toi un meilleur père.
        Salut Bob, on se voit demain matin."
        "[Sarah raccroche]"


        $ relation_gabriel=relation_gabriel+1
        $ relation_sarah=relation_sarah-1

    label _1_4_done:


#-------------------------------------------------------------------------------

    scene bg_computer_fb
    with slowdissolve

    "[Une notification apparaît]"
    B "Une nouvelle demande d’ami sur Facebook ?
        \nQui ça peut bien être ?"
    B "Depuis le temps que je n’y suis plus allé.
        \nCela fait longtemps que je n’ai rien posté en plus."
    B "Mmh... je pourrais parler du nouveau projet qu’on m’a confié!"

    "[Bob sur son fil Facebook]"

    scene bg_computer_fb_posting
    with slowdissolve

    B "Super journée, je commence à bosser sur un nouveau projet très cool et important au boulot, affaire à suivre... ;)"

    B "Voilà pas mal, j’imagine déjà la tête d’Andrew quand il va lire ça."

#-------------------------------------------------------------------------------

    scene bg_living_room
    with slowdissolve

    show gabriel_normal
    with mediumdissolve

    B "Hey Gab!
        \nJ’ai vu que ta chambre était loin d’être rangée alors que je te l’ai demandé plusieurs fois déjà, tu pourrais faire un effort s’il te plaît ?"


    hide gabriel_normal
    show gabriel_angry
    with mediumdissolve

    G "Mais oui bien sûr… et toi tu pourrais ranger tous tes papiers qui trainent depuis des mois dans ton bureau ?
        \nBientot il y en aura tellement que je pourrai même plus poser mon ordi dessus!"



    B "Ça n’a rien à voir voyons… Allez, range-moi ça au plus vite!"

    hide gabriel_angry

    B "C’est vrai que j’ai un peu délaissé le rangement de mon bureau avec tout le travail que j’ai ces derniers temps.
    Je vais aller ranger ça vite fait bien fait comme ça, ça motivera Gabriel à ranger sa chambre."

    scene bg_desk_messy
    with slowdissolve

    B "Oh c’est vrai qu’il y a beaucoup plus de documents que ce que je pensais."


    menu:
        "Bon je ne vais garder que les plus récents et mettre le reste à la poubelle, de toute façon je n’aurais jamais besoin de toute cette paperasse...":
            jump _1_5A

        "Allez, tout ce bazar direction poubelle ! Si j’avais eu besoin d’un de ces papiers je m’en serais déjà rendu compte depuis le temps.":
            jump _1_5B

    label _1_5A:
        $ flag_1_5=0

        jump _1_5_done
    label _1_5B:
        $ flag_1_5=1

        jump _1_5_done
    label _1_5_done:

    scene bg_desk
    with slowdissolve

    B "Voilà qui est fait, ce n’était pas si long après tout.
        \nJe me regarderai bien un film maintenant que tout est rangé, ça fait un moment que j’attends de voir le dernier Star Wars."

    B "On dirait que Gabriel est sorti, il a du aller voir Loris.
        \nBon tant pis, il aurait pu me prévenir quand même..."

    scene bg_computer_fb
    with slowdissolve

    B "Voyons, si j’arrive à le télécharger."

    "[Bob tape sur le moteur de recherche]"

    scene bg_computer_search_starwars
    with slowdissolve

    "[Téléchargement gratuit dernier Star Wars]"
    "[Bob clique sur le premier lien]"

    scene bg_computer_starwars_first_link
    with slowdissolve

    B "Je vais essayer sur ce site"
    "[Bob télécharge le fichier]"
    B "Mmmh… La qualité est vraiment pas terrible…"

    $ has_malware = False

    menu:
        "Je vais essayer de trouver un meilleur site.":
            jump _1_6A

        "Bof, c’est pas grave, après tout c’est un site gratuit.":
            jump _1_6B

    label _1_6A:
        $ flag_1_6 = 0
        B "Bien, essayons celui-là"

        scene bg_computer_search_starwars
        with slowdissolve

        B "L’apparence de ce site m’a l’air bizarre."

        $ DisplayExeExtension=False
        $ RunMovieExe=False

        menu:
            "Je crois que je vais retourner sur le premier site.":
                jump _1_6A1A

            "Courage, ca va bien finir par marcher.":
                jump _1_6A1B

        label _1_6A1A:
            $ flag_1_6A1 = 0

            scene bg_computer_starwars_first_link
            with slowdissolve

            jump _1_6B
        label _1_6A1B:
            $ flag_1_6A1 = 1

            scene bg_computer_starwars_second_link
            with mediumdissolve

            "[Bob a téléchargé le fichier]"

            label loop_1_6:
                if not(DisplayExeExtension or RunMovieExe):
                    scene bg_computer_starwars_second_link
                    show screen could_click_extension

                $ renpy.pause()
                jump loop_1_6

            label end_loop_1_6:

                if DisplayExeExtension:
                    scene bg_computer_starwars_second_link_with_exe

                    menu:
                        "Je prefère retourner sur le premier site et effacer ce fichier":
                            jump _1_6A1B1A
                        "Allez! Je démarre ce film":
                            jump _1_6A1B1B
                    label _1_6A1B1A:
                        $ flag_1_6A1B1 = 0
                        scene bg_computer_starwars_first_link
                        jump _1_6B
                    label _1_6A1B1B:
                        $ flag_1_6A1B1 = 1
                        jump _1_6A1B_done
                    label _1_6A1B_done:
                "[Bob lance le film (qui ne démarre pas)]"
                B "Pourquoi le film ne se lance-t-il pas ?"
                "[Bob clique plusieurs fois sur le fichier]"
                B "Ah enfin, ce n’était pas trop tôt. Et cette fois la qualité est au rendez-vous !"

                $ has_malware= True

            jump _1_6A_done
        label _1_6A_done:

        jump _1_6_done

    label _1_6B:
        $ flag_1_6 = 1

        B "Même si la qualité du film n’est pas au top, c’est tout de même appréciable de pouvoir regarder des films si facilement."

        jump _1_6_done
    label _1_6_done:


    scene bg_black
    with slowdissolve

    "[Après la fin du film]"
    B "Vraiment sympa ce film.
        \nOuh il est déjà tard, je devrais aller me coucher."


    "[Fin Part I.]"



    "END OF SCRIPT"
    "END OF SCRIPT"

    return

    screen could_click_extension:
        modal False
        imagebutton:
            xpos 1235 ypos 116
            idle "checkbox_show_extension.png"
            hover "checkbox_show_extension.png"
            action [SetVariable("DisplayExeExtension", True), Hide("could_click_extension"), Jump("end_loop_1_6")]
        imagebutton:
            xpos 262 ypos 312
            idle "movie_avi_exe.png"
            hover "movie_avi_exe.png"
            action [SetVariable("RunMovieExe", True), Hide("could_click_extension"), Jump("end_loop_1_6")]
