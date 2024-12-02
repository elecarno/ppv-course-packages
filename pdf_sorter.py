import os

directory = "spa"

keywords = {
    "N5": "n5",
    "NH": "nh",
    "NAH": "ah"
}

types = {
    # Sciences & Mathematics
    "Paper1": "p1",
    "Paper2": "p2",
    "Paper-1": "p1",
    "Paper-2": "p2",
    "Section1": "s1",
    "Section2": "s2",
    "Section-1": "s1",
    "Section-2": "s2",
    # English
    "Critical Reading": "cr",
    "Critical-Reading": "cr",
    "Textual Analysis": "cr",
    "Reading-for-Understanding-Analysis-and-Evaluation": "ru",
    # Modern Languages
    "Listening-Transcript": "li_sp",
    "Directed-Writing": "dw",
    "Writing": "wr",
    "Reading": "re",
    "Listening": "li",
    "RUAE": "ru",
    # Geography
    "Global-Issues-and-Geographical-Skills": "gg",
    "Physical-and-Human-Environments": "ph",
    "OS-Map": "sp",
    "OS-map": "sp",
    # History
    "British-European-and-World-History": "bw",
    "Scottish-History": "sh",
    # Media
    "Analysis-of-media-content": "am",
    "Analysis-of-Media-Content": "am",
    "The-role-of-media": "rm",
    "The-Role-of-Media": "rm",
    # General
    "QP": "qp",
    "sp": "sp",
    "all": "all",
    "All": "all"
    # If type cannot be found, default to "all"
}

# Create a function to extract the year from a file name
def extract_year(filename):
    for year in range(1970, 2050, 1):
        if str(year) in filename:
            return str(year)

# Create a function to search for files containing the keywords in their names
def search_files_with_keywords(directory, keywords):
    # Create folders for each keyword
    for keyword in keywords.values():
        keyword_dir = os.path.join(directory, keyword)
        os.makedirs(keyword_dir, exist_ok=True)

        # Create folders for each year within keyword folders
        for year in range(1970, 2050, 1):
            year_dir = os.path.join(keyword_dir, str(year))
            os.makedirs(year_dir, exist_ok=True)

    # Iterate over all files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            # Check if any of the keywords are in the filename
            for original_keyword, keyword in keywords.items():
                if original_keyword in filename:
                    # Initialize type as "all"
                    type_value = "qp"
                    # Check if any of the types keywords are in the filename
                    for type_key, value in types.items():
                        if type_key in filename:
                            type_value = value
                            break  # Exit loop if type is found
                    # Construct the new filename
                    year = extract_year(filename)
                    new_filename = f"{directory}_{keyword}_{year}_{type_value}.pdf"
                    # Append "_mi" if "mi" was in the original filename
                    if "mi_" in filename:
                        new_filename = new_filename.replace(".pdf", "_mi.pdf")
                    # Get the full path of the file
                    file_path = os.path.join(root, filename)
                    new_file_path = os.path.join(root, new_filename)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                    # Move the file to the respective year folder within keyword folder
                    os.replace(new_file_path, os.path.join(directory, keyword, year, new_filename))
    
    # Delete empty year folders
    for keyword in keywords.values():
        keyword_dir = os.path.join(directory, keyword)
        for year in range(1970, 2050, 1):
            year_dir = os.path.join(keyword_dir, str(year))
            if not os.listdir(year_dir):
                os.rmdir(year_dir)
                print(f"Deleted empty folder: '{year_dir}'")

# Call the function to search for files containing the keywords
search_files_with_keywords(directory, keywords)
