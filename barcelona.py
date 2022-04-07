
##cette fonction permet d'accueillir l'usager et lui presenter les datasets par défaut
def bonjour(loadeddfs):
    ## proposer de voir les datasets dans le programme ##
    accueil = 'Bonjour! ce programme contient par défaut des données de la ville de Barcelone\n'
    accueil += 'voulez vous voir les datasets disponibles?\n'
    accueil += 'oui/non\n'

    reponse = input(accueil)

    if (reponse.lower()) == 'oui':
        print('les voici:\n')
        display(loadeddfs)
    return

##cette fonction permet à l'usager de choisir un df particulier, parmi barcelone ou de son choix

def choixdf(loadeddfs,pd,data):
    intro = 'vous pouvez choisir un jeu de données ou en ajouter un nouveau.\n'
    intro += 'voulez-vous proceder? oui/non\n'
    reponse = input(intro)

    while (reponse.lower()) == 'oui':
        msg = "veuillez entrer le nom ou l'emplacement des données:\n"
        msg +="celles-ci doivent être en format csv\n"
        msg +="le fichier est lu avec pandas.read_csv\n"
        lieu = input(msg)

        try:
            newdata = pd.read_csv(lieu)
        except FileNotFoundError:
            print('\n')
            print('le fichier ne peut être lu')
            print("veuillez vérifier l'emplacement ou le nom\n")
            print('voulez-vous recommencer?')
            reponse = input()

        else:
            print('voici votre dataframe\n')
            data = newdata
            if lieu not in loadeddfs:
                loadeddfs.append(lieu)
            display(newdata)
            break
    return




##cette fonction permet d'afficher 2 diagrammes a barres presentant les 10 unités 
##avec les plus et le moins de valeurs pour la mesure choisie
##par défaut il montre les quartiers avec les plus et le moins de population
## les arguments data -le df-,colonne1-triprimaire-,colonne2-trideclassification
## et  xlabel,ylabel et title - pour ajuste l'affichage peuvent être changés


#les valeurs par défaut correspondent a un df preloadé mais peuvent être ajustées selon vos besoins
#faites attention a la structure 
def barres(data,fonctions,colonne1 = 'Neighborhood.Name',colonne2='Number',xlabel='Nom de la ville',
           ylabel="Population",title="Taille de population par quartier",):
    import seaborn as sns
    import matplotlib.pyplot as plt
    ## initions les variables
    data = data
    colonne1 = colonne1
    colonne2 = colonne2   
#  print (type(data))

    ## resumé des statistiques descriptives des colonnes
    data.describe(include ='all')

    # Tableau affichant le nombre de population par quartier 
    data_nb_population = data.groupby([colonne1])[[colonne2]].sum() 


    # Tableau affichant le top 10 des quartiers avec la plus grande taille de population
    data_nb_population.sort_values(by=[colonne2], ascending = False).head(10).round(2) 

    # Nous voulons maintenant stocker ce "top 10" dans un dataframe
    data_nb_populationtop10 = data_nb_population.sort_values(by=[colonne2], ascending = False).head(10).round(2) 
    data_nb_populationtop10 

    #Histogramme population - message d'erreur

    # Histogramme présentant le nombre de population selon la ville, top 10 
    ##barplot = sns.catplot(kind='bar', x='Neighborhood.Name', y='Number', data=data_nb_populationtop10, order = data_nb_populationtop10['Neighborhood.Name'].value_counts().index)
    ##barplot.set(xlabel='Nom de la ville', ylabel="Population", title="Taille de population par quartier")
    ##plt.xticks(rotation=90)
    ##plt.show()
    #Ça ne fonctionne pas ici puisqu'en faisant le sort, les noms de quartiers devenaient des index. Il faut donc ajouter un reset.index()

    data_nb_populationtop10 = data_nb_population.sort_values(by=[colonne2], ascending = False).head(10).round(2).reset_index() 
    data_nb_populationtop10

    # # diagramme a barres présentant les 10 quartiers avec le plus de population 
    barplot = sns.catplot(kind='bar', x=colonne1, y=colonne2,data=data_nb_populationtop10, order = data_nb_populationtop10[colonne1].value_counts().index)
    barplot.set(xlabel= xlabel, ylabel=ylabel, title=title)
    plt.xticks(rotation=90)
    plt.show()

    # Tableau affichant le top 10 des quartiers avec la plus petite taille de population 
    data_nb_populationlast10= data_nb_population.sort_values(by=[colonne2], ascending = False).tail(10).round(2).reset_index() 
    data_nb_populationlast10 

    # diagramme a barres présentant les 10 quartiers avec le moins de population 
    barplot = sns.catplot(kind='bar', x=colonne1, y=colonne2,data=data_nb_populationlast10, order = data_nb_populationlast10[colonne1].value_counts().index)
    barplot.set(xlabel=xlabel, ylabel=ylabel, title=title)
    plt.xticks(rotation=90)
    
    texte = '''cette fonction permet d'afficher 2 diagrammes a barres presentant les unités
avec les plus et le moins de valeurs pour la mesure choisie
par défaut il montre les quartiers avec les plus et le moins de population,
les arguments data -le df-,colonne1-triprimaire-,colonne2-trideclassification
et  xlabel,ylabel et title - pour ajuste l'affichage peuvent être changés'''

    fonctions.update({'barres()':(texte)})
    
    plt.show()
    return


