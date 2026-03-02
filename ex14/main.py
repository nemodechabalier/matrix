"""Exercice 14 - Projection.

Ce module teste la génération d'une matrice de projection perspective 4x4
utilisée pour le rendu 3D.

Paramètres : FOV, ratio d'aspect, plans near et far.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from matrix import Matrix
from projection import projection


def write_proj(matrix: Matrix, filepath: str):
    """Exporte une matrice de projection vers un fichier.
    
    Écrit la matrice transposée (colonnes en lignes) dans un fichier texte
    au format CSV pour utilisation avec un visualiseur externe.
    
    Args:
        matrix (Matrix): Matrice 4x4 de projection.
        filepath (str): Chemin du fichier de sortie.
    """
    with open(filepath, 'w') as f:
        n = len(matrix.data)
        for col in range(n):
            row_values = [str(matrix.data[row][col]) for row in range(n)]
            f.write(", ".join(row_values) + "\n")


def main():
    """Fonction principale pour tester la matrice de projection.
    
    Génère une matrice de projection avec les paramètres par défaut
    et l'exporte vers un fichier.
    """
    proj = projection()
    print(proj)
    write_proj(proj, "matrix_display/proj")
	
if __name__ == "__main__":
	main()