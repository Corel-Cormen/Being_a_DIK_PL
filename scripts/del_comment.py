with open("new_script.rpy", "r", encoding="utf-8") as file:
    with open("new_script_2.rpy", "w", encoding="utf-8") as newFile:
        for line in file:
            if not line.startswith("#"):
                newFile.write(line)