##cette fonction permet d'afficher un pie chart des 10 plus grandes valeurs qui selon les proportions correspondant a l'aggregation d'une ##colonne au choix
## par défaut il montre la  repartition des types de transports dans barcelone
## explode doit etre None ou bien une serie de type array avec autant d'unités que de catégories dans le piechart
#les arguments data -le df-,col1-triprimaire- peuvent etre chagés pour jouer avec d'autres données,
# et title et explode pour ajuster l'affichage
# On veut maintenant s'intéresser à la répartition des transports

def pie(data,explode = (0.1, 0.01, 0.01,0.1,0.2,0.3,0.4,0.5,),
       title = 'Répartition des transports', col1 = 'Transport',ag='count',col2 = 'Transport'):
    data_transports = data
    data_transports
    import matplotlib.pyplot as plt

    # Voyons voir les différents types de transports utilisés
    colonne = col1
    data_transports[colonne].unique()

    df_transports = data_transports.groupby(col1)[col2].agg(ag).sort_values(ascending = False).head(10)
    df_transports

    # Essayons de voir quels sont les moyens de transport les plus populaires avec un pie chart 
    fig = plt.figure(figsize = (6, 6))
    plt.pie(df_transports,
            labels = df_transports.index,
            autopct = '%1.1f%%',
            colors = ['#00A699','#FF5A60','#79CCCD','#767676'],
            labeldistance = 1.2,
            explode = explode, 
            pctdistance =0.85,)

    plt.title(title)
    plt.show()
    return

#les valeurs par défaut correspondent a un df preloadé mais peuvent être ajustées selon vos besoins
#faites attention a la structure 



#plusieurs dataframes contiennent de la donnée temporelle et par quartier
#essayons d'en faciliter le tri

##cette fonction permet d'afficher et retourner un dataframe qui fait le tri d'un premier dataframe
## le tri est fait selon l'année choisie et la valeur d'une colonne au choix
## par défaut il montre toutes entrées correspondant a un quartier et une année de Barcelone
#data - corresond au dataframe source
#col1 a la colonne d'année
#col2 a au deuxiemme tri

