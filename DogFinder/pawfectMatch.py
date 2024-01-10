import requests
import streamlit as st
import os


st.title("PawfectMatch: Canine Companion Finder")
	
"""
In the sidebar, choose what you want in your dog! \n
You will then get an output of your ideal dog 🐶
"""


def dog(dogL):
    #asks the users their preferences for their ideal dog
    st.sidebar.title("Ideal Charachteristics")
    idealDogSize = st.sidebar.radio("Select how big you would like your dog to be", ["Small", "Medium", "Large"])
    idealEnergyLevel = st.sidebar.radio("Describe how energetic you would like your dog to be", ["Low", "Medium", "High"])
    idealPlay = st.sidebar.select_slider("How playful would you like your dog to be?", ["not much", "at times", "always"])
    idealGroom = st.sidebar.radio("How much grooming are you willing to do?", ["none", "a little", "as much as needed"])
    idealBarking = st.sidebar.selectbox("Do you care about barking?", ["Yes", "No"])
    idealChildren = st.sidebar.selectbox("Do you have children?", ["Yes", "No"])                            
    idealOtherDogs = st.sidebar.selectbox("Do you have other dogs?", ["Yes", "No"])
    
    baseurl = "https://api.api-ninjas.com/v1/dogs?name="

    #iterates through the list of all dogs to see if the user's prefences match with any of the dogs charachteristics
    for each in dogL:
        st.write(each)
        try:
            r = requests.get(baseurl+each, headers={'X-Api-Key': 'Ct4wBESeKPiOzGemfXSqdQ==CvXHC3CAhKz2E03P'})
            data = r.json()
            for eachDict in data:
                energy = eachDict["energy"]
                maxWeight = eachDict["max_weight_male"]
                playful = eachDict["playfulness"]
                groom = eachDict["grooming"]
                barking = eachDict["barking"]
                children = eachDict["good_with_children"]
                otherDogs = eachDict["good_with_other_dogs"]
                image = eachDict["image_link"]

                if maxWeight < 10:
                    dogSize = "Small"
                elif maxWeight >=10 and maxWeight < 35:
                    dogSize = "Medium"
                else:
                    dogSize = "Large"

    ##
                if energy <=2:
                    energyL = "Low"
                elif energy == 3:
                    energyL = "Medium"
                else:
                    energyL = "High"
    ##
                if playful <= 2:
                    play_level = "not much"
                elif playful == 3:
                    play_level = "at times"
                else:
                    play_level = "always"
    ##
                if groom <= 2:
                    groomL = "none"
                elif groom == 3:
                    groomL = "a little"
                else:
                    groomL = "as much as needed"

                if barking <= 3:
                    barking_level = "No"
                else:
                    barking_level = "Yes"
    ##

                if children <= 3:
                    children_level = "No"
                else:
                    children_level = "Yes"
    ##
                if otherDogs <= 3:
                    otherDogs_level = "No"
                else:
                    otherDogs_level = "Yes"

                #checks to see which dogs fit the criteria
                if dogSize == idealDogSize and energyL == idealEnergyLevel and play_level == idealPlay and groomL == idealGroom and barking_level == idealBarking and children_level == idealChildren and otherDogs_level == idealOtherDogs:
                    st.title(each)
                    st.write("Your ideal dog is a {}".format(each))
        except:
            continue

#do this for rest and then do an if thing that says if dogSize == idealDogSize, energyLevel = idealEnergyLevel .... then do the st.title(dog) and stuff for each of the dog

