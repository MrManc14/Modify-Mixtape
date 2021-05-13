import os
import json
from JsonParser import JsonParser
from MixtapeModifier import MixtapeModifier


def main():
    mixtape = get_mixtape()
    changes = get_changes()

    mixtape_modifier = MixtapeModifier(mixtape, changes)
    mixtape_modifier.apply_changes()
    
    updated_mixtape = mixtape_modifier.get_mixtape()
    save_mixtape(updated_mixtape)


def get_mixtape():
    current_working_directory = os.getcwd()
    mixtape_file = '{}/../data/mixtape.json'.format(current_working_directory)
    return JsonParser(mixtape_file).get()


def get_changes():
    current_working_directory = os.getcwd()
    changes_file = '{}/../data/changes.json'.format(current_working_directory)
    return JsonParser(changes_file).get()


def save_mixtape(mixtape):
    current_working_directory = os.getcwd()
    output_file = '{}/../data/output.json'.format(current_working_directory)
    file = open(output_file, 'w')
    json.dump(mixtape, file, indent=2)
    file.close()


if __name__ == "__main__":
    main()