#cette fonction permet de choisir une année et une catégorier a filtrer sur un dataframe
def tritempsetautre(data,col1='Year',col2 = 'Neighborhood.Name'):
    data=data
    col1=col1
    col2 = col2
    #display(data)

    menos = (data[col1].min())
    mas = (data[col1].max())
    
    msg = f'choisir une année entre {menos} et {mas}\n'
    choix_a = int(input(msg))

    redemander ='oui'
    while redemander == 'oui':
        if (choix_a <= mas) and (choix_a >= menos):
            print(f"l'annee choisie est : {choix_a}")
            redemander = 'non'
            break
        else : 
            print("Choix inconnu, choissisez une année parmi:")
            print(data[col1].unique())
            choix_a = int(input(msg))

    #analysons maitenant le df en conservant seulement les données de l'année choisie:
    df_tri_année = data[data[col1] == choix_a]
    df_tri_année

    # nous remarquons maitenant que les données semblent sous-divisées par groupe d'age et sexe
    # choisons un seul quartier pour analyser avec un peu plus de détail

    #mais quels sont les quartiers de Barcelone? demandons a python d'afficher les valeurs uniques des noms de quartiers
    #gardons cette liste de noms
    quartiers = []
    quartiers = data[col2].unique()
    quartiers

    print('voici vos choix:\n')
    display(quartiers)

    msg = 'choisir un filtre parmi les options \n'    

    #nous faisons une liste car on pourrait eventuellement modifier le code pour pouvoir selectionner plusieurs cartiers
    quartier = []
    q = (input(msg))
    quartier.append(q)

    redemander ='oui'
    while redemander == 'oui':
        if q in quartiers:        
            print(f"le choisi de filtre est : {q}")
            redemander = 'non'
            break
        else : 
            print("Choix inconnu, choissisez parmi la liste suivante")
            print(quartiers)
            q = (input(msg))

    df_tri_quartier = data.loc[data[col2].isin(quartier)]
    df_tri_quartier
    # nous avons reussi a filtrer par quartier mais perdons le filtre par année

    # incluons maitenant les deux filtres
    df_tri_multiple = data[(data[col1] == choix_a) & data[col2].isin(quartier)]
    display(df_tri_multiple)
    return 

### code pour afficher la carte folium ###
def carte(data,col1='Neighborhood.Name',col2='Transport',critere='Night bus stop',name='Arrets de bus',url = 'https://raw.githubusercontent.com/martgnz/bcn-geodata/master/barris/barris.geojson',key_on='feature.properties.NOM'):
    import folium
    import requests
    import json
## prenons les arrets de bus
    data = data
    #display(data)
    ## nous voyons que les bus sont énumérés par quatier, coordonnées et si c'est des bus de nuit ou de jour

    #intialisation de la carte folium avec laquelle nous travaillerons
    carte_bus = folium.Map()
    carte_bus

    # nous voudrons afficher une carte des bus avec au centre le point milieu de tous les arrets.
    latitude_moy  = data['Latitude'].mean()
    longitude_moy = data['Longitude'].mean()

    # nous activons l'option de tuile watercolor pour un affichage plus simple et agreable a regarder
    tiles ="Stamen Watercolor"

    #nous creons la carte avec barcelone au milieu
    carte_bus = folium.Map(location=[latitude_moy,longitude_moy],tiles=tiles, control_scale=True,zoom_control=False,zoom_start=12)
    carte_bus

    # rajoutons une éthiquete sur le milieu de la ville pour indiquer qu'il s'agit de barcelone
    folium.Marker(location=[latitude_moy,longitude_moy],
                  popup='Barcelone',
                 ).add_to(carte_bus)
    carte_bus

    ## grace a la fonction marker nous pouvons rajouter un arret de bus dans la carte avec ses infos en éthiquette
    ## le code suivant a été rétiré du main pcq nous explorons une meilleure methode par la suite

    #folium.Marker(location=[data.iloc[0]['Latitude'],data.iloc[0]['Longitude']],
    #              popup=(data.iloc[0]['Bus.Stop']+data.iloc[0]['Transport']+'\n\n'+data.iloc[0]['Neighborhood.Name']),
    #            ).add_to(carte_bus)

    # maitenant essayons de rajouter tous les arrets a l'aide d'une boucle for 
    #for i in range(0,len(data)):
    #   folium.Marker(location=[data.iloc[i]['Latitude'],data.iloc[i]['Longitude']],
    #                popup=(data.iloc[i]['Bus.Stop'])).add_to(carte_bus)

    # nous remarquons que la carte ainsi produite est beaucoup trop chargée et pas tres utile je enleve ces marquers du code avec#

    ##essayons de creer une heatmap 
    #data['bus']=1
    #coord = data[['Latitude','Longitude','bus']]
    #HeatMap(coord).add_to(carte_bus)

    #le resultat est une peu plus clair mais ne permet pas vraiement de retier de insight
    #essayons de rafiner les résultats

    #data['bus']=100
    #coord = data[['Latitude','Longitude','bus']]
    #HeatMap(coord).add_to(carte_bus)
    # la méthode ne semble pas plus appropriée

    #rajoutons une couche a la carte afin d'afficher les barrieres géographiques des cartiers
    #a partir des deonnées de type geojason disponibles sur github
    url = url
    perimetre_quartiers = requests.get(url)
    perimetre_quartiers

    #on verifie et on constate que les données sont de type string
    #print(perimetre_quartiers)
    geo = perimetre_quartiers.text
    #print(type(geo))
    #print(geo)

    #lit le json et transforme le string en dict
    geodict = json.loads(geo)
    #print(type(geodict))

    #obtenir les nombre d'arrets de bus par quartier
    bus = data[[col1,col2]].groupby([col1]).count().reset_index()
    bus

    #ajouter les quartiers dans la carte avec l'info sur le nombre d'arrets
    folium.Choropleth(
        geo_data=geodict,
        data =bus,
        columns=[col1, col2],
        name=name,
        key_on = key_on,
                     ).add_to(carte_bus)
    carte_bus

    #idem mais juste pour les bus de nuit

    #obtenir les donnees
    nuit = data.loc[data[col2] == critere] 
    quartier_nuit = nuit[[col1,col2]].groupby([col1]).count().reset_index()
    quartier_nuit

    #creer le filtre
    folium.Choropleth(
        geo_data=geodict,
        data =quartier_nuit,
        fill_color="PuBuGn",
        columns=[col1, col2],
        name=critere,
        key_on='feature.properties.NOM',
                     ).add_to(carte_bus)
    folium.LayerControl().add_to(carte_bus)

    #nous remettons data a notre valeur initiale puisque elle etait differente dans choropleth
    #data = bus_stops

    #afficher la carte    
    display(carte_bus)

    ## nous voyons que sur la carte le réseau de bus est principalement concentré au centreville et dans les banlieues le jours
    ## tandis que uniquement au centre-ville la nuit
    
    ## les accidents d'auto ont presque tous lieu au centre-ville
    return


