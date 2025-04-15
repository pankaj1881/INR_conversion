from word2number import w2n

def text_to_number_amount(text):
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
    if "paisa" in text.lower().split() or "paise" in text.lower().split():
        paisa_text = text.lower().split()
        index = -(paisa_text[::-1].index('and') + 1) or -(paisa_text[::-1].index('point') + 1) or -(paisa_text[::-1].index('rupees') + 1)
        paisa_text[index] = "[#]"
        rupee_amount = " ".join(paisa_text).split('[#]')[0]
        paisa_amount = " ".join(paisa_text).split('[#]')[1]

        try:
            paisa_amount = f"{w2n.word_to_num(paisa_amount):02d}"
        except ValueError:
            paisa_amount = 0  
    else:
        rupee_amount = text.lower()

    # to handle if point values are present for paisa
    if "point" in text.lower().split():
        paisa_text = text.lower().split()
        index = -(paisa_text[::-1].index('point') + 1)
        paisa_text[index] = "[#]"
        rupee_amount = " ".join(paisa_text).split('[#]')[0]
        paisa_amount = " ".join(paisa_text).split('[#]')[1]

        try:
            paisa_amount = f"{w2n.word_to_num(paisa_amount):02d}"
        except ValueError:
            paisa_amount = 0  
    else:
        rupee_amount = text.lower()


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
        return float(f"{total}.{paisa_amount}")
    elif total:
        return float(total)
    else:
        return 0  
