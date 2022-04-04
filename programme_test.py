####https://github.com/MorganGautherot/Tuto_Tree_ML/blob/master/Les_arbres_de_de%CC%81cision_regresseur_from_scratch.ipynb


import numpy as np
import pandas as pd
from functools import reduce
import operator

dataframe = pd.DataFrame([[140000, 50, 1, 2],
                         [150000, 55, 0, 3],
                         [100000, 38, 1, 2],
                         [200000, 72, 0, 3],
                         [220000, 70, 1, 4],
                         [120000, 40, 0, 2],
                         [198000, 68, 0, 3],
                         [130000, 54, 0, 2],
                         [140000, 62, 0, 3],
                         [190000, 79, 1, 2],
                         [170000, 67, 1, 4],
                         [90000, 40, 0, 2]],
                         columns=['prix', 'surface', 'garage', 'nb_piece'])

#print(dataframe)

class decision_tree_regressor :
  """ Cette classe a pour but de créer un algorithme d'apprentissage automatique
  d'arbres de décision regresseur"""

  def __init__(self, target, dataframe, max_depth):
    """Cette fonction a pour but d'initialiser les variables essentiel à la 
    construction de notre algorithme.
   INPUT 
    - target : la variable cible qu'il faudra classifier
    - dataframe : les données d'apprentissage
    - max_deapth : la profondeur maximal de l'arbre à entraîner
   """
    self.max_depth = max_depth
    self.target = target
    self.dataframe = dataframe

  def __quanti_split__(self, feature, value, dataset):
   """Cette fonction split un jeu de données en fonction
   de la valeur 'value' de la variable quantitative 'feature' passé en paramètre
   INPUT 
    - feature : integer correspondant à la variable à séparer
    - value : integer correspond à la valeur à laquelle séparer notre jeu de données
    - dataset : pandas dataframe à séparer
   OUTPUT 
    - left : dataframe avec les données où 'feature' est plus petit ou égale à 'value'
    - right : dataframe avec les données où 'feature' est plus grande que 'value' 
   """
   
   left = dataset[dataset.loc[:,feature]<= value]
   right = dataset[dataset.loc[:,feature]> value]

   return left, right

  def __quali_split__(self, feature, value, dataset):
   """Cette fonction split un jeu de données en fonction
   de la valeur 'value' de la variable qualitative'feature' passé en paramètre
   INPUT 
    - feature : integer correspondant à la variable à séparer
    - value : integer correspond à la valeur à laquelle séparer notre jeu de données
    - dataset : pandas dataframe à séparer
   OUTPUT 
    - left : dataframe avec les données où 'feature' est égale 'value'
    - right : dataframe avec les données où 'feature' est différent 'value'
   """
   
   left = dataset[dataset.loc[:,feature]== value]
   right = dataset[dataset.loc[:,feature]!= value]

   return left, right

tree = decision_tree_regressor('prix', dataframe, 4)
left_node, right_node = tree.__quanti_split__('surface', 60, dataframe)
print(left_node)
print(right_node)

