# The script of the game goes in this file.
$ renpy.music.set_volume(0.5, .5, channel="music")

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define B = Character("Bob", color="#ff6633")
define B_shout = Character("Bob", color="#ff6633",what_size=54)
define Al = Character("Alice", color="#99ff33")
define Ad = Character("Andrew", color="#cc9900")
define G = Character("Gabriel", color="#0099ff")
define S = Character("Sarah", color="#6600ff")
define S_shout = Character("Sarah", color="#6600ff",what_size=54)
define P = Character("Mr.Parker", color="#660033")
define M = Character("Marc", color="#006633")
define VS = Character("Voix de synthèse", color="#FFFFFF")

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
image sarah_phone= im.FactorScale("bg_phone_icone.png", 0.25)
image sarah_normal= im.FactorScale("Sarah_normal.png", 0.25)
#Scale Alice
image alice_smile= im.FactorScale("alice_smile.png", 0.25)
image alice_neutre = im.FactorScale("alice_neutre.png", 0.25)
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

    scene disclaimer
    with slowdissolve

    $ renpy.pause ()

    scene bg_alarm
    with slowdissolve

    play sound "audio/clock_ring.mp3"
    play music "audio/base0.mp3"  fadeout 1.0 fadein 1.0

    "{i}*Drinnnnnnnnnnnnnng*{/i}"

    stop sound

    "Mmmh... ?"
    "Pfff et dire que j’ai déjà mis le réveil le plus tard possible..."
    "Faut vraiment que je pense à me coucher plus tôt."
    "Bon aller pas le temps de trainer, petite douche et c’est parti."

    scene bg_living_room
    with slowdissolve

    "-Ok je suis prêt-"
    "-Je n’ai pas l’impression d’avoir entendu le réveil de Gabriel, je vais aller rapidement vérifier qu’il est réveillé.-"
    B_shout "Gabriel ! N'oublie pas que tu dois être à l’arrêt de bus dans moins de 20 minutes !"
    B_shout "Eh Gabriel tu es réveillé ?"

    show gabriel_normal
    with mediumdissolve
    G "Ouais ouais, c’est bon t’inquiète."
    G "Je serai au bus à l’heure, je prend juste une douche j’ai pas envie de petit déjeuner ce matin."

    "Bon ça marche."
    "D’ailleurs ca te dirait qu’on se mate un film ce soir pour fêter la fin de la semaine ?
        \nJe pensais télécharger le dernier Star Wars."

    G "Heu ouais pourquoi pas mais je devais peut-être voir Loris ce soir. Je te redis."

    "D’accord, on verra bien ce soir. Allez j’y vais, bon courage pour les cours Gab !"

    hide gabriel_normal

#--------------------------------------------------------------------

    scene bg_job
    with slowdissolve

    play music "audio/joyeuse0.mp3" fadeout 1.0 fadein 1.0

    show parker_normal
    with mediumdissolve
    P "Bonjour Bob
        \nJ’ai regardé ton rapport sur le projet Johnson, c’est du bon boulot !"

    "Merci Monsieur Parker."

    P "Du coup, je pensais vous assigner toi et ton équipe sur le nouveau projet Baker qui débute la semaine prochaine."
    P "Je te laisse informer ton équipe et terminer le débriefing du projet
        \nJohnson aujourd’hui."
    P "Si tu gères ce nouveau projet comme le précédent je pense que j’en toucherai deux mots au prochain conseil de direction."

    "Merci de me confier ce projet, on m’a dit qu’il était très ambitieux."

    P "Oui en effet, mais je pense que tu as les compétences pour le mener à bien."
    hide parker_normal

#-------------------------------------------------------------------------------

    scene bg_corridor
    with slowdissolve

    show alice_smile
    with mediumdissolve
    Al "Hey hey, salut Bob! Comment tu vas ?"
    Al "Alors comme ça il parait que tu vas être assigné sur le projet Baker ?"

    "Mais attends comment tu sais déjà ça ? "

    Al "Héhé, j’ai mes informateurs tu sais ? J’ai embauché pleins de gens pour t’espionner !"

    "Non mais arrête, il vient juste de l’annoncer comment tu as fait pour être déjà au courant ?"

    Al "Haha je te fais marcher !
        \nJ’ai parlé hier avec Monsieur Parker et il m’a dit qu’il comptait te mettre sur le dossier."
    Al "Tu as de la chance que je sois déjà trop occupée avec le dossier Adak !"

    "Oh mince, tu aurais voulu bosser sur le dossier Baker ?"

    Al "Bien sûr que non, je suis bien contente pour toi, tu le mérites ce projet."
    Al "Allez, trêve de plaisanteries, j’ai du pain sur la planche !"

    "Oula oui tu as raison, il faut que je me dépêche aussi sinon l’équipe va m’attendre !"
    "À plus tard Alice !"
    hide alice_smile

#-------------------------------------------------------------------------------

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    scene bg_job
    with slowdissolve

    "Ok tout le monde ! Monsieur Parker nous a chargé d’un nouveau dossier
        qu’on commence la semaine prochaine."
    "Il s’agit d’une affaire en collaboration avec la compagnie Baker
        et j’ai l’impression que la compagnie prend ce projet particulièrement
        à coeur donc je compte sur vous pour être une fois de plus au top la semaine prochaine !"
    show andrew_normal
    with mediumdissolve
    "Bien. Pour commencer Andrew est-ce que tu pourrais aller nous chercher
        les archives du dernier dossier que nous avons traité avec eux ?"
    "Et début semaine prochaine tu pourrais nous faire un récapitulatif
        des différentes filiales de Baker ainsi que leur situation sur le marché ?"

    play music "audio/dispute0.mp3" fadeout 1.0 fadein 1.0

    Ad "Écoute Bob, je vais te le dire franchement, j’ai l’impression que tu me
        donnes souvent le sale boulot à faire."
    Ad "Je trouve pas ça très productif de ta part et j’aimerais que tu me donnes
        un peu plus de responsabilités sur le projet de la semaine prochaine."

    "..."
    "Andrew ce n’est pas la première fois que tu te plains des tâches qui te sont assignées."
    "La dernière fois qu’on en a parlé tu m’as déjà fait comprendre que tu voulais plus de responsabilités."

    "Tu es très compétent mais je ne vais pas non plus te donner l’organisation du dossier, c’est mon boulot de faire ça."

    Ad "Bob, je ne te demande pas ton boulot. Laisse moi juste l’opportunité de faire du travail qui sera remarqué."
    Ad "On a tous envie d’avoir une partie du mérite attribué au projet, je pense que les autres sont d’accord non ?"

    "Bon, bon."
    "Ce weekend je vais réfléchir aux différentes tâches de la semaine prochaine et je vous propose qu’on reparle tous ensemble de leur répartition lundi matin."
    "Tout le monde est d’accord avec ça ?"
    hide andrew_normal

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    "-Bien on dirait que tout le monde est d’accord.-"
    "-Même Andrew arrête d’objecter.-"

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

        "-Je devrais peut être demander à Alice ce qu’elle en pense.-"

        jump _1_1_done

    label _1_1_done:

#-------------------------------------------------------------------------------
    scene bg_computer_mail
    with slowdissolve

    "Bon voyons les messages du jour..."

    "[La boîte mail est pleine de spams et de tentatives de connexions au compte Roll20]"

    "Tiens, quelqu’un a cherché à se connecter à mon compte Roll20 ?"
    "Je ne me souviens même plus à quoi ce compte pouvait bien servir."

    show andrew_normal
    with mediumdissolve

    Ad "Bob, j’ai trouvé des informations intéressantes sur la compagnie Baker."
    Ad "Tu peux venir voir ?"

    menu:
        "Oh tu as quand même été chercher les archives au final ? C’est sympa, je viens regarder ça avec toi !":
            jump _1_2A

        "Ok, attends 5 minutes je termine ce que je fais et j’arrive.":
            jump _1_2B

    label _1_2A:
        $ flag_1_2 = 0

        hide andrew_normal

        jump _1_2_done

    label _1_2B:
        $ flag_1_2 = 1

        play music "audio/intrigue0.mp3" fadeout 1.0 fadein 1.0

        hide andrew_normal

        "Cette histoire de compte m’a l’air vraiment étrange, je ferais mieux de vérifier tout ça."

        scene bg_computer_roll20
        with slowdissolve

        "Qu’est-ce que j’avais bien pu mettre comme identifiants ?"
        "Mmmh, probablement un de ceux que je mets un peu partout."
        "..."
        "Ahah, c'était ça, parfait."
        "Je vais supprimer mon compte, je ne l’utiliserai sans doute plus jamais et ça résoudra le problème par la même occasion."

        jump _1_2_done

    label _1_2_done:

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

