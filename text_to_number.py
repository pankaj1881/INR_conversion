from word2number import w2n
from spello.model import SpellCorrectionModel

sp = SpellCorrectionModel(language='en')
sp.load(r"spell_check\model.pkl")


def text_to_number_amount(text):  

    text = sp.spell_correct(text= text.lower())["spell_corrected_text"]

    """"This code will convert amount upto crore into numbers (Designed for INR currancy).
        Example . . . . 
        text =  Five crore twenty lac fifty thousand and fifty paisa only : 

        text_to_number_amount(text)
        return value in float : 52050000.5 
    """
    
    lac_list = ["lakh", "lac","laksh"]
    crore_list = ["crore"]

    lac = ""
    crore = ""
    total = ""
    rupee_amount = ""
    paisa_amount = ""


    # to handle if paisa values are present
    rupees_keywords = {'rupee', 'rupees', 'rs', 'rupaya'}
    paisa_keywords = {'paisa', 'paise', 'pesa'}


    # text = ' '.join(text.lower().split())
    words = text.split()

    rupee_index = -1
    paisa_index = -1


    for i, word in enumerate(words):
        if word in rupees_keywords:
            rupee_index = i
        elif word in paisa_keywords:
            paisa_index = i

    if rupee_index != -1:
        
        rupee_amount = " ".join([word for word in words[:rupee_index]
                        if not word.startswith(())])

    if rupee_index != -1 and paisa_index != -1:
        paisa_amount = " ".join(words[rupee_index + 1:paisa_index])
    elif paisa_index != -1:  
        paisa_amount = " ".join(words[:paisa_index])


    for word in rupee_amount.split():
        if word in lac_list:
            lac = word
        elif word in crore_list:
            crore = word

    # to handle if values are presents in crore
    if crore:
        try:
            upto_crore = rupee_amount.split(crore)[0]
            crore_amount = w2n.word_to_num(upto_crore) * 10000000

            try:
                upto_lac = rupee_amount.split(crore)[1].split(lac)[0]
                lac_amount = w2n.word_to_num(upto_lac) * 100000
            except:
                lac_amount = 0
            try:
                upto_thousand = rupee_amount.split(crore)[1].split(lac)[1]
                thousand_amount = w2n.word_to_num(upto_thousand)
            except:
                thousand_amount = 0

            total = crore_amount + lac_amount + thousand_amount

        except ValueError:
            total = 0  

    # to handle if values are presents in lac
    elif lac and crore == "":
        try:
            upto_lac = rupee_amount.split(lac)[0]
            lac_amount = w2n.word_to_num(upto_lac) * 100000

            try:
                upto_thousand = rupee_amount.split(lac)[1]
                thousand_amount = w2n.word_to_num(upto_thousand)
            except:
                thousand_amount = 0

            total = lac_amount + thousand_amount
        except ValueError:
            total = 0  

    elif lac == "" and crore == "":
        try:
            total = w2n.word_to_num(rupee_amount)
        except ValueError:
            total = 0  

    if paisa_amount:
        return {"text_amount":text, "number_amount" : float(f"{total}.{w2n.word_to_num(paisa_amount):02d}")}
    elif total:
        return {"text_amount" : text, "number_amount" : float(total)}
    else:
        return {"text_amount" : text, "number_amount" : 0}
