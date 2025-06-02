import os
import shutil

# === CONFIGURATION ===
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FOLDER = os.path.join(SCRIPT_DIR, "Template")
BASE_OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, "Projects")

# Editable list of project categories (you can add any folder name here)
PROJECT_CATEGORIES = [
    "Maniac",
    "YouTube",
    "Client Work",
    "Personal Projects",
    "School Projects"
]

def list_categories():
    print("Choose a category:")
    for idx, category in enumerate(PROJECT_CATEGORIES, start=1):
        print(f"{idx}. {category}")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number of the category: "))
            if 1 <= choice <= len(PROJECT_CATEGORIES):
                return PROJECT_CATEGORIES[choice - 1]
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a number.")

def create_project():
    project_name = input("Enter the name of your project: ").strip()
    list_categories()
    category = get_user_choice()

    # Create the category folder inside the Projects folder if it doesn't exist
    category_folder = os.path.join(BASE_OUTPUT_FOLDER, category)
    os.makedirs(category_folder, exist_ok=True)

    # Full path where the new project will be placed (inside category folder)
    destination_project_folder = os.path.join(category_folder, project_name)

    if os.path.exists(destination_project_folder):
        print("⚠️ Project folder already exists! Choose a different name.")
        return

    # Copy template into the destination project folder
    try:
        shutil.copytree(TEMPLATE_FOLDER, destination_project_folder)
        print(f"✅ Project created at: {destination_project_folder}")
    except Exception as e:
        print(f"❌ Error copying template: {e}")
        return

    # Rename the project.kdenlive file
    original_kdenlive = os.path.join(destination_project_folder, "project.kdenlive")
    renamed_kdenlive = os.path.join(destination_project_folder, f"{project_name}.kdenlive")

    if os.path.exists(original_kdenlive):
        os.rename(original_kdenlive, renamed_kdenlive)
        print(f"📝 Renamed project.kdenlive to {project_name}.kdenlive")
    else:
        print("⚠️ project.kdenlive not found in the template folder.")

if __name__ == "__main__":
    create_project()
