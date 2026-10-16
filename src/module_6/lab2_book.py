# Refer to this module's readme
def main():
    with open("alice.txt", "r", encoding='utf-8') as f:
        contents = f.readlines()

    chapter1 = contents[52:272]
    with open("chapter1.txt", "w", encoding='utf-8') as f:
        f.writelines(chapter1)

main()