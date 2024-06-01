import os
import json

def folder_to_dict(folder_path, root_path):
    folder_dict = {}
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders = [subfolder for subfolder in os.listdir(item_path) if os.path.isdir(os.path.join(item_path, subfolder))]
            if subfolders:
                folder_dict[item] = folder_to_dict(item_path, root_path)
            else:
                files_dict = {}
                for filename in os.listdir(item_path):
                    file_path = os.path.join(item_path, filename)
                    file_name, file_extension = os.path.splitext(filename)
                    relative_file_path = os.path.relpath(file_path, root_path)
                    if file_name.endswith("_mi") and file_name[:-3] in files_dict:
                        files_dict[file_name[:-3]]['mi'] = {'name': file_name, 'path': relative_file_path}
                    elif file_name.endswith("_sp") and file_name[:-3] in files_dict:
                        files_dict[file_name[:-3]]['sp'] = {'name': file_name, 'path': relative_file_path}
                    else:
                        files_dict[file_name] = {'name': file_name, 'path': relative_file_path}
                folder_dict[item] = list(files_dict.values())
    return folder_dict

def main():
    root_dir = "./paper_files/DIR"
    course_name = os.path.basename(root_dir)
    parsed_data = folder_to_dict(root_dir, root_dir)

    # Create a dictionary with the course name as the first entry
    output_data = {
        "course": course_name,
        "data": parsed_data
    }

    # Define the path for the JSON files inside the root_dir
    json_output_path = os.path.join(root_dir, 'package_data.json')

    # Save the JSON data to a file
    with open(json_output_path, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"File structure parsed and saved to {json_output_path}")

    # Write the JSON data into a JSON file
    with open(json_output_path, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"JSON data written to {json_output_path}")

if __name__ == "__main__":
    main()
