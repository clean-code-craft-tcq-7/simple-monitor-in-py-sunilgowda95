def print_in_english(flag, *args):
    if flag == 1:
        print("Threshold WARNING : ", args)
        return
    print("Threshold BREACH : ", args)
    
def print_in_kannada(flag, *args):
    if flag == 0:
        print("ಮಿತಿ ಎಚ್ಚರಿಕೆ : ", *args)
        return
    print("ಮಿತಿ ಉಲ್ಲಂಘನೆ : ", *args)
        
language = "english"
print_message = print
if language == "english":
    print_message = print_in_english
elif language == "kannada":
    print_message = print_in_kannada