import requests

# API Key and Search Engine ID
API_KEY = "YOUR API_KEY"
SEARCH_ENGINE_ID = "YOUR SEARCH ENGINE ID"

# Base URL for Google Custom Search
url = 'YOUR URL'


# Function to perform the search
def search(query, search_type=None):
    params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'lr': 'lang_en',
        'cr': 'countryIN|countryUS'
    }

    if search_type == 'image':
        params['searchType'] = 'image'

    # Make the GET request to the API
    response = requests.get(url, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        results = response.json().get('items', [])

        # If no results found
        if not results:
            print("No results found.")
            return

        # Print the search results
        for item in results:
            print(item['link'])
    else:
        print(f"Error: {response.status_code}, {response.text}")


# Function to search for information
def search_info():
    query = input("Enter your search query for information: ").lower()
    search(query, 'information')


# Function to search for images
def search_images():
    query = input("Enter your search query for images: ").lower()
    search(query, 'image')


# Function to exit the program
def exit_code():
    print("Thank you for using our Search Engine!")
    print("Exiting the program.")
    exit()


# Function to display the menu
def display_menu():
    print("Automated Search Engine Using API")
    print("WELCOME")
    print("\nWhat would you like to Search for Today?")
    print("\nMenu:")
    print("1. Search for Information")
    print("2. Search for Images")
    print("3. Exit")


# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            search_info()
        elif choice == '2':
            search_images()
        elif choice == '3':
            exit_code()
        else:
            print("Invalid choice. Please enter an option between 1 and 3.")


if __name__ == "__main__":
    main()