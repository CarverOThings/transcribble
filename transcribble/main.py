from modules.transcribble import transcribble


def main():
    try:
        transcribble()
    except Exception as e:
        print(e)
        exit()


if __name__ == "__main__":
    main()
