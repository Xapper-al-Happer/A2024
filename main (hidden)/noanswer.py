import easyocr
import g4f
import time
import sys
from colorama import Fore, just_fix_windows_console
from g4f.Provider import (
    Bing
)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result_question = reader.readtext('1.png', detail = 0)

variable_question = "\n".join(result_question)

prequestion_list = [bcolors.BOLD + "this is something" + bcolors.BOLD]
# was Fore.RED
prequestion = "\n".join(prequestion_list)
final_question_list = [prequestion, "Answer the following question: ", variable_question]
final_question = "\n".join(final_question_list)

final_sendoff_list = [final_question]
final_sendoff = "\n".join(final_sendoff_list)
print(final_sendoff)

print("Generating answer")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.80)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
#print("\n")

g4f.debug.logging = False  # Enable logging
#g4f.check_version = False  # Disable automatic version checking
# print(g4f.version)
#print(g4f.Provider.Ails.params) 
# Automatic selection of provider
print("\n")

# Normal response
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.You,
    messages=[{"role": "user", "content": final_sendoff}]
)  # Alternative model setting

# g4f.models.gpt_4
# model=g4f.models.gpt_4
# was bing

just_fix_windows_console()

print(response)

input('Press ENTER to exit') 

# time.sleep(30)

# 35 s (deep)
# 