# Logic Pro : template d'enregistrement batterie + playback

À faire une seule fois, puis enregistrer comme modèle. Les intitulés de menus peuvent varier légèrement selon la version de Logic.

## 1. Réglages audio (Logic Pro > Réglages > Audio)
- **Périphérique d'entrée et de sortie** : la carte son.
- **Taille de la mémoire tampon** : 64 ou 128 échantillons (jouer sans latence).

## 2. Nouveau projet (Fichier > Nouveau > Projet vide)
Dans **Fichier > Réglages du projet** :
- **Audio** : fréquence d'échantillonnage **48 kHz**.
- **Enregistrement** : format **WAV**, **24 bits**.
- **Smart Tempo** : mode **Conserver** (le tempo du projet ne doit jamais s'adapter au jeu).

## 3. Pistes
| Nom exact | Type | Entrée | Pan |
|---|---|---|---|
| `KICK` | audio mono | entrée du micro grosse caisse | centre |
| `SNARE` | audio mono | entrée du micro caisse claire | centre |
| `OH_L` | audio mono | overhead gauche | gauche |
| `OH_R` | audio mono | overhead droit | droite |
| `TOM_1`, `TOM_2`… | audio mono | si micros de toms | selon le kit |
| `PLAYBACK` | audio stéréo | — (fichier importé) | — |

- **Aucun plugin** sur les pistes batterie à l'enregistrement.
- **Flex Time désactivé** sur toutes les pistes batterie. Pas de quantification, pas de Drummer.

## 4. Playback
- Exporter le playback depuis Moises en **WAV, 48 kHz** (pas de MP3).
- À l'import, si Logic propose d'adapter le tempo du projet au fichier : **refuser**.
- Placer le playback au tout début du projet (mesure 1).

## 5. Niveaux (gain staging)
- Régler le gain **sur la carte son**, pas avec les faders de Logic (ils n'agissent pas sur l'enregistrement).
- En jouant le passage le plus fort : crêtes entre **−12 et −6 dBFS**, jamais dans le rouge.

## 6. Enregistrer comme modèle
**Fichier > Enregistrer comme modèle…** → par exemple « Batterie + playback 48k ». Il apparaîtra ensuite dans **Fichier > Nouveau à partir d'un modèle**.

## 7. Prise de calibration (une fois par installation)
Tant que les micros ne bougent pas, une seule prise suffit : 10 s de silence, puis 4 coups de grosse caisse, 4 de caisse claire, 4 sur chaque tom, 1 sur chaque cymbale, en laissant sonner. Exporter comme une session normale (titre « calibration »).

## 8. Export pour le mix
**Fichier > Exporter > Toutes les pistes en tant que fichiers audio** :
- format **WAV**, **24 bits**, **48 kHz** ;
- **effets désactivés** (bypass des plugins), **normalisation désactivée** ;
- toutes les pistes à partir de la **mesure 1** (même point de départ) ;
- destination : un dossier par morceau, au choix (le skill demandera de le sélectionner) ;
- ajouter le playback (`playback.wav`) et, si possible, le morceau original (`original.wav`).
