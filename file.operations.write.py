with open("story.txt", "w") as f: #to start the story
    while True:
        text = input("What do you want to write")
        if text == "q":
            break
        f.write(text+"\n")


with open("story.txt", "a") as f: #to continue the story (append?)
    while True:
        text = input("What do you want to write")
        if text == "q":
            break
        f.write(text+"\n")