
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

def choixdf(loadeddfs,pd):
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
    return data




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



