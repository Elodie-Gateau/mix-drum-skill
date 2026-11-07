# mix-drum-skill

Un plugin Claude pour **mixer et masteriser rapidement des pistes de batterie** enregistrées dans Logic Pro sur un playback généré avec Moises. Son vintage **Daptone** par défaut, réglable.

> **Règle d'or : le jeu du batteur n'est jamais modifié**, seul le son change.

## Installer (Claude Desktop)
1. **Customize → Plugins → Add marketplace**
2. Coller `Elodie-Gateau/mix-drum-skill`
3. Installer le plugin **drum-mix** et activer **Sync automatically** pour recevoir les mises à jour.

## Contenu
```
.claude-plugin/marketplace.json            la « vitrine » du repo
plugins/drum-mix/
  .claude-plugin/plugin.json               nom + version (à incrémenter à chaque mise à jour)
  skills/drum-mix-playback/
    SKILL.md                               la méthode
    scripts/                               le code Python
    presets/                               les recettes de son (daptone, …)
    templates/                             modèles de profil et de fiche de session
```

## Confidentialité
Ce repo est public : **aucun fichier audio et aucun profil personnel** n'y est stocké (voir `.gitignore`). Le profil réel du batteur reste sur son Mac, dans `~/Music/DrumMix/`.

## Licence
MIT
