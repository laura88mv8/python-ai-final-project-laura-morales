songs_db = {}

def load_database():
    global songs_db
    try:
        with open("songs_database.txt", "r") as file:
            for line in file:
                parts = line.strip().split('","')
                parts = [p.strip('"') for p in parts]
                if len(parts) == 5:
                    title, artist, album, genre, duration = parts
                    song = {
                        "title": title,
                        "album": album,
                        "genre": genre,
                        "duration": duration
                    }
                    if artist in songs_db:
                        songs_db[artist].append(song)
                    else:
                        songs_db[artist] = [song]
    except FileNotFoundError:
        print("Error: songs_database.txt file not found.")

def search_by_title():
    title = input("\nEnter the song title to search: ")
    print(f"\nSearching for songs with title: '{title}'")
    found = False
    for artist, songs in songs_db.items():
        for song in songs:
            if song["title"].lower() == title.lower():
                print(f"Found: '{song['title']}' by {artist} (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
                found = True
                break
        if found:
            break
    if not found:
        print(f"Song title '{title}' does not exist in the database.")

def search_by_artist():
    artist = input("\nEnter the artist's name to search: ")
    print(f"\nSearching for songs by artist: '{artist}'")
    found = False
    for artist_name, songs in songs_db.items():
        if artist_name.lower() == artist.lower():
            for song in songs:
                print(f"Found: '{song['title']}' (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
            found = True
            break
    if not found:
        print(f"No songs found for artist '{artist}'.")

def main():
    load_database()
    
    while True:
        print("\n--- User Menu ---")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            search_by_title()
        elif choice == "2":
            search_by_artist()
        elif choice == "3":
            print("\nExiting the Songs Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
