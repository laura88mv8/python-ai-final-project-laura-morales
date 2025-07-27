# Global song database
song_database = {}

# Display menu
def display_menu():
    print("Developer Menu:")
    print("1. Load Song Data")
    print("2. View Songs Database")
    print("3. Delete a Song")
    print("4. Modify a Song")
    print("5. Exit")

# Load songs from file
def load_data():
    global song_database
    filename = input("Enter the file name to load songs: ")

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split('","')
                parts = [p.strip('"\n ') for p in parts]

                if len(parts) != 5:
                    print(f"Skipping line due to incorrect format: {line}")
                    continue

                title, artist, album, genre, duration = parts

                song = {
                    "title": title,
                    "album": album,
                    "genre": genre,
                    "duration": duration
                }

                if artist in song_database:
                    song_database[artist].append(song)
                else:
                    song_database[artist] = [song]

        print(f"Songs loaded from {filename}.")
    except FileNotFoundError:
        print("Error: File not found.")

# View songs
def view_database():
    if not song_database:
        print("No data loaded.")
        return

    print("Songs Database:")
    print("Title\t\t\t\tArtist\t\t\t\tGenre")
    print("=" * 72)

    for artist, songs in song_database.items():
        for song in songs:
            title = song["title"]
            genre = song["genre"]
            print(f'"{title}"\t\t"{artist}"\t\t"{genre}"')

# Delete a song
def delete_song():
    global song_database

    artist = input("Enter the artist's name of the song to delete: ")
    title = input("Enter the title of the song to delete: ")

    if artist in song_database:
        for song in song_database[artist]:
            if song["title"] == title:
                song_database[artist].remove(song)
                if not song_database[artist]:
                    del song_database[artist]
                print(f'Deleted "{title}" by "{artist}" from the database.')
                return
    print("Song not found.")

# ✅ Modify a song
def modify_song():
    global song_database

    artist = input("Enter the artist's name of the song to modify: ")
    title = input("Enter the title of the song to modify: ")

    if artist in song_database:
        for song in song_database[artist]:
            if song["title"] == title:
                print(f'Current details:\nTitle: "{title}", Album: "{song["album"]}", Genre: "{song["genre"]}", Duration: "{song["duration"]}"')

                new_album = input("Enter new album (or press Enter to keep current): ")
                new_genre = input("Enter new genre (or press Enter to keep current): ")
                new_duration = input("Enter new duration (or press Enter to keep current): ")

                if new_album:
                    song["album"] = new_album
                if new_genre:
                    song["genre"] = new_genre
                if new_duration:
                    song["duration"] = new_duration

                print(f'Modified "{title}" by "{artist}".')
                return

    print("Song not found.")

# Main loop
def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            load_data()
        elif choice == "2":
            view_database()
        elif choice == "3":
            delete_song()
        elif choice == "4":
            modify_song()
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