#-------------------------------------------------------------------------------

    scene bg_living_room
    with slowdissolve

    "[Après une journée de travail bien remplie…]"

    show gabriel_normal
    with mediumdissolve

    "Alors Gabriel, comment s’est passé ta journée aujourd’hui ?"

    hide gabriel_normal
    show gabriel_angry
    with mediumdissolve

    G "Comme d’habitude, avec cette grognasse de proviseure, même si je ne fais rien c’est toujours de ma faute."
    G "J’en ai marre."

    menu:
        "Hey ne soit pas grossier ! Tu sais que les études c’est important quand même !":
            jump _1_3A

        "C’est vrai que j’ai entendu dire que cette nouvelle proviseure adorait punir les élèves par pur plaisir.":
            jump _1_3B

    label _1_3A:
        $ flag_1_3 = 0

        G "*Pff... Tous les mêmes ces boomers.*"

        hide gabriel_angry

        $ relation_gabriel=relation_gabriel-1

        jump _1_3_done

    label _1_3B:
        $ flag_1_3 =1

        hide gabriel_angry
        show gabriel_flustered
        with mediumdissolve

        G "C’est ça rigole mais en attendant la salle de retenue n’a jamais été aussi pleine !"

        hide gabriel_flustered

        $ relation_gabriel=relation_gabriel+1

        jump _1_3_done

    label _1_3_done:

    show gabriel_normal
    with mediumdissolve

    "Et sinon qu’as-tu de prévu ce week-end ?
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

        play music "audio/dispute0.mp3" fadeout 1.0 fadein 1.0

        "Demain tu iras chez elle point final."
        "Si elle ne veut pas que tu ailles à ce concert c’est qu’elle a ses raisons"

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

        "Mais tu as intérêt à être super sage à ce concert sinon ta mère va me tuer."

        G "Papa t’es le meilleur ! Merci !"
        "[Gabriel s’en va]"

        hide gabriel_normal

        "*Soupire*"
        "[Compose le numéro de Sarah sur son portable]"
        "Salut Sarah, c’est moi."

        show sarah_phone:
            xalign 0.03
            yalign 0.98

        S "Salut Bob! Tout va bien ?
            \nUn soucis avec Gabriel ?"

        "Non non ne t’inquiète pas, c’est rien de grave."
        "C’est juste que Gabriel m’a dit qu’il devait aller à un concert demain avec Loris et il est vraiment déçu."

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

        play music "audio/dispute1.mp3" fadeout 1.0 fadein 1.0

        S "Tu es vraiment pas croyable."
        S "Tu ne pourrais pas prendre mon parti pour une fois ?"
        S "À chaque fois que tu en a l’opportunité, tu me rappelles pourquoi j’ai demandé le divorce c’est dingue !"
        S "Mon week-end, ma décision."
        S "Et dire oui tout le temps à ton fils ne fera pas de toi un meilleur père."
        S "Salut, on se voit demain matin."
        "[Sarah raccroche]"


        $ relation_gabriel=relation_gabriel+1
        $ relation_sarah=relation_sarah-2

    label _1_4_done:

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

#-------------------------------------------------------------------------------

    scene bg_computer_fb
    with slowdissolve

    "[Une notification apparaît]"
    "Une nouvelle demande d’ami sur Facebook ?
        \nQui ça peut bien être ?"
    "Cela fait longtemps que je n’ai rien posté en plus."
    "Mmh... je pourrais parler du nouveau projet qu’on m’a confié !"

    scene bg_computer_fb_posting
    with slowdissolve

    "\"Super journée, je commence à bosser sur un nouveau projet très cool et important au boulot, affaire à suivre... ;)\""

    "Voilà pas mal, j’imagine déjà la tête d’Andrew quand il va lire ça."