#cette fonction permet de choisir entre le sexe, la periode temporelle et une variable qualitative-par default le cartier et il #affiche des visualisations, le top 5 des quartiers
def sex(data):
    import seaborn as sns
    import matplotlib.pyplot as plt

    data= data
    col1='Gender'
    print(data[col1].unique())
    msg = f"choisisez parmi les valeurs affichees : \n"
    choix_s = input(msg)


    # afin d'eviter des resultats vides, on verifie l'input de l'utilisateur avant de continuer.
    redemander = 'oui'
    while ( redemander == 'oui'):
        if (choix_s == 'Male') or (choix_s == 'Female'):
            print(f'{col1}')
            redemander = 'non'
            break
        else : 
            print("Choix inconnu, choissisez entre 'Male' et 'Female' ")
            choix_s = input(msg)

    #on stocke les noms des colonnes de la dataframe 'life_expectancy' dans une liste et on garde juste les periodes.
    Periode = list(data.columns)
    del(Periode[0])
    del(Periode[-1])
    print(Periode)
    #choissisez l'index de la periode voulu
    msg_p = "choisisez l'index de la periode voulue le premier i=1:  \n"
    choix_p = input(msg_p)
    # puisque les index des listes commence par 0 et non pas par 1, on change le type de l'input a 'integer' et on diminue le choix de l'utilisateur de 1  
    choix_p = int(choix_p) -1 
    print('la periode choisie est : {0}'.format(Periode[choix_p]))

    #On afficher les resultats selon les critères choisis:
    life_ex = data[['Neighborhood','Gender',Periode[choix_p]]]
    life_ex = life_ex[(life_ex['Gender'] == choix_s)]
    life_ex = life_ex.sort_values(by = Periode[choix_p], ascending = False) 


        #On souhaite afficher les 5 quartiers qui ont la meilleure 'life_expectancy' pour le sexe et la periode choisi par l'utilisateur.

    

    # On remarque qu'il y a des valeurs null qui ont été lues comme 'NaN', 
    # donc on souhaite remplacer les 'NaN' dans le resultat par 'No data'.
    life_ex[Periode[choix_p]] = life_ex[Periode[choix_p]].fillna("No Data")
    #display(life_ex)



    # Ici on affiche les 5 quartiers qui ont la meilleure 'life_expectancy' selon les criteres choisi : 
    life_e = life_ex.head(5)
    #display(life_e)

     #Affichage
    barplot = sns.catplot(x="Neighborhood", y=Periode[choix_p], kind="bar", data=life_e, aspect=2) 
    barplot.set(xlabel='Neighborhood', ylabel='life_expectancy', title=' les 5 quartiers qui ont le meilleur life_expectancy')
    plt.xticks(rotation=90)
    plt.show()

    #On demande a l'utilisateur de choisir un quartier et un sexe afin d'analyser le changement du 'life expectancy' entre 2006 et 2014
    # demandons a python d'afficher les valeurs uniques des noms de quartiers
    colonne = 'Neighborhood'
    V_unique = data[[colonne,'Gender']].groupby([colonne]).count().reset_index()
    V_unique = V_unique.drop(columns=['Gender'])
    print('Vous avez {0} quartiers'.format(V_unique.size))
    display(V_unique.T)

    # demandons a 'l'utilisateur de choisir un quartier: 
    msg = "choisisez l'index  du quartier a analyser\n"
    choix = int(input(msg))
    quartiers = V_unique.to_dict()
    quartier_choisi = quartiers['Neighborhood'][choix]
    print('Vous avez choisi : {0} -{1}'.format(choix,quartier_choisi))

    # demandons a 'l'utilisateur de choisir un sexe: 

    print(data.Gender.unique())
    msg = "choisisez le sexe voulu : \n"
    choix_s = input(msg)
    redemander = 'oui'
    while ( redemander == 'oui'):
        if (choix_s == 'Male') or (choix_s == 'Female'):
            print('le sexe choisi est : {0}'.format(choix_s))
            redemander = 'non'
            break
        else : 
            print("Choix inconnu, choissisez entre 'Male' et 'Female' ")
            choix_s = input(msg)

    #On affiche les resultats selon les critères choisis:
    life_ex1 = data[(data['Neighborhood'] == quartier_choisi)&(data['Gender']==choix_s)]
    life_ex1


    #on crée une dataframe qui nous permet de faire l'affichage.
    liife = life_ex1.T.reset_index()
    liife= liife.drop(0)
    liife= liife.drop(6)
    liife.columns = ["Periode" , "Life Expectancy"]
    liife


    life_ex_q = sns.relplot(kind='line', x='Periode', y='Life Expectancy', data=liife)
    life_ex_q.set(title=' Life expectancy pour le sexe :{0} et pour le quartier : {1}'.format(choix_s,quartier_choisi))
    plt.show()
    return

