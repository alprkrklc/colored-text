from enum import Enum

# Text colors.
class Color(Enum):
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    
# Text styles.
class Style(Enum):
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Resets current options.
RESET = '\033[0m'

def cprint(text, *args: Color | Style):    
    print(
        *[arg.value for arg in args], 
        text, 
        RESET, 
        sep=''
    )
