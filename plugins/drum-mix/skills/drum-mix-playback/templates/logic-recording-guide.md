# Logic Pro : créer le template d'enregistrement batterie + playback

À faire une seule fois. Adapte les numéros d'entrées et les micros au profil (`profile.yaml` : `mics`, `input_map`). Les intitulés de menus peuvent varier selon la version de Logic : en cas de doute, demande une capture d'écran.

## 0. Sur la carte son, avant d'ouvrir Logic
1. Brancher les micros dans l'ordre du profil, par exemple : 1 = grosse caisse, 2 = caisse claire, 3 = overhead gauche, 4 = overhead droit.
2. **Alimentation fantôme (48V)** sur les entrées des **micros statiques** (souvent les overheads). Sans elle, ils ne donnent aucun son. Inutile sur les micros dynamiques.
3. **Modes de couleur du préampli** (ex. « Air » chez Focusrite) : **désactivés** pour un son vintage. Ils sont enregistrés dans la piste et irréversibles. Surtout, garder toujours le même réglage.
4. Dans le logiciel de la carte son, activer le **retour direct** (*direct monitoring*) : le batteur s'entend sans retard dans le casque.

## 1. Réglages audio (Logic Pro → Réglages → Audio)
- **Périphérique d'entrée et de sortie** : la carte son.
- **Taille de la mémoire tampon** : 128 échantillons (suffisant avec le retour direct).

## 2. Créer les pistes batterie en une fois
1. **Fichier → Nouveau** → **Projet vide**.
2. Dans la fenêtre de création de piste : **Audio**, **Mono**, entrée **Entrée 1**, cocher **Ordre croissant**, **Nombre** = nombre de micros, cocher **Activer l'enregistrement**.
3. **Créer**.

## 3. Nommer et placer
1. Double-clic sur chaque nom de piste : `KICK`, `SNARE`, `OH_L`, `OH_R` (et `TOM_1`… s'il y a des micros de toms).
2. Panoramique : `OH_L` à gauche, `OH_R` à droite, le reste au centre.
3. Table de mixage (**X**) → **Options → Étiquettes E/S** : nommer les entrées (« Kick », « Snare », « OH L », « OH R »).

## 4. Piste de l'original
1. **Piste → Nouvelle piste audio**, **Stéréo**, sans entrée.
2. La nommer `ORIGINAL` et la couper (**M**).

À chaque morceau : glisser l'original sur cette piste, lancer le **Stem Splitter** (Ctrl-clic sur la région, souvent dans **Traitement** ; la piste créée peut s'appeler « Hampes » en français), puis couper le stem de batterie.

## 5. Réglages du projet (Fichier → Réglages du projet)
- **Audio** : **48 kHz**.
- **Smart Tempo** : mode **Conserver**.
- **Enregistrement** : **WAV**, **24 bits** (parfois dans Logic Pro → Réglages → Enregistrement), **décompte** 1 mesure.
- **Métronome** dans le casque (touche **K**). Il n'est jamais inclus dans les exports.

## 6. Vérifications
- **Flex Time désactivé** sur toutes les pistes (**⌘F** affiche les commandes Flex). Pas de quantification.
- **Aucun plugin** sur les pistes batterie.
- **Test de niveau** sur le passage le plus fort : gain réglé **sur la carte son**, crêtes entre **−12 et −6 dB** dans Logic, jamais dans le rouge.

## 7. Enregistrer
1. **Fichier → Enregistrer comme modèle…** → « Batterie + playback » (puis **Fichier → Nouveau à partir d'un modèle**).
2. **Fichier → Enregistrer sous…** → `~/Music/DrumMix/template.logicx` (copie utilisée pour créer automatiquement le projet de chaque morceau).

## 8. Régler l'export une fois pour toutes
**⇧⌘E** (Exporter toutes les pistes en tant que fichiers audio) : **WAV**, **24 bits**, **48 kHz**, **effets désactivés**, **normalisation désactivée**, toutes les pistes depuis la **mesure 1**. Logic retient ces réglages.

## 9. Prise de calibration (une fois par installation)
Tant que les micros ne bougent pas : 10 s de silence, puis 4 coups de grosse caisse, 4 de caisse claire, 4 sur chaque tom, 1 sur chaque cymbale en laissant sonner. Exporter comme une session (titre « calibration »).

## Pendant les sessions
- **Logic Remote** (iPhone/iPad, gratuit) : lancer et arrêter l'enregistrement depuis la batterie.
- **Marqueurs** (Intro, Couplet, Refrain…) : permettent de citer des numéros de mesure pour le mix.
- **Prises en mode Cycle** (**C**) : c'est le batteur qui choisit sa meilleure prise, jamais l'IA.
- **Fichier → Gestion de projet → Consolider** avant de copier un projet ailleurs.
