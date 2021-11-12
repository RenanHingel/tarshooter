import tarfile
import os
import sys

# Script details - feel free to contact!
author_name = "Renan Hingel"
author_contact = "renanhingel@gmail.com"
git_url = "https://github.com/RenanHingel/tarshooter"
script_version = "1.0.3"

# ANSI color codes
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_RED = "\033[1;31m"
CEND = "\033[0m"


def makedir(directory):
    # Check if the informed directory exists
    is_exist = os.path.exists(directory)

    # If it does not exist, create it and print to console terminal
    if not is_exist:
        os.makedirs(directory)
        print("Created directory: " + LIGHT_CYAN + directory + CEND + ".")


def untar(file, directory):
    # Open the compressed file
    file = tarfile.open(file)

    # Print the compressed file contents
    print("Files found: " + LIGHT_CYAN + str(file.getnames()) + "." + CEND)
    print("------------------------------------------------------------------------")
    # Extract and close
    file.extractall(directory)
    file.close()


def tshoot(workdir):
    # We will create a command dictionary so we can store the commands found later
    commands_dict = {}

    # The delimiter variable will help us find the useful lines
    delimiter = "******** show "
    last_line = 0
    # What we want to clean from the file
    clean = "******** "
    clean2 = " *******"

    # Open the file supplied by the user
    with open(workdir, "r") as raw_text:
        read_text = raw_text.readlines()

        # Now, enumerate all lines inside the file and remove the \n characters with strip
    for index, line in enumerate(read_text):
        line_count = index + 1
        last_line = index + 1
        strip_line = line.strip()
        if delimiter in strip_line:
            strip_line = strip_line.replace(clean, "")
            strip_line = strip_line.replace(clean2, "")
            # After cleaning the lines, append them to our dictionary
            commands_dict[strip_line] = line_count

    while True:
        command = input("Enter a " + LIGHT_CYAN + "[specific command]" + CEND + ", " + LIGHT_CYAN + "[all]"
                        + CEND + "to see all available commands or " + LIGHT_CYAN + "[1]"
                        + CEND + " to quit to main menu: ")

        if command == "1":
            break

        if command == "all":
            print('Available commands: ' + LIGHT_CYAN + ', '.join(
                str(key) for key, value in commands_dict.items()) + CEND)
            command = input("Enter a " + LIGHT_CYAN + "[specific command]" + CEND + ": ")
        try:
            current_line = commands_dict[command]

            next_key = None
            dict_iter = iter(commands_dict)
            for key in dict_iter:
                if key == command:
                    next_key = next(dict_iter, None)

            try:
                next_line = (commands_dict[next_key] - 1)

            except:
                next_line = last_line

            output_interval = range(current_line, next_line)
            lines_to_read = list(output_interval)
            print("------------------------------------------------------------------------")
            print(f"Output for: {command}")
            for position, line in enumerate(read_text):
                if position in lines_to_read:
                    print(line.strip())
            print("------------------------------------------------------------------------")
        except:
            print(f'Command "{command}" not found.')


if __name__ == '__main__':
    try:
        print("------------------------------------------------------------------------")
        print(LIGHT_CYAN + '88888888888    d88888888888b.     .d8888b. 888    888 .d88888b.  .d88888b.8888888888888888888888888888b.  ')
        print('    888       d88888888   Y88b   d88P  Y88b888    888d88P" "Y88bd88P" "Y88b   888    888       888   Y88b ')
        print(CYAN + '    888      d88P888888    888   Y88b.     888    888888     888888     888   888    888       888    888 ')
        print('    888     d88P 888888   d88P    "Y888b.  8888888888888     888888     888   888    8888888   888   d88P ')
        print(LIGHT_BLUE + '    888    d88P  8888888888P"        "Y88b.888    888888     888888     888   888    888       8888888P"  ')
        print(BLUE + '    888   d88P   888888 T88b           "888888    888888     888888     888   888    888       888 T88b   ')
        print('    888  d8888888888888  T88b    Y88b  d88P888    888Y88b. .d88PY88b. .d88P   888    888       888  T88b  ')
        print('    888 d88P     888888   T88b    "Y8888P" 888    888 "Y88888P"  "Y88888P"    888    8888888888888   T88b ' + CEND)
        print("------------------------------------------------------------------------")
        while True:
            print(LIGHT_CYAN + "TarShooter" + CEND + " can be run in two different modes: " + LIGHT_CYAN + "extract [1]" + CEND + " or " + LIGHT_CYAN + "read [2]" + CEND + ".")
            print("Select " + LIGHT_CYAN + "[1]" + CEND + " extract mode to extract a .gz file.")
            print("Select " + LIGHT_CYAN + "[2]" + CEND + " to read the troubleshoot file.")
            print("Select " + LIGHT_CYAN + "[3]" + CEND + " or press " + LIGHT_CYAN + "CTRL + C" + CEND + " at any time to exit.")
            print("------------------------------------------------------------------------")

            menu_option = input("Choose an option " + LIGHT_CYAN + "[1-3]" + CEND + ": ")

            if menu_option == "1":
                print("You have selected" + LIGHT_CYAN + " [1] extract mode" + CEND + ".")
                print("------------------------------------------------------------------------")
                file_path = input("File path: ")
                dest_dir = input("Destination directory: ")
                makedir(dest_dir)
                untar(file_path, dest_dir)

            if menu_option == "2":
                print("You have selected" + LIGHT_CYAN + " [2] read mode" + CEND + ".")
                print("------------------------------------------------------------------------")
                work_dir = input("Please provide a path to the troubleshooting file: ")
                if os.path.isfile(work_dir):
                    print("File " + LIGHT_CYAN + work_dir + CEND + " found!")
                    tshoot(work_dir)
                else:
                    print("Could not locate the informed file. Please check the syntax.")

            if menu_option == "3":
                os._exit(1)

    except KeyboardInterrupt:
        print(LIGHT_RED + "Break sequence CTRL + C detected. Script will exit." + CEND)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
