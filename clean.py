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

ba.barres(data=population,colonne1 = 'Neighborhood.Name',colonne2='Number',xlabel='Nom de la ville',
           ylabel="Population",title="Taille de population par quartier",fonctions=fonctions)
ba.barres(data=unemployment,colonne1='Neighborhood Name',title='Emploi par quartier',xlabel='quartier',ylabel='chomeurs',fonctions=fonctions)

#affiche la repartition des modes de transport ainsi que la repartition entre les bus de jour et de nuit
ba.pie(data=transports)
ba.pie(title='Bus Stops',data=bus_stops,col1='Transport',explode=None)

#affiche la population et les gens en recherche d'emploi selon l'année et le quartier choisi
ba.tritempsetautre(data=population)
ba.tritempsetautre(data=unemployment,col1='Year',col2 = 'Neighborhood Name')
