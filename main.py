from astronauts import Astronauts


def main():
    astronauts = Astronauts()
    if astronauts.were_found():
        astronauts.display()
        astronaut_name = input("Enter an astronaut name:")
        if astronauts.check_astronaut(astronaut_name):
            astronaut_description = astronauts.get_description(astronaut_name)
            if astronaut_description is not None:
                print(astronaut_description)
            else:
                print(f"Unable to get a description for: {astronaut_name}")
        else:
            print("This astronaut does not exist.")
    else:
        print("Error connecting to Astronaut's API")


if __name__ == "__main__":
    main()