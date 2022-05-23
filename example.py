from colored_text import Color, Style, cprint

def main():
    text = 'Hello World!'

    # Colored print.
    cprint(text, Color.YELLOW)

    # Colored, bolded and underlined print.
    cprint(text, Color.CYAN, Style.BOLD, Style.UNDERLINE)
    
    # Regular print.
    print(text)

if __name__ == '__main__':
    main()
