from pprint import pprint

file_name = "recipes.txt"


def catalog_reader(file):
    with open(file) as file_obj:
        result = {}
        for line in file_obj:
            dish_name = line.strip()
            ingridients = []
            for item in range(int(file_obj.readline())):
                ingridient = file_obj.readline()
                ingridients.append(ingridient.strip())
            ingridients_dicts = []
            for item in ingridients:
                some_dict = {}
                new_list = item.split(sep='|')
                some_dict['ingredient_name'] = new_list[0].strip()
                some_dict['quantity'] = new_list[1].strip()
                some_dict['measure'] = new_list[2].strip()
                ingridients_dicts.append(some_dict)
            result[dish_name] = ingridients_dicts
            file_obj.readline()
        return result


catalog = catalog_reader(file_name)
pprint(catalog, sort_dicts=False)
