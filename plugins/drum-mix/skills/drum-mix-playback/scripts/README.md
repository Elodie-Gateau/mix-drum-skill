# Scripts

Avancement (on construit par petites étapes, chaque script est testé avant de passer au suivant) :

| # | Script | État |
|---|---|---|
| 1 | `track_info.py` : lire des WAV, afficher fréquence, durée, crête, LUFS, clipping | ✅ fait |
| 1b | `folders.py` : fenêtres Finder pour choisir le dossier d'entrée et le dossier de sortie | ✅ fait |
| 2 | traiter une piste (EQ + compresseur) | à faire |
| 3 | charger les réglages depuis un preset YAML | à faire |
| 4 | mixer toutes les pistes + playback | à faire |
| 5 | master (−14 LUFS, −1 dBTP) + export WAV/MP3 | à faire |
| 6 | contrôle « jeu intact » (mêmes coups, mêmes positions) | à faire |

## Installation (une seule fois)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