##cette fonction effectue des analyses sur la table unemployment de barcelone
## elle permet a l'utilisateur de choisi le sexe et l'année
## elle affiche ensuite les 3 quartiers avec le moins de chomage
##elle sera adapté a un usage sur mesure lors d'une prochaine version de ce programme
def unemployment(data):
    import seaborn as sns
    import matplotlib.pyplot as plt
    unemployment = data
    # Pour la table unemployment on souhaite garder juste les colonnes qui sont pertinants a notre analyse, donc commence par filtrer les données. 
    unemployment = unemployment[['Year','Neighborhood Name','Gender','Number']].groupby(['Year','Neighborhood Name','Gender']).sum().reset_index()
    unemployment.sort_values(by = 'Year')


    # a la fin, on souhaite comparer 3 quartier selon le nombre de personne en chomage.
    # On commence par demander a l'utilisateur de choisir le sexe qu'il souhaite analyser et on verifie l'entrée de l'utilisateur :
    print(unemployment.Gender.unique())
    msg = "choisisez le sexe voulu : \n"
    choix_s = input(msg)
    redemander = 'oui'
    while ( redemander == 'oui'):
        if (choix_s == 'Male') or (choix_s == 'Female'):
            print('le sexe choisi est : {0}'.format(choix_s))
            redemander = 'non'
            break
        else : 
            print("Choix inconnu, choissisez entre 'Male' et 'Female' ")
            choix_s = input(msg)

    #on affiche les années disponibles et on demande a l'utilisateur de choisir l'année:
    colonne_y = 'Year'
    V_unique_y = unemployment[[colonne_y,'Number']].groupby([colonne_y]).sum().reset_index()
    V_unique_y = V_unique_y.drop(columns=['Number'])
    display(V_unique_y.T)
    Years = V_unique_y.to_dict()
    msg = "choisir l'index  de l'année a analyser\n"
    choix = int(input(msg))
    year_choisi = Years['Year'][choix]
    print('Vous avez choisi : {0} -{1}'.format(choix,year_choisi))


    # On affiche les 3 quartiers qui ont le plus bas nombre de personne en chomage:
    chomage = unemployment[(unemployment['Gender'] == choix_s) & (unemployment['Year']== year_choisi) ]
    chomage = chomage.sort_values(by = 'Number', ascending = False) 
    chomage = chomage.tail(3)
    chomage

    #Affichage
    barplot = sns.catplot(x="Neighborhood Name", y='Number', kind="bar", data=chomage) 
    barplot.set(ylabel='Nombre de personnes en chômage.', title=' les 3 quartiers qui ont le plus bas nombre de personne en chomage')

    plt.show()
    return

