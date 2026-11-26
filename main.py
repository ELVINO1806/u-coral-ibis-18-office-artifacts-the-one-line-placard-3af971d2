
import os


def main():
    text = "Stapler, c. 2019. Pressed steel, jammed. Ritual binding tool of the Accounts tribe; donor unknown, victim's thumb still attached to file 7B."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
