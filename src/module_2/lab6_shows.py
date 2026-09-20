# Refer to this module's readme
SHOWS = ["Avatar: the last airbender" , "Ben 10" , "Arthur" , "Spongebob Squarepants" , "Phineas and ferb" , "Kim Possible" , "Jimmy Neutron" , "the Proud Family"]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
    

    print(', '.join(cleaned_shows))

main()