dogL = ["Affenpinscher", "Afghan Hound", "Airedale Terrier", "Akita", "Alaskan Klee Kai", "Alaskan Malamute", "American Bulldog", "American English Coonhound", "American Eskimo Dog", "American Foxhound", "American Hairless Terrier", "American Leopard Hound", "American Staffordshire Terrier", "American Water Spaniel", "Anatolian Shepherd Dog", "Appenzeller Sennenhund", "Australian Cattle Dog", "Australian Kelpie", "Australian Shepherd", "Australian Terrier", "Azawakh", "Barbet", "Basenji", "Basset Hound", "Beagle", "Bearded Collie", "Beauceron", "Bedlington Terrier", "Belgian Laekenois", "Belgian Malinois", "Belgian Sheepdog", "Belgian Tervuren", "Bergamasco Sheepdog", "Berger Picard", "Bernese Mountain Dog", "Bichon Frise", "Biewer Terrier", "Black and Tan Coonhound", "Black Russian Terrier", "Bloodhound", "Bluetick Coonhound", "Boerboel", "Bolognese", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier", "Bouvier des Flandres", "Boxer", "Boykin Spaniel", "Bracco Italiano", "Braque du Bourbonnais", "Braque Francais Pyrenean", "Briard", "Brittany", "Broholmer", "Brussels Griffon", "Bull Terrier", "Bulldog", "Bullmastiff", "Cairn Terrier", "Canaan Dog", "Cane Corso", "Cardigan Welsh Corgi", "Carolina Dog", "Catahoula Leopard Dog", "Caucasian Shepherd Dog", "Cavalier King Charles Spaniel", "Central Asian Shepherd Dog", "Cesky Terrier", "Chesapeake Bay Retriever", "Chihuahua", "Chinese Crested", "Chinese Shar-Pei", "Chinook", "Chow Chow", "Cirneco dell'Etna", "Clumber Spaniel", "Cocker Spaniel (American)", "Cocker Spaniel (English)", "Collie", "Coton de Tulear", "Croatian Sheepdog", "Curly-Coated Retriever", "Czechoslovakian Vlcak", "Dachshund", "Dalmatian", "Dandie Dinmont Terrier", "Danish-Swedish Farmdog", "Deutscher Wachtelhund", "Doberman Pinscher", "Dogo Argentino", "Dogue de Bordeaux", "Drentsche Patrijshond", "Drever", "Dutch Shepherd", "Dutch Smoushond", "East Siberian Laika", "English Foxhound", "English Setter", "English Springer Spaniel", "English Toy Spaniel", "Entlebucher Mountain Dog", "Estrela Mountain Dog", "Eurasier", "Field Spaniel", "Finnish Lapphund", "Finnish Spitz", "Flat-Coated Retriever", "French Bulldog", "French Spaniel", "Galgo Espanol", "German Longhaired Pointer", "German Pinscher", "German Shepherd Dog", "German Shorthaired Pointer", "German Spitz", "German Wirehaired Pointer", "Giant Schnauzer", "Glen of Imaal Terrier", "Golden Retriever", "Gordon Setter", "Grand Basset Griffon Vendeen", "Great Dane", "Great Pyrenees", "Greater Swiss Mountain Dog", "Greek Harehound", "Greenland Dog", "Greyhound", "Griffon Bleu de Gascogne", "Griffon Fauve de Bretagne", "Griffon Nivernais", "Hamiltonstovare", "Hanoverian Scenthound", "Harrier", "Havanese", "Hokkaido", "Hovawart", "Ibizan Hound", "Icelandic Sheepdog", "Indian Pariah Dog", "Irish Red and White Setter", "Irish Setter", "Irish Terrier", "Irish Water Spaniel", "Irish Wolfhound", "Italian Greyhound", "Jagdterrier", "Japanese Akitainu", "Japanese Chin", "Japanese Spitz", "Japanese Terrier", "Jindo", "Kai Ken", "Kaikadi", "Kangal Dog", "Karelian Bear Dog", "Karst Shepherd", "Keeshond", "Kerry Blue Terrier", "Kishu Ken", "Komondor", "Kromfohrlander", "Kuvasz", "Labrador Retriever", "Lagotto Romagnolo", "Lakeland Terrier", "Lancashire Heeler", "Landseer", "Lapponian Herder", "Leonberger", "Lhasa Apso", "Lithuanian Hound", "Longhaired Whippet", "Lowchen", "Maltese", "Manchester Terrier", "Maremma Sheepdog", "Mastiff", "McNab", "Mexican Hairless Dog", "Miniature American Shepherd", "Miniature Bull Terrier", "Miniature Pinscher", "Miniature Schnauzer", "Mountain Cur", "Mudi", "Neapolitan Mastiff", "Nederlandse Kooikerhondje", "Newfoundland", "Norfolk Terrier", "Norrbottenspets", "Norwegian Buhund", "Norwegian Elkhound", "Norwegian Lundehund", "Norwich Terrier", "Nova Scotia Duck Tolling Retriever", "Old Danish Pointer", "Old English Sheepdog", "Otterhound", "Papillon", "Parson Russell Terrier", "Patterdale Terrier", "Pekingese", "Pembroke Welsh Corgi", "Perro de Presa Canario", "Peruvian Inca Orchid", "Petit Basset Griffon Vendeen", "Pharaoh Hound", "Plott", "Pointer", "Polish Lowland Sheepdog", "Pomeranian", "Pont-Audemer Spaniel", "Poodle", "Porcelaine", "Portuguese Podengo", "Portuguese Pointer", "Portuguese Sheepdog", "Portuguese Water Dog", "Posavac Hound", "Pudelpointer", "Pug", "Puli", "Pumi", "Pyrenean Mastiff", "Pyrenean Shepherd", "Rafeiro do Alentejo", "Rajapalayam", "Rampur Greyhound", "Rat Terrier", "Redbone Coonhound", "Rhodesian Ridgeback", "Romanian Mioritic Shepherd Dog", "Rottweiler", "Russell Terrier", "Russian Spaniel", "Russian Toy"]
dog(dogL)
