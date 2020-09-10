import json


class ExportFile:

    def export_all_to_json(self, json_content: str):
        """This one exports all band data to json file"""

        try:
            name = json_content.get('main').get('Name')
            file_name = name.strip().replace(' ', '_').lower() + '.json'
            file_path = f'exports/{file_name}'
        except Exception as e:
            print(f'Could not create the file name: {e}')

        try:
            # TODO: save to new directory
            with open(file_name, 'w', encoding='utf-8') as f:
                json.dump(json_content, f, indent=4, sort_keys=True)
        except Exception as e:
            print(f'Could not export info for for {name} to {file_path}: {e}')

        print(f'Successfully exported all info for {name} to {file_path}.')