####cette fonction nous permet d'afficher deux histogrammes, l'un avec toutes les données- pas idéal
### et l'autre avec un tri 
def histo(data):
    import seaborn as sns
    import matplotlib.pyplot as plt
    #Extraire les données uniquement pour 2017
    df_tri_2017 = data[data['Year'] == 2017]
    colonne = 'Neighborhood Name'
    V_unique = df_tri_2017[[colonne,'Number']].groupby([colonne]).sum().reset_index()
    V_unique = V_unique.drop(columns=['Number'])
    print('Vous avez {0} quartiers'.format(V_unique.size))
    display(V_unique)
    
    
    
    #Permettre à l'utilisateur de regarder les données selon le quartier de son choix
    msg = 'choisir un quartier\n'
    quartier = []
    choix = (input(msg))
    quartier.append(choix)
    df_tri_quartier = data.loc[data['Neighborhood Name'].isin(quartier)]
    df_tri_quartier

    #On combine les deux codes afin d'analyser les données selon les quartiers mais uniquement en 2017
    df_tri_quartier_2017 = data[(data['Year'] == 2017) & data['Neighborhood Name'].isin(quartier)]
    df_tri_quartier_2017

    #On veut maintenant vérifier si le compte de nationalités est bon
    nationalite =df_tri_quartier_2017.groupby(['Neighborhood Name'])[['Nationality']].count()
    nationalite

    #Affichons le tout sur un histogramme afin de mieux visualiser la répartition
    Number = data["Number"]
    Nationality = data["Nationality"]
    histo = sns.catplot(kind = "bar", x = "Nationality" , y = "Number", data = df_tri_quartier_2017)
    histo.set(xlabel = "Nationality", ylabel = "Nombre", title = choix)
    plt.xticks(rotation=90)
    plt.show()

    #Nous voyons que l'histogramme est beaucoup trop chargé! réglons le tir.

    #tri par nationalité
    tri_nationalite = df_tri_quartier_2017[["Nationality","Number","Neighborhood Name"]].groupby(["Nationality"]).sum()
    display(tri_nationalite)

    #Nous observons que plusieurs données sont négligeables! Il est donc logique de vouloir faire un Top 20.
    nationalite20 = tri_nationalite.sort_values(by=["Number"], ascending = False).head(20).round(2).reset_index()
    nationalite20

    #histogramme des 20 nationalités les plus predominantes par quartier

    Number = data["Number"]
    Nationality = data["Nationality"]
    histo_2 = sns.catplot(kind = "bar", x = "Nationality" , y = "Number", data = nationalite20)
    histo.set(xlabel = "Nationality", ylabel = "Nombre", title = choix)
    plt.xticks(rotation=90)
    plt.show()
    return