#-------------------------------------------------------------------------------

    scene bg_living_room
    with slowdissolve

    show gabriel_normal
    with mediumdissolve

    "Hey Gab!"
    "J’ai vu que ta chambre était loin d’être rangée alors que je te l’ai demandé plusieurs fois déjà, tu pourrais faire un effort s’il te plaît ?"


    hide gabriel_normal
    show gabriel_angry
    with mediumdissolve

    G "Mais oui bien sûr… et toi tu pourrais ranger tous tes papiers qui trainent depuis des mois dans ton bureau ?"
    G "Bientot il y en aura tellement que je pourrai même plus poser mon ordi dessus !"

    "Ça n’a rien à voir voyons... Allez, range-moi ça au plus vite !"

    hide gabriel_angry

    "C’est vrai que j’ai un peu délaissé le rangement de mon bureau avec tout le travail que j’ai ces derniers temps."
    "Je vais aller ranger ça vite fait bien fait comme ça, ça motivera Gabriel à ranger sa chambre."

    scene bg_desk_messy
    with slowdissolve

    "Oh c’est vrai qu’il y a beaucoup plus de documents que ce que je pensais."


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

    "Voilà qui est fait, ce n’était pas si long après tout."
    "Je me regarderai bien un film maintenant que tout est rangé, ça fait un moment que j’attends de voir le dernier Star Wars."

    "On dirait que Gabriel est sorti, il a dû aller voir Loris.
        \nBon tant pis, il aurait pu me prévenir quand même..."

    scene bg_computer_google
    with slowdissolve

    "Voyons, si j’arrive à le télécharger."

    scene bg_computer_search_starwars
    with slowdissolve

    "[Téléchargement gratuit dernier Star Wars]"

    scene bg_computer_starwars_first_link
    with slowdissolve

    "Je vais essayer sur ce site"
    "[Télécharge le fichier]"
    "Mmmh... La qualité est vraiment pas terrible..."

    $ has_malware = False

    play music "audio/intrigue1.mp3" fadeout 1.0 fadein 1.0

    menu:
        "Je vais essayer de trouver un meilleur site.":
            jump _1_6A

        "Bof, c’est pas grave, après tout c’est un site gratuit.":
            jump _1_6B

    label _1_6A:
        $ flag_1_6 = 0
        "Bien, essayons celui-là."

        scene bg_computer_search_starwars
        with slowdissolve

        "L’apparence de ce site m’a l’air bizarre."

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

            "[Télécharge le fichier]"

            label loop_1_6:

                "Je devrais démarrer le film en cliquant sur le fichier"

                if not(DisplayExeExtension or RunMovieExe):
                    scene bg_computer_starwars_second_link
                    show screen could_click_extension

                $ renpy.pause()
                jump loop_1_6

            label end_loop_1_6:

                if DisplayExeExtension:
                    scene bg_computer_starwars_second_link_with_exe

                    menu:
                        "Je prefère retourner sur le premier site et effacer ce fichier.":
                            jump _1_6A1B1A
                        "Allez! Je démarre ce film.":
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
                "Pourquoi le film ne se lance-t-il pas ?"
                "[Bob clique plusieurs fois sur le fichier]"
                "Ah enfin, ce n’était pas trop tôt."
                "Et cette fois la qualité est au rendez-vous !"

                $ has_malware= True

            jump _1_6A_done
        label _1_6A_done:

        jump _1_6_done

    label _1_6B:
        $ flag_1_6 = 1

        "Même si la qualité du film n’est pas au top, c’est tout de même appréciable de pouvoir regarder des films si facilement."

        jump _1_6_done
    label _1_6_done:

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    scene bg_black
    with slowdissolve

    "[Après la fin du film]"
    "Vraiment sympa ce film.
        \nOuh il est déjà tard, je devrais aller me coucher."


    "[Fin du chapitre I]"


    #---------------------------------------------------------PARTIE 2----------

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    scene bg_blue_sky
    with slowdissolve

    "Ce beau week-end touche bientôt à sa fin, il est temps que j’aille récupérer Gabriel chez sa mère."
    "C’est parti !"

    scene bg_black
    with mediumdissolve
    "[Une demie-heure plus tard…]"

    scene bg_blue_sky
    with mediumdissolve

    show sarah_normal

    "Bonjour Sarah ! Comment vas-tu ? Vous avez passé un bon week-end ?"
    S "Salut Bob ! Bien et toi ? Un plûtot bon weekend oui."
    "D'accord, tant mieux."

    menu:
        "Je voulais m’excuser pour l’autre jour, ça ne se reproduira plus. Tu sais, je fais de mon mieux pour que tout se passe bien entre toi, Gabriel et moi mais parfois je suis simplement maladroit.":
            jump _2_1A
        "Gabriel n’a pas été trop désagréable ? Je sais qu’il peut faire la tête pendant des heures quand il n’a pas ce qu’il veut.":
            jump _2_1B
    label _2_1A:
        $ flag_2_1A=0

        S "Je sais Bob… C’est oublié. Je suis désolée aussi, ma réaction était excessive."

        $ relation_sarah=relation_sarah+1

        jump _2_1_done
    label _2_1B:
        $ flag_2_1B=0

        S "Non, tout s’est très bien passé figure-toi."

        $ relation_sarah=relation_sarah-1

        jump _2_1_done
    label _2_1_done:


    S_shout "Gabriel ton père est là !"

    "Je vais voir s’il a besoin d’aide pour ses affaires, je reviens."

    hide sarah_normal
    show sarah_normal:
        xalign 0.15
        yalign 0.8
    with mediumdissolve

    play music "audio/joyeuse2.mp3" fadeout 1.0 fadein 1.0

    show gabriel_happy:
        xalign 0.8
        yalign 0.8
    with mediumdissolve

    G "Salut Papa ! Je suis prêt, on peut y aller !"
    "Salut mon grand ! Super, c’est parti alors."
    "Au revoir Sarah, passe une bonne soirée."
    S "Au revoir Bob. Bisous mon coeur."
    G "Maman, je t’ai déjà dit que j’aimais pas quand tu m’appelles comme ça."
    S "Ah oui pardon, ça m’a échappé. Au revoir Gabriel, sois sage !"

    scene bg_car
    with slowdissolve

    show gabriel_happy
    with slowdissolve

    "Alors, qu’est ce que tu as fait de beau ce week-end ?"
    G "Oh tu sais pas grand chose."
    "J’ai fait mes devoirs, et j’ai un peu traîné. Et Maman a fait des lasagnes."
    "Ah si ! J’ai joué à un nouveau jeu sur la console. Ça s’appelle “Mega war IV”, tu connais ?"

    menu:
        "Non, jamais entendu parler. C’est un jeu de guerre c’est ça ?":
            jump _2_2A
        "Ah non, pas un jeu de guerre ! En plus, tu es trop jeune pour ça et il paraît que les joueurs de ces jeux ont tendance à devenir violents !":
            jump _2_2B

    label _2_2A:
        $ flag_2_2A = 0

        G "Oui c’est ça. C’est un jeu coopératif, les effets sont super bien faits."
        "Je n’aime pas trop que tu joues à des jeux de guerre."
        "Il y a pleins de jeux sympas pour les jeunes sur la console, pourquoi tu choisis ceux-là ?"
        G "J’ai pleins de copains qui y jouent, et ils en parlent tout le temps à l’école. Du coup, ça me permet d’en discuter avec eux."
        G "Et puis c’est pas réel, c’est qu’un jeu."
        "Tu sais, faire quelque chose pour être comme les autres, c’est jamais une bonne idée. Réfléchis-y !"
        "Si tu veux, on regarde ensemble pour te trouver un nouveau jeu plus sympa et plus adapté à ton âge. Et je te l’offre."
        G "Ah bah si tu me l’offres, ça me va !"
        G "Et puis comme ça, je le montrerai à mes copains, et c’est eux qui voudront faire comme moi !"
        "Tu comprends vite mon fils !"

        $ relation_gabriel=relation_gabriel+1

        jump _2_2_done
    label _2_2B:
        $ flag_2_2B = 1

        play music "audio/dispute1.mp3" fadeout 1.0 fadein 1.0

        "Ah non, pas un jeu de guerre ! En plus, tu es trop jeune pour ça et il paraît que les joueurs de ces jeux ont tendance à devenir violents !"

        hide gabriel_happy
        show gabriel_angry

        G "Vous êtes pénibles avec maman ! C’est bon je suis grand et c’est qu’un jeu ! Et c’est des rumeurs ton truc là."
        G "Je suis sûr que c’est des parents pénibles qui ont créé cette rumeur pour pas que leurs enfants jouent aux jeux vidéos."
        G "Si tu te renseignais un peu, tu verrais qu’il y a pleins d'études qui montrent qu’il n’y a aucun lien."
        "Bon écoute, c’est simple, tu n’as plus le droit de jouer à ce jeu."
        G "C’est injuste !"
        "C’est pour ton bien, Gabriel. En plus il fait beau, tu n’as qu’à aller voir tes copains ou profiter de l’extérieur."

        $ relation_gabriel=relation_gabriel-1

        jump _2_2_done
    label _2_2_done:

    scene bg_black
    with mediumdissolve

    scene bg_alarm
    with mediumdissolve

    play sound "audio/clock_ring.mp3"
    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    "{i}*Drinnnnnnnnnnnnnng*{/i}"

    stop sound

    "Il ne faut pas que je traîne, je ne peux pas me permettre d'arriver en retard avec ce nouveau projet."
    "Tout le monde doit être sur le qui-vive."

    scene bg_living_room
    with slowdissolve

    "Je crois que je n'ai rien oublié, je peux y aller."
    "Je serai même en avance comme ça."
    "Salut Gabriel, passe une bonne journée."

    scene bg_job
    with slowdissolve

    "Effectivement, je suis arrivé bien en avance."
    "C'est cool, pour une fois je vais avoir le temps de regarder mes mails avant d'attaquer ma journée."

    #scene bg_computer_trash
    scene bg_computer_mail #En attendant
    with mediumdissolve

    "Alors quoi de neuf dans la boite aujourd'hui ?"
    "Pub, pub, notifications facebook. Rien d'intéressant pour le moment."

    play music "audio/intrigue0.mp3" fadeout 1.0 fadein 1.0

    "Tiens, pourquoi il est déjà marqué comme lu ce mail ?"
    "C’est bizarre, aurais-je cliqué dessus par inadvertance en me connectant ?"
    "Tiens donc... et comme par hasard un mail de ma banque juste après."
    "Tentative de connexion depuis un nouvel appareil ? Je n’aime pas ça du tout... "
    "Bon aller calme toi Bob et garde la tête froide, ça a un bon en-tête d'e-mail frauduleux."
    "Je me rappelle qu’on avait fait un mini briefing sur les tentatives de phishing il y a quelques années."
    "Bon qu’est-ce que je fais du coup ? "

    # Déclaration des flags sinon la variable n'est pas créée dans certains choix
    $ flag_2_3B_1A_1 = -1
    $ flag_2_3B_1 = -1

    menu:
        "Je suis certain que c’est un spam, je vais directement le mettre dans la corbeille, comme ça aucun risque.":
            jump _2_3A

        "Je vais commencer par l’ouvrir, normalement ça risque pas trop.":
            jump _2_3B

        # Possibilité de choix et d'interaction en même temps ?!
        #[Si le joueur découvre le bouton pour accéder à la corbeille]:
        #   jump _2_3C

    label _2_3A:
        $ flag_2_3 = 0
        "Aller hop, adieu vilain petit poisson."
        "Faut pas me prendre pour un pigeon non plus."
        jump _2_3_done

    label _2_3B:
        $ flag_2_3 = 1
        #scene bg_computer_tentative_connexion
        #with mediumdissolve

        "Je sais pas si je deviens parano, mais j’ai l’impression qu’il n’est pas comme d’habitude."
        "Alors… “Nous avons remarqué une connexion depuis un appareil inhabituel, blablabla, veuillez vous connecter sur le site pour confirmer qu’il s’agit bien de vous.”"

        menu:
            "Je vais cliquer sur le lien, le début de l’URL a l’air de correspondre à celle de ma banque.":
                jump _2_3B_1A

            "Je devrais essayer de retrouver moi-même le lien en naviguant depuis mon moteur de recherche.":
                jump _2_3B_1B

        label _2_3B_1A:
            $ flag_2_3B_1 = 0
            scene bg_login_bank
            with mediumdissolve

            "Veuillez entrer vos identifiants…"

            menu:
                "Le site est exactement le même que celui de ma banque, j’entre mes identifiants.":
                    jump _2_3B_1A_1A

                "Le site ressemble à s’y méprendre, mais ça ressemble bien trop à du phishing, je m’arrête là.":
                    jump _2_3B_1A_1B

            label _2_3B_1A_1A:
                $ flag_2_3B_1A_1 = 0
                "Tiens, je reçois une alerte."
                jump _2_3_alert

            label _2_3B_1A_1B:
                $ flag_2_3B_1A_1 = 1
                "Faut pas me prendre pour un pigeon non plus."
                jump _2_3_done

        label _2_3B_1B:
            $ flag_2_3B_1 = 1
            scene bg_search_bank
            with mediumdissolve

            "Alors, voyons voir."
            "Se connecter…"

            scene bg_login_bank
            with mediumdissolve

            "Mes alertes..."
            "On dirait que je suis arrivé à l’URL exacte du mail."

        label _2_3_alert:
            "Ce qui veut dire que ce n’était pas un spam, et que quelqu’un s’est bel et bien connecté à mon compte !"
            "Ça date d’hier, et ils me disent que la connexion s’est faite dans la région."
            "Impossible, je ne me suis pas connecté sur mon compte depuis un bon moment. Le système aurait-il eu un dysfonctionnement ?"
            "Ou alors, est-ce que ça pourrait être Sarah qui a été vérifier quelque chose ? Elle doit encore avoir les identifiants, vu qu’on faisait compte commun…"
            "Elle doit être au boulot elle aussi, je l'appellerai ce soir, sans faute."
            "Dans tous les cas, il va falloir que je tire ça au clair rapidement."
            jump _2_3_done

    label _2_3C:
        $ flag_2_3 = 2
        scene bg_computer_tentative_connexion
        with mediumdissolve

        "Non mais attends, qu’est-ce que c’est que ce bazard ?!?"
        "On dirait que quelqu’un s’est connecté à la plupart de mes comptes ! Il a même commencé à changer les mots de passe de certains !"
        "Il faut que je fasse quelque chose au plus vite…"
        "Mais quoi ?"
        jump _2_3_done

    label _2_3_done:

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    scene bg_job
    with mediumdissolve

    menu:
        "Tiens, Alice est arrivée. Je vais aller lui dire bonjour, ça nous permettra de discuter un moment.":
            jump _2_4A

        "Je viens de voir Monsieur Parker passer. Je vais lui montrer qu’il a bien fait de se tourner vers moi pour le projet Baker.":
            jump _2_4B

    label _2_4A:
        $ flag_2_4 = 0

        show alice_smile

        "Salut Alice ! Ça va ? Tu as passé un bon week-end ?"
        Al "Hé Bob ! Oui super, et toi ?"
        "Bien aussi ! J’étais tout seul, Gabriel était chez sa mère. "
        "Le week-end est passé à une vitesse folle !"
        Al "C’est souvent comme ça haha, surtout vu le beau temps qu’on a eu !"

        menu:
            "J’en ai profité pour voir le dernier Star Wars, depuis le temps que j’en avais envie !":
                jump _2_4A_1A

            "Pendant que tu es là, je voulais te parler d’Andrew.":
                jump _2_4A_1B

            "J’ai vu un truc inquiétant dans ma boîte mail, et je souhaiterais t’en parler.":
                jump _2_4A_1C

        label _2_4A_1A:
            $ flag_2_4A_1 = 0

            "Et je n’ai pas été déçu, il est vraiment super !"
            Al "Dis-moi rien, je ne l’ai pas encore vu !"
            Al "Tu pourrais me le prêter ? "
            Al "Tu l’as en DVD ? "
            Al "Je meurs d’envie de le voir aussi !"
            "Ah non, je n’ai pas le DVD, je l’ai téléchargé."
            Al "Oh, tu devrais faire attention avec ça, c’est vite fait d’attraper une saleté sur ces sites !"
            "C’était juste pour une fois, je ne le fais pas d’habitude donc bon, ça devrait aller !"
            Al "Méfie-toi Bob, je ne veux pas faire ma rabat-joie, mais c’est tellement vite arrivé ! "
            Al "Et quand tu as un de ces trucs sur ta machine, après tu peux être bien embêté !"
            jump _2_4A_1_done

        label _2_4A_1B:
            $ flag_2_4A_1 = 1

            Al "Dis-moi donc ! Je suis toujours heureuse de pouvoir t’éclairer si je le peux !"
            "Ça fait déjà plusieurs fois qu’il se plaint que je lui donne du sale boulot."
            "Il voudrait que je lui donne plus de responsabilités, afin qu’il puisse se faire davantage remarquer par la direction. "
            "Qu’est-ce que tu en penses toi ? Je devrais lui laisser plus de tâches conséquentes ?"
            Al "Effectivement, c’est épineux comme question…"
            Al "Je peux comprendre Andrew, ça fait un moment qu’il essaye de monter dans la hiérarchie sans trop de succès."
            Al "Je pense que c’est important que tout le monde ait sa chance."
            Al "Après, je pense aussi que c’est ton projet et que si tu estimes qu’Andrew doit faire un certain boulot, et bien c’est sûrement la bonne solution."
            Al "Peut être aussi qu’il n’a pas eu l’attitude qui t’aurais donné envie de l’aider ou de lui faire confiance."
            Al "Ton choix sera le bon Bob, tu fais du super boulot dans cette boîte. "
            jump _2_4A_1_done

        label _2_4A_1C:
            $ flag_2_4A_1 = 2

            "J’ai vu un mail marqué comme lu, alors que j’étais persuadé de ne jamais l’avoir ouvert."

            if flag_2_3 == 0 or flag_2_3B_1A_1 == 1:
                "Et puis je reçois des e-mails de phishing franchement bien faits."
            elif flag_2_3B_1 == 1:
                "Et surtout, on dirait que quelqu’un s’est connecté à mon compte sur le site de ma banque…"
                "C’est probablement Sarah qui avait besoin de vérifier quelque chose, mais ça m'inquiète."
                "Et si ce n’était pas elle ? Elle me tient au courant lorsqu’elle se connecte normalement."

            "C’est bizarre non ?"
            "Enfin, soit ma boîte mail débloque, soit je perds la tête."
            "Tu crois que je devrais aller me faire dépister pour Alzheimer ?"

            hide alice_smile
            #show Alice_rire

            Al "*rire*"
            Al "Mais non Bob ! Tu n’as pas Alzheimer ! Arrête de dire des bêtises !"
            Al "Tu as une bien meilleure mémoire que moi, si un de nous deux doit consulter, ce n’est pas toi !"

            #hide Alice_rire
            show alice_neutre

            Al "Par contre pour ta boîte mail, je me ferais un peu plus de soucis. "
            Al "Un mail ne se lit jamais tout seul ! Gabriel a accès à tes mails ?"
            "Non, non, il a sa propre adresse, et il ne connaît pas mon mot de passe. "
            "Enfin je crois en tout cas… je lui ai peut être donné un jour mais ca devait être il y a longtemps. "
            "Dans tous les cas ça m’étonnerait qu’il s’y soit connecté sans m’en parler."
            Al "D’accord. "
            Al "C’est possible que tu l’aies lu sans t’en rendre compte, mais si ça t’arrive à nouveau, tu devrais demander à quelqu’un qui s’y connaît !"

            if flag_2_3B_1 == 1:
                Al "Et concernant ta banque, c’est encore bien plus inquiétant. "
                Al "Tu devrais essayer de les appeler dans la journée pour leur demander conseil."

            jump _2_4A_1_done

        label _2_4A_1_done:

        "Merci Alice !"
        "Comme d’habitude, tu es toujours de bon conseil. "
        "Tu sais, je suis content que tu ne sois jamais bien loin !"
        "Passe une bonne journée, on se voit plus tard !"
        Al "C’est toujours avec plaisir ! "
        Al "Repasse me voir quand tu veux !"
        Al "Courage pour ton projet, tu vas assurer !"
        "Merci, toi aussi, tu assures ! "
        "Allez j’y vais, à plus tard !"

        jump _2_4_done

    label _2_4B:
        $ flag_2_4 = 1

        show parker_normal

        "Bonjour Monsieur Parker, comment allez-vous ?"
        P "Bonjour Bob ! Très bien et toi ? "
        "Bien, je tenais encore à vous remercier de m’avoir mis sur ce projet."
        "Je vais faire un débrief avec l’équipe ce matin et répartir les tâches pour la semaine à venir !"
        "J’ai commencé à débroussailler ce week-end et je compte m’investir à fond !"
        P "Je suis heureux de l’entendre ! "
        P "Et je ne doute pas que j’aie fait le bon choix en vous mettant sur ce projet. "
        P "Vous voir motivé comme cela me confirme que j’avais raison !"
        "Merci Monsieur Parker. "
        "Je vous tiens au courant des avancées du projet. "
        "Passez une bonne journée !"
        P "Merci Bob, pareillement !"
        jump _2_4_done

    label _2_4_done:

    scene bg_corridor
    with mediumdissolve

    play music "audio/intrigue0.mp3" fadeout 1.0 fadein 1.0

    "Hé, salut Marc !"
    show marc
    with mediumdissolve

    M "Tiens Bob ! Comment ça va aujourd’hui ?"
    "Bien, bien. Je retourne à mon bureau pour démarrer ma journée de travail !"
    M "Décidément, toujours à aller discuter à droite à gauche toi ! *rire* Je rigole, tu travailles bien plus que moi hahaha !"
    M "Dis donc, qu’est-ce que ça donne le hack de ton Facebook ? Tu as pu résoudre le problème ? "
    "Le hack de mon Facebook ?"
    M "Bah oui ! J’ai vu ta publication."

    show bg_phone_publication
    with slowdissolve

    M "En tout cas, tu as bien fait de le signaler ! J’espère que ça ne te causera pas trop de soucis, des pourris ces hackeurs !"

    hide bg_phone_publication

    M "Bon, je dois y aller, je suis en retard. À plus Bob !"

    hide marc

    "C’est quoi cette histoire de compte piraté ? Ce n’est pas moi qui ai publié ce post."
    "Et Marc avait bien l’air d’être convaincu qu’il venait de moi. Ça ne doit pas être le seul."
    "Je vais aller regarder tout ça d’un peu plus prêt."

    show bg_phone_publication
    with slowdissolve

    "Effectivement, je peux comprendre qu’ils pensent que ce soit moi. Même nom, mêmes photos, mêmes infos personnelles... Ce compte est presque entièrement identique au mien."
    "Comment a-t-il pu avoir accès à toutes ces informations ?"
    "Et merde, on dirait que le hackeur a pu se connecter à mon véritable compte..."
    "Il a publié pleins de spams publicitaires sur mon vrai mur pour appuyer l’hypothèse que je me suis fait piraté !"
    "Je ne sais pas trop ce que je peux faire."

    hide bg_phone_publication

    menu:
        "Tiens il y a Andrew qui passe justement, je vais lui demander conseil.":
            jump _2_5A

        "Je vais appeler Gabriel. Il est bien plus “connecté” que moi, il saura sûrement ce qu’il faut faire dans cette situation.":
            jump _2_5B

    label _2_5A:
        $ flag_2_5 = 0

        show andrew_normal
        with mediumdissolve

        "Andrew ! J’ai besoin de ton aide !"
        "Apparemment quelqu’un a créé un faux profil Facebook quasiment identique au mien, et il essaie de faire croire que mon compte actuel a été hacké."
        "Et je crois qu’il a aussi eu accès à mon véritable compte..."
        "Qu’est-ce que je peux faire à ton avis ?"
        Ad "C’est gentil de me demander conseil pour une fois Bob."
        Ad "Je suis désolé, mais c’est déjà presque l’heure du meeting Baker. Je ne voudrais pas arriver en retard pour un projet si important, et je pense que toi non plus."
        Ad "Tu devrais laisser tes problèmes personnels pour le moment et t’en occuper ce soir."
        Ad "On va tous avoir besoin de toi pour définir le planning de tâches. C’est toi le chef de projet après tout."
        "Je vois, tu as raison. Je vais aller au meeting, à tout de suite."

        hide andrew_normal

        "-Décidément il est vraiment odieux ce type.-"
        "-Il peut travailler aussi bien qu’il veut, je n’arriverai jamais à le supporter.-"
        "-Je me demande si je n’arriverais pas à le faire muter dans une autre équipe.-"

        $ relation_andrew=relation_andrew-1
        jump _2_5_done

    label _2_5B:
        $ flag_2_5 = 1

        show sarah_phone:
            xalign 0.03
            yalign 0.98
        with slowdissolve

        "Allô Gabriel ? Ça va mon grand ?"
        G "Salut Papa ! Euh...oui, ça va et toi ? Pourquoi est-ce que tu m’appelles maintenant ?"
        "J’ai un problème avec mon profil facebook. Et j’aurais besoin de ton aide."
        G "Okay. Je suis en pause mais je reprends dans 10 minutes, qu’est-ce qu’il se passe ?"
        "Apparemment quelqu’un a créé un nouveau profil quasiment identique au mien, et il essaie de faire croire que mon compte actuel a été hacké."
        "Et je crois qu’il a aussi eu accès à mon vrai compte... Tout le monde croit que c’est moi qui ai signalé le hack, alors que pas du tout !"
        "Qu’est-ce que je peux faire à ton avis ?"
        G "Oula, c’est embêtant. C’est arrivé à un de mes copains y a pas longtemps, et son père est informaticien. Apparemment, il y a plusieurs choses que tu peux faire."
        "Vas-y dis moi tout !"
        G "Tu as de la chance, sur Facebook je crois que tu ne peux pas changer ton mot de passe sans répondre à ta question secrète."
        G "Du coup, commence par changer ton mot de passe par sûreté."
        G "Tu pourrais également activer l'authentification à deux facteurs. Finalement, une fois que tu auras sécurisé ton compte, tu devrais signaler le faux à Facebook."
        "Ça marche, je vais commencer par changer le mot de passe du coup. Je verrai ce soir pour le reste."
        "Merci mille fois Gabriel, tu me sors une épine du pieds !"
        G "De rien papa, aller je te laisse à tes mots de passe, je dois y aller. À ce soir !"

        hide sarah_phone

        "Ok, changer mon mot de passe Facebook, ça devrait pas être sorcier."

        play music "audio/mini_jeu0.mp3" fadeout 1.0 fadein 1.0

        show bg_phone_changer_mdp
        with slowdissolve

        "Tiens d’ailleurs, c’est vrai que je devrais faire attention, j’utilise un peu toujours les mêmes mots de passe..."
        "Je vais en inventer un nouveau cette fois."
        "Alors qu’est-ce que je vais bien pouvoir mettre ?"

        menu:
            "facebookBob123":
                jump _2_5B_1A

            "FaCebooKBob951":
                jump _2_5B_1B

            "f@C3b0OK951bOb!":
                jump _2_5B_1C

        label _2_5B_1A:
            $ flag_2_5B_1 = 0
            jump _2_5B_done

        label _2_5B_1B:
            $ flag_2_5B_1 = 1
            jump _2_5B_done

        label _2_5B_1C:
            $ flag_2_5B_1 = 2
            jump _2_5B_done

        label _2_5B_done:

        "Et maintenant, la question secrète: le nom de mon premier chat."
        "Brave petit Gargamel, tu es vraiment la meilleure des sécurités !"
        "Voilà, ça devrait faire l’affaire."
        "Je vais noter ce nouveau mot de passe quelque part, sinon je risque de l’oublier."
        "Aller il faut vraiment que je m’y mette maintenant, tout le monde doit déjà m’attendre pour la distribution des tâches du projet Baker..."

        $ relation_gabriel=relation_gabriel+1
        # A changé son mot de passe de Facebook -> met fin à futurs problèmes avec Facebook MAIS le joueur devra se rappeler le nouveau mdp à un moment de l’aventure
        jump _2_5_done

    label _2_5_done:

        scene bg_black
        with slowdissolve

    play music "audio/base0.mp3" fadeout 1.0 fadein 1.0

    show bg_living_room
    with slowdissolve

    "Pfiou, impossible de dégager ne serait-ce que 15 minutes de la journée."
    "Ça va vraiment être du gros boulot ce projet Baker."
    "Salut Gabriel ! Je suis rentré !"

    if flag_2_5 == 1:
        G "Salut Papa ! Alors tu as eu droit à des nouvelles farces de ton hacker ?"
        G "Tu as bien changé ton mot de passe Facebook ?"

        "Oui, oui, merci encore pour tes conseils, ça m’a beaucoup aidé."
        "Et non pas de nouvelles, j’espère que mon nouveau mot de passe aidera à ce que cette mauvaise blague prenne fin."

        G "Mais oui, ça va aller !"
        G "Tu sais que même moi j‘ai cru que c’était toi sur le nouveau compte !"

        "C’est qu’il se débrouille bien ce lascar… "
        "Je suis inquiet. J’ai l’impression que quelqu’un essaye de me jouer des tours en ce moment… "

        G "Mais non ! Bon allez je vais dans ma chambre, à tout à l’heure !"

    else:
        G "Salut Papa !"

        "Comment ça va ? Tu as passé une bonne journée ?"

        G "Oui et toi ?"

        play music "audio/intrigue0.mp3" fadeout 1.0 fadein 1.0

        "Une journée surprenante… Dans le mauvais sens."
        "J’ai eu un problème avec mon profil facebook."

        G "Ah bon ? Qu’est-ce qui t’es arrivé ?"

        "Apparemment quelqu’un a créé un nouveau profil quasiment identique au mien, et il essaie de faire croire que mon compte actuel a été hacké."
        "Et je crois qu’il a aussi eu accès à mon vrai compte... Tout le monde croit que c’est moi qui ai signalé le hack, alors que pas du tout !"
        "Qu’est-ce que je peux faire à ton avis ?"
        G "Oula, c’est embêtant. C’est arrivé à un de mes copains y a pas longtemps, et son père est informaticien. Apparemment, il y a plusieurs choses que tu peux faire."
        "Vas-y dis moi tout !"
        G "Tu as de la chance, sur Facebook je crois que tu ne peux pas changer ton mot de passe sans répondre à ta question secrète."
        G "Du coup, commence par changer ton mot de passe par sûreté."
        G "Tu pourrais également activer l'authentification à deux facteurs. Finalement, une fois que tu auras sécurisé ton compte, tu devrais signaler le faux à Facebook."
        "Ça marche, je vais commencer par changer le mot de passe du coup."
        "Merci mille fois Gabriel, tu me sors une épine du pieds !"

        G "De rien papa, aller je te laisse à tes mots de passe, je vais dans ma chambre."

        "Ok, changer mon mot de passe Facebook, ça devrait pas être sorcier."

        play music "audio/mini_jeu0.mp3" fadeout 1.0 fadein 1.0

        show bg_phone_changer_mdp
        with slowdissolve

        "Tiens d’ailleurs, c’est vrai que je devrais faire attention, j’utilise un peu toujours les mêmes mots de passe..."
        "Je vais en inventer un nouveau cette fois."
        "Alors qu’est-ce que je vais bien pouvoir mettre ?"

        menu:
            "facebookBob123":
                jump _2_5B_1A_bis

            "FaCebooKBob951":
                jump _2_5B_1B_bis

            "f@C3b0OK951bOb!":
                jump _2_5B_1C_bis

        label _2_5B_1A_bis:
            $ flag_2_5B_1 = 0
            jump _2_5B_done_bis

        label _2_5B_1B_bis:
            $ flag_2_5B_1 = 1
            jump _2_5B_done_bis

        label _2_5B_1C_bis:
            $ flag_2_5B_1 = 2
            jump _2_5B_done_bis

        label _2_5B_done_bis:

        "Et maintenant, la question secrète: le nom de mon premier chat."
        "Brave petit Gargamel, tu es vraiment la meilleure des sécurités !"
        "Voilà, ça devrait faire l’affaire."
        "Je vais noter ce nouveau mot de passe quelque part, sinon je risque de l’oublier."

        hide bg_phone_changer_mdp
        with slowdissolve

        # A changé son mot de passe de Facebook -> met fin à futurs problèmes avec Facebook MAIS le joueur devra se rappeler le nouveau mdp à un moment de l’aventure

    "Je vais commencer par faire le repas pour Gabriel comme ça après je ne serai plus embêté pour régler mes problèmes."

    "[Après le repas]"

    show bg_computer_2030
    with slowdissolve

    play music "audio/intrigue1.mp3" fadeout 1.0 fadein 1.0

    "Gabriel est remonté dans sa chambre. Qu’est-ce que je devrais faire en premier ?"

    #------------------------------------------------------CHOIX_1--------------
    $ flag_2_7=-1 #need to initialize this here to allow _2_7 to reuse choices in _2_6
    $ flag_2_8=-1 #need to initialize this here to allow _2_8 to reuse choices in _2_7
    $ flag_2_9=-1 #need to initialize this here to allow _2_9 to reuse choices in _2_8

    menu:
        " Je vais essayer de me détendre et de me coucher tôt pour réattaquer du bon pied demain. Après la journée que j’ai passé, je n’ai pas le courage de m‘en occuper ce soir":
            jump _2_6A
        "Je vais appeler M. Parker pour voir s’il ne peut pas me libérer ma journée de demain. Il faut que je m’occupe de mes soucis persos.":
            jump _2_6B
        "Tiens, et si j’appelais Alice ? C’est toujours agréable de discuter avec elle. Aller je me lance !":
            jump _2_6C
        "Je me demande qui peut bien être derrière mon problème sur facebook. Je vais essayer de creuser un peu.":
            jump _2_6D
        "Vu ce que j’ai vu ce matin dans ma boîte mail, je vais me dépêcher d’appeler la banque. Je vais le faire tout de suite." if flag_2_3B_1==1:
            jump _2_6E
    label _2_6A:
        $ flag_2_6=0
    label _2_6A_nondestructive:

        #[pas fatigué le lendemain]
        #Aller directement à la fin du chapitre

        jump _2_6_done
    label _2_6B:
        $ flag_2_6=1
    label _2_6B_nondestructive:

        #Icône du téléphone
        play sound "audio/phone_ring.mp3"
        "Dring…"
        "\nDring…"
        "\n\nDring…"
        stop sound

        "Votre correspondant n’est pas joignable. Veuillez réessayer plus tard."

        "Ça ne répond pas. Bon, tant pis. Je vais faire autre chose."

        jump _2_6_done
    label _2_6C:
        $ flag_2_6=2
    label _2_6C_nondestructive:

        #Icône du téléphone
        play sound "audio/phone_ring.mp3"
        "Dring…"
        "\nDring…"
        "\n\nDring…"
        stop sound
        play music "audio/joyeuse0.mp3" fadeout 1.0 fadein 1.0

        Al "Allô Bob ? Mais que me vaut cet honneur ?"
        "Bonsoir Alice ! Rien de spécial, j’avais juste envie de t’appeler."
        Al "C’est gentil ça ! Puisque que c’est toi qui appelle, c’est toi qui décide de quoi on parle !"
        "Hahaha, ça me va !"

        menu:
            "Je peux te parler de mon nouveau sujet favori haha ! Cette histoire de compte   facebook me prend la tête !":
                jump _2_6C_1A
            "Je peux te décrire à quelqu’un point je t’ai trouvé ravissante aujourd’hui ?":
                jump _2_6C_1B

        label _2_6C_1A:
            $ flag_2_6C_1=0

            Al "Je comprends que ça t’angoisse Bob. Mais déstresse, et essaie de trouver des solutions."
            Al "Rester sans rien faire va uniquement faire monter tes angoisses."
            "Tu n’as pas tort… Mais je n’ai aucune idée de quoi faire ! Tu me connais je suis nul avec ces trucs là !"
            Al "Il me semble que tu peux demander à Facebook de clôturer le faux compte. Je suis sûre que tu peux trouver des solutions, fais-toi confiance!"
            Al "Ca doit pas être si sorcier que ça !"
            "Oui c’est vrai. Bon, je vais essayer d’être plus positif alors !"
            Al "C’est ça que je veux entendre !"
            "Bon allez j’arrête de t’embêter avec mes problèmes, parlons d’autre chose !"
            Al "Aucun soucis haha ! On discute de ce que tu veux !"
            #Black screen
            "[30 minutes de discussion plus tard…]"
            Al "Je vais raccrocher, il se fait tard. J’ai passé un très bon moment avec toi Bob merci !"
            "Pareil pour moi. Merci d’avoir répondue présente. On se voit au bureau !"
            Al "Oui, à demain !"

            jump _2_6C_1_done
        label _2_6C_1B:
            $ flag_2_6C_1=1

            Al "Hihi, Bob arrêteee. Tu vas réussir à me gêner."
            "Bon d’accord, j’arrête. Mais je me suis rendu compte qu’on se voyait uniquement au bureau."
            "Ça pourrait être sympa qu’on aille se faire un ciné ou un restau un de ces jours non ?  Tu serais partante ?"
            Al "Oui bien sûr, avec plaisir !"
            "La semaine prochaine ? Jeudi soir par exemple tu pourrais ?"
            Al "Oui jeudi soir je suis libre ! Je note ça dans mon agenda !"
            "Je manquerai pas de te le rappeler sinon ! C’est un des avantages à bosser ensemble !"
            #Black screen
            "[30 minutes de discussion plus tard…]"
            Al "Bon allez, je vais raccrocher, c’est qu’il commence à se faire tard avec tes bêtises."
            "J’ai passé un très bon moment avec toi Bob, merci !"
            "Pareil pour moi. Merci à toi d’avoir décroché ! Je t’embrasse, on se voit au bureau."
            Al "Oui, à demain !"

            jump _2_6C_1_done
        label _2_6C_1_done:

        $ relation_alice=relation_alice+1

        play music "audio/intrigue1.mp3" fadeout 1.0 fadein 1.0

        jump _2_6_done

    label _2_6D:
        $ flag_2_6=3
    label _2_6D_nondestructive:

        play music "audio/intrigue1.mp3" fadeout 1.0 fadein 1.0

        #Graphique ordinateur maison (recherche Internet)

        "Je trouve un paquet de sites en lien avec ma recherche, mais jusqu’à maintenant ils ne m’apprennent rien d’intéressant…"
        "L’informatique c’est un vrai métier moi je vous le dis. Allez, j’essaye encore celui-là et après je laisse tomber."

        #Afficher page : https://www.243tech.com/retrouver-la-personne-qui-vous-espionne-facebook/

        "Ah tiens. Celui-là m’a l’air intéressant. Ils disent de regarder les photos publiées sur le faux-compte et de consulter la liste d’amis."
        "Apparemment ça permet d’obtenir des informations sur le hacker. C’est à ma portée, je vais le faire tout de suite."

        #Graphique ordinateur maison (Facebook)

        "Bon, je n’ai rien appris de très intéressant. Je vais retourner voir ce qu’ils conseillent de faire après ça"

        #Afficher page : https://www.243tech.com/retrouver-la-personne-qui-vous-espionne-facebook/


        "Ensuite, ils disent d’essayer de changer le mot de passe et de suivre plusieurs étapes. Ca m’a l’être d’être un peu plus long et compliqué à faire."
        "Je ne sais pas si je vais me lancer là dedans tout de suite, voyons déjà ce que j’ai d’autre à faire."


        jump _2_6_done
    label _2_6E:
        $ flag_2_6=4
    label _2_6E_nondestructive:

        "Vu ce que j’ai vu ce matin dans ma boîte mail, je vais me dépêcher d’appeler la banque. Je vais le faire tout de suite."
        #Icône du téléphone
        play sound "audio/phone_ring.mp3"
        "Dring…"
        "\nDring…"
        "\n\nDring…"
        stop sound
        VS "Votre banque est fermée pour le moment. Nous sommes ouverts du lundi au vendredi, de 8h à 18h et le samedi de 8h à 12h. Merci de nous rappeler ultérieurement."

        "C’est vrai qu’il est déjà tard. Il faut que je réessaye d’appeler au plus vite demain."

        jump _2_6_done
    label _2_6_done:

    #------------------------------------------------------CHOIX_2--------------

    if flag_2_6!=0 and flag_2_7==-1:

        show bg_computer_2130
        with slowdissolve
        "Déjà 21h30 ?! Le temps a filé sans que je m’en rende compte…"
        "Je ne sais pas ce que je devrais faire vu l’heure qu’il est…"

        menu:
            "Je vais aller me coucher maintenant. Je m’occuperai du reste demain quand je serai plus en forme.":
                jump _2_7A
            "Je vais appeler M. Parker pour voir s’il ne peut pas me libérer ma journée de demain. Il faut que je m’occupe de mes soucis persos." if flag_2_6!=1:
                jump _2_7B
            "Je vais réessayer d’appeler M. Parker. J’ai vraiment besoin d’avoir ma journée de demain de libre pour m’occuper de tout ce que j’ai à régler."if flag_2_6==1:
                jump _2_7C
            "Tiens et si j’appelais Alice ? C’est toujours agréable de discuter avec elle." if flag_2_6!=2:
                jump _2_7D
            "Je me demande qui peut bien être derrière mon problème sur facebook. Je vais essayer de creuser un peu." if flag_2_6!=3:
                jump _2_7_E
            "Je vais poursuivre ma piste pour trouver l’identité du hacker. Ca va me prendre du temps mais ça peut marcher. Je vais tenter le coup."if flag_2_6==3:
                jump _2_7F
            "Je vais chercher sur Internet comment demander la fermeture de ce faux compte.":
                jump _2_7G
        label _2_7A:
            $ flag_2_7=0

            #[pas fatigué le lendemain]
            #(Aller directement à la fin du chapitre)

            jump _2_7_done
        label _2_7B:
            $ flag_2_7=1

            jump _2_6B_nondestructive #redirect to the first dialogue

            #jump _2_7_done
        label _2_7C:
            $ flag_2_7=2

            #Icône du téléphone
            play sound "audio/phone_ring.mp3"
            "Dring…"
            "\nDring…"
            "\n\nDring…"
            stop sound
            play music "audio/dispute1.mp3" fadeout 1.0 fadein 1.0

            P "Bob ? Tout va bien ?"
            "Bonsoir M. Parker. Je suis désolé de vous appeler si tard mais j’aurais vraiment besoin de prendre ma journée de demain… J’ai quelques ennuis personnels."
            P "Vous m’appelez à bientôt 22h pour me demander un jour de congé ?"
            "..."
            P "Et vous me le demandez au moment ou je vous confie un des plus gros projets de l’année ?"
            "Je sais ça tombe mal…"
            P "En plus, vous connaissez le règlement !"
            P "Vous devez me prévenir au moins une semaine à l’avance pour prendre des congés. La veille au soir, ce n‘est pas possible Bob."
            P "Surtout lorsque je vous confie un projet comme celui-là."
            P "Je pensais que vous aviez compris l’ampleur de ce travail mais apparemment ce n’est pas le cas."
            P "Bonne soirée Bob, je vous attends au bureau demain."

            play music "audio/intrigue1.mp3" fadeout 1.0 fadein 1.0

            "J’ai intérêt à assurer au boulot demain. M.Parker avait l’air remonté."
            "Mais quelle idée j’ai eu de l’appeler pour lui demander un congé à cette heure-ci…"
            "Je vais devoir régler mes problèmes perso tout seul et faire avec le boulot."
            $ relation_parker=relation_parker-1

            jump _2_7_done
        label _2_7D:
            $ flag_2_7=3

            jump _2_6C_nondestructive #redirect to the first dialogue

            #jump _2_7_done
        label _2_7E:
            $ flag_2_7=4

            jump _2_6D_nondestructive #redirect to the first dialogue

            #jump _2_7_done
        label _2_7F:
            $ flag_2_7=5
        label _2_7F_nondestructive:

            #Afficher page : https://www.243tech.com/retrouver-la-personne-qui-vous-espionne-facebook/

            "Du coup pour la dernière étape ils disent d’essayer de changer le mot de passe."
            "Ils précisent que je n’arriverai pas à changer le mot de passe du faux-compte étant donné que je ne le connais pas, mais qu’essayer de le changer est suffisant."
            "C’est pas très clair, mais bon je vais continuer."
            "Apparemment je dois aller sur le faux-profil et copier le nom d’utilisateur dans la barre d’adresse. Mmmm… C’est fait."
            "Puis se déconnecter de facebook et coller le nom d’utilisateur dans \"se connecter\" et cliquer sur \"Mot de passe oublié\n."
            "Et là il me propose de recevoir le code de réinitialisation du mot de passe et je dois cliquer sur “Envoyer un SMS”."
            "Ok, voilà j’ai fini."
            "Ahhh je vois, maintenant j’ai les deux derniers chiffres du numéro de la personne qui m’a hackée."
            "Je vais aller vérifier dans mon répertoire si un de mes numéros se terminent par ces deux derniers chiffres."
            "En soit le hacker aurait pu utiliser un faux numéro, mais c’est peu probable."
            "Ce qui est bien possible par contre que le hacker ne fasse absolument pas partie de mon entourage... Mais bon je n’ai rien à perdre à vérifier !."
            "Vu le peu de numéros que j’ai dans mon portable c’est pas gagné…"
            "Gabriel… Non."
            "Sarah… Non."
            "Alice… Non."
            "Parker… Non plus."
            "Il faut vraiment que je me mette à la technologie."
            "Il y a un numéro qui m’aurait été bien utile tiens…"
            "Celui d’Andrew. Je ne le sens pas ce gars-là."
            "En plus il est drôlement doué avec les machines, contrairement à moi. Je devrais essayer d’obtenir son numéro."

            jump _2_7_done
        label _2_7G:
            $ flag_2_7=6
        label _2_7G_nondestructive:

            "Je vais lancer une recherche Internet avec un peu de chance je vais trouver ce que je cherche sans trop galérer."
            "Ce site m’a l’air pas mal."

            #Afficher page : https://www.facebook.com/help/306643639690823?helpref=uf_permalink
            #+ voir images à la fin du doc

            "La procédure pour fermer un compte m’a l’air claire."
            "Je vais prendre mon temps pour être sûr de ne pas me tromper."
            "..."
            # faire défiler images à la fin du doc ? -> procedure de Fb floutée pour report un compte
            "Voilà et maintenant j’appuie sur confirmer. À priori un rapport m’a été envoyé par mail et ma demande a été transmise aux gérants du site. Parfait."

            jump _2_7_done
        label _2_7_done:

    #------------------------------------------------------CHOIX_3--------------

    if flag_2_6!=0  and flag_2_7!=0 and flag_2_8==-1 :

        show bg_computer_2330
        with slowdissolve

        "Que l’heure tourne vite… Plus de 23h déjà… Il est trop tard pour passer des appels maintenant."

        menu:
            "C’est l’heure d’aller me coucher, je ne veux pas être trop fatigué demain.":
                jump _2_8A
            "Je me demande qui peut bien être derrière mon problème sur facebook. Je vais essayer de creuser un peu." if flag_2_6!=3 and flag_2_7!=4:
                jump _2_8B
            "Je vais poursuivre ma piste pour trouver l’identité du hacker. Ca va me prendre du temps mais ça peut marcher. Je vais tenter le coup." if flag_2_7!=5 and (flag_2_6==3 or flag_2_7==4):
                jump _2_8C
            "Je vais chercher sur Internet comment demander la fermeture de ce faux compte." if flag_2_8!=6:
                jump _2_8D
        label _2_8A:
            $ flag_2_8=0

            #[fatigué le lendemain]

            jump _2_8_done
        label _2_8B:
            $ flag_2_8=1

            jump _2_6D_nondestructive #redirect to the second dialogue

            #jump _2_8_done
        label _2_8C:
            $ flag_2_8=2

            jump _2_7F_nondestructive #redirect to the second dialogue

            #jump _2_8_done
        label _2_8D:
            $ flag_2_8=3

            jump _2_7G_nondestructive #redirect to the second dialogue

            #jump _2_8_done
        label _2_8_done:
    #------------------------------------------------------CHOIX_4--------------

    if flag_2_6!=0  and flag_2_7!=0 and flag_2_8!=0 and flag_2_9==-1 :

        show bg_computer_0045
        with slowdissolve

        menu:
            "J’ai abusé sur l’heure… Je vais être crevé demain, au lit.":
                jump _2_9A
            "Je me demande qui peut bien être derrière mon problème sur facebook. Je vais essayer de creuser un peu." if flag_2_6!=3 and flag_2_7!=4 and flag_2_8!=1:
                jump _2_9B
            "Je vais poursuivre ma piste pour trouver l’identité du hacker. Ca va me prendre du temps mais ça peut marcher. Je vais tenter le coup." if flag_2_7!=5 and flag_2_8!=2 and (flag_2_6==3 or flag_2_7==4 or flag_2_8==1):
                jump _2_9C
            "Je vais chercher sur Internet comment demander la fermeture de ce faux compte." if flag_2_7!=6 and flag_2_8!=3:
                jump _2_9D
        label _2_9A:
            $ flag_2_9=0

            jump _2_9_done
        label _2_9B:
            $ flag_2_9=1

            jump _2_9_done
        label _2_9C:
            $ flag_2_9=2

            jump _2_9_done
        label _2_9D:
            $ flag_2_9=3

            jump _2_9_done
        label _2_9_done:

    if flag_2_9>0:
        "Qu’est-ce que je voulais faire déjà….\nJe me sens tellement fatigué d’un coup..."
        "Il faut que je….\n…"
        #[ne met pas de réveil]

    #[très fatigué le lendemain]

    play sound "audio/snore.mp3"
    scene bg_black

    "Fin de la demo. Nous espérons qu'elle vous aura plu et à bientôt pour la suite des aventures de Bob !"
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
