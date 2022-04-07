#importer les modules dont nous aurons besoin
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import folium
import requests
import json


#importer le module que nous avons crée pour ce projet
import barcelona as ba



###le but de cet outil est de permettre a un entrepreneur de faire l'analyse
###de données provenant des bases de données disponibles publiquement et reperer des occasions d'affaires,
###etudes de marché ou des insights ###
### nous utiliserons les données provenant de https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets
### d'autres bases de données pourraient egalement être traitées par l'utilisateur


### Le code source est hebergé sur https://github.com/alvamig/barcelona ###
### vous pouvez contacter alvaro.chavez-zavaleta@hec.ca si vous désirez devenir collaborateur ###


###
###  Cette partie nous permet de loader les datasets de barcelone
###


#lire les données par défaut
deaths = pd.read_csv("deaths.csv")
accidents_2017 = pd.read_csv("accidents_2017.csv")
air_quality_Nov2017 = pd.read_csv("air_quality_Nov2017.csv")
air_stations_Nov2017 = pd.read_csv("air_stations_Nov2017.csv")
births = pd.read_csv("births.csv")
bus_stops = pd.read_csv("bus_stops.csv")
immigrants_by_nationality = pd.read_csv("immigrants_by_nationality.csv")
immigrants_emigrants_by_age = pd.read_csv("immigrants_emigrants_by_age.csv")
immigrants_emigrants_by_destination = pd.read_csv("immigrants_emigrants_by_destination.csv")
immigrants_emigrants_by_destination2 = pd.read_csv("immigrants_emigrants_by_destination2.csv")
immigrants_emigrants_by_sex = pd.read_csv("immigrants_emigrants_by_sex.csv")
life_expectancy = pd.read_csv("life_expectancy.csv")
most_frequent_baby_names = pd.read_csv("most_frequent_baby_names.csv")
most_frequent_names = pd.read_csv("most_frequent_names.csv")
population = pd.read_csv("population.csv")
transports = pd.read_csv("transports.csv")
unemployment = pd.read_csv("unemployment.csv")
#par default
data = population

#crée une liste des dfs disponibles
loadeddfs = []
loadeddfs = ["deaths.csv","accidents_2017.csv","air_quality_Nov2017.csv","air_stations_Nov2017.csv"]
loadeddfs.extend(["births.csv","bus_stops.csv","immigrants_by_nationality.csv","immigrants_emigrants_by_age.csv"])
loadeddfs.extend(["immigrants_emigrants_by_destination.csv","immigrants_emigrants_by_destination2.csv"])
loadeddfs.extend(["immigrants_emigrants_by_sex.csv","life_expectancy.csv","unemployment.csv"])
loadeddfs.extend(["most_frequent_baby_names.csv","most_frequent_names.csv","population.csv","transports.csv"])
#display(loadeddfs)

#ce dictionnaire nous permettra de documenter les fonctions que nous créeons dans le programme
fonctions = {}


##
## cette partie du code fait appel aux des diverses fonctions du module que nous avons crée
##

ba.bonjour(loadeddfs)
ba.choixdf(loadeddfs,pd,data)



# Maintenant, on commence notre analyse:


# Quels sont les 10 quartiers qui ont les plus/moins de population ? 

ba.barres(data=population,colonne1 = 'Neighborhood.Name',colonne2='Number',xlabel='Nom de la ville',
           ylabel="Population",title="Taille de population par quartier",fonctions=fonctions)

# Quels sont les 10 quartiers qui ont les plus/moins de chômeurs ?
ba.barres(data=unemployment,colonne1='Neighborhood Name',title='Emploi par quartier',xlabel='quartier',ylabel='chomeurs',fonctions=fonctions)

# Quels sont les 10 quartiers qui ont les plus/moins de naissances ?
ba.barres(data=births,colonne1 = 'Neighborhood Name',colonne2='Number',xlabel='Nom de la ville',
           ylabel="nombre de naissances",title="nombre de naissances par quartier",fonctions=fonctions)


# Affichage de la repartition des modes de transport ainsi que la repartition entre les bus de jour et de nuit:

#Quelle est la répartition des transports?
ba.pie(data=transports)

#Quels sont les différents types de bus-stop?  
ba.pie(title='Bus Stops',data=bus_stops,col1='Transport',explode=None)

#Quelle est la répartition des destinations d'immigration?
ba.pie(title='immigrants par destination',data=immigrants_emigrants_by_destination2,col1='to',explode=None, ag='sum',col2 = 'weight')


# Pour cette partie, on fait le tri des dataframe selon les critères choisis par l'utilisateur:


# Quelle est la répartition des tranches d'âges de la population selon l'année et le quartier choisi par l'utilisateur? 
ba.tritempsetautre(data=population)

#Quelle est la répartition des chomeurs pour les differents mois de l'année et du quartier choisi par l'utilisateur?
ba.tritempsetautre(data=unemployment,col1='Year',col2 = 'Neighborhood Name')


### Dans ce projet nous avons pu mettre en pratique enormement de notions du cours de programation en gestion
### A plus haut niveau le plus grand defi que nous avons su relever etait celui-ci de collaborer efficacement a distance
### a cet effet nous avons adopté et appris a utiliser github
### de plus lorsque au fur et a mesure que note code gagnait en longeur et complexité nous avons décidé de le découper
### en fonctions. Cela nous a permis de gagner simplicité et flexibilité
### une fois que nous avions des fonctions logiquement nous avons décidé de toutes les regrouper dans un module de notre cru
### ainsi nous pouvons maintenant appeler au besoin
### a plus bas niveau, nous avons apris a mettre en pratique Pandas, Seaborn, Folium ainsi que Requests
