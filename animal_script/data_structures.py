class DataStructures:
    @staticmethod
    def list_example():
        try:
            # Creating a list of animals
            animal_list = ["Elephant", "Lion", "Giraffe", "Zebra", "Tiger"]

            # Accessing elements of a list
            first_animal = animal_list[0]
            last_animal = animal_list[-1]

            # Modifying elements of a list
            animal_list[2] = "Monkey"

            # Adding elements to a list
            animal_list.append("Bear")

            # Removing elements from a list
            animal_list.remove("Lion")

            return animal_list
        except Exception as e:
            return "An error occurred: " + str(e)

    @staticmethod
    def dictionary_example():
        try:
            # Creating a dictionary of animal characteristics
            animal_dict = {'Elephant': 'Big', 'Lion': 'Fierce', 'Giraffe': 'Tall', 'Zebra': 'Striped', 'Tiger': 'Predator'}

            # Accessing elements of a dictionary
            elephant_characteristic = animal_dict['Elephant']
            tiger_characteristic = animal_dict.get('Tiger')

            # Modifying elements of a dictionary
            animal_dict['Giraffe'] = 'Long Neck'

            # Adding elements to a dictionary
            animal_dict['Hippo'] = 'Heavy'

            # Removing elements from a dictionary
            del animal_dict['Zebra']

            return animal_dict
        except Exception as e:
            return "An error occurred: " + str(e)

    @staticmethod
    def set_example():
        try:
            # Creating a set of animal sounds
            animal_sounds = {"Roar", "Trumpet", "Growl", "Snarl"}

            # Adding elements to a set
            animal_sounds.add("Howl")

            # Removing elements from a set
            animal_sounds.remove("Snarl")

            return animal_sounds
        except Exception as e:
            return "An error occurred: " + str(e)
