# Initiation à FreeFem++ : chauffage d'une pièce

## I. Génération du maillage

- `mesh.edp` construit le maillage
- `meshWithCircle.edp` construit le maillage en incorporant une zone interne circulaire où l'onde souhaite connaître la température moyenne.

## II. Thermique stationnaire

On calcule le champ de température à l'équilibre, ie vérifiant sur le domaine :
$$
\Delta T = 0
$$
Et ce pour différentes conditions sur les 3 bords du domaines que sont les murs, la fenêtre et le radiateur:
- `temperaturePieceStat.edp` : Avec 3 configuration de conditions aux limites possibles : 
  - Dirichlet sur la fenêtre et le radiateur (T constante), Neuman sur les murs (flux constant)
  - Dirichlet sur la fenêtre et les murs (T constante), Neuman sur le radiateur (flux proportionnel au différentiel de T)
  - Dirichlet sur la fenêtre et le radiateur, Neuman sur les murs (flux proportionnel au différentiel de T)

## III. Problème transitoire

On s'intéresse ensuite à résoudre le problème dynamique avec l'équation de conduction de la chaleur:
$$
\rho C_p \frac{\partial T}{\partial t} -k\Delta T = 0
$$

Et les conditions aux limites:
- Spatiales : 1ère configuration étudiée dans le porblème statique
- Temporelles : pièce initiallement à la température exterieure

Les scripts suivants ont été réalisés:
- `temperaturePieceTransBE.edp` : Avec implicit Euler
- `temperaturePieceTransTimeEq.edp` : calcule le temps pour atteindre l'équilibre (selon une tolérance sur la norme relative)
- `temperaturePieceDichot.edp` : calcule le temps pour atteindre une certaine température au centre de la pièce, par dichotomie.
- `temperaturePieceTransCN.edp` Avec Cranck-Nicolson

En plus de cela les fichiers `.asc`, sorties de FreeFem++, servent d'entrée au script de plot `plotNorms.py`.