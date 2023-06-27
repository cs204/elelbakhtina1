try:
    while True:
        text = input()
        if text == "stop":
            break
        text = text.replace(":)", "🙂")
        text = text.replace(":(", "🙁")

        print(text)

except EOFError:
    pass