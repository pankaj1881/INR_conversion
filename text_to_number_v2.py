
def text_to_num(text):

    one_digit = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
        }
    
    two_digit = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90
        }
    

    num_dict = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
    "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "lac":100000 ,"#": 0
        }
    

    mul_lst = [100,1000,100000]

    text_num_list = [num_dict[i] for i in text.split()]
    common_elements = set(mul_lst) & set(text_num_list)

    text_list = text.split()

    if common_elements:
        # print("currecy word found!")
        lst_ = [num_dict[i] for i in text_list]
        lst_.insert(0,0)
        lst_.append(0)
        lst_.append(0)
        final_lst = []
        for i in range(len(lst_)-2):
            
            if lst_[i+2] in mul_lst and lst_[i] not in mul_lst:
                num1 = (lst_[i]+lst_[i+1]) * lst_[i+2]
                # print(num1)
                final_lst.append(num1)
            
            elif lst_[i+1] in mul_lst:
                if lst_[i-1] not in mul_lst:
                    pass
                else:
                    # print(lst_[i+1])
                    num1 = lst_[i]* lst_[i+1]
                    # print(num1)
                    final_lst.append(num1)

            elif lst_[i] not in mul_lst:
                    num1 = lst_[i]
                    # print(num1)
                    final_lst.append(num1)
            
        return sum(final_lst)
    
    else:
        # print("No currancy word found! ")
        text_list = text.split()
        text_list.append("#")
        lst_ = []

        for i,v in enumerate(text_list):
            if text_list[i-1] not in two_digit and text_list[i] in one_digit:
                lst_.append(num_dict[text_list[i]])

            elif text_list[i] in two_digit and text_list[i+1] in one_digit:
                lst_.append(num_dict[text_list[i]]+num_dict[text_list[i+1]])

            elif text_list[i-1] in two_digit and text_list[i] in one_digit:
                pass
            else:
                
                lst_.append(num_dict[v])

        return eval("".join([str(i) for i in lst_[:-1]]) )
    


def detect_rupee_paisa_part(text):
    # to handle if paisa values are present
    rupees_keywords = {'rupee', 'rupees', 'rs', 'rupaya','point'}
    paisa_keywords = {'paisa', 'paise', 'pesa'}


    # text = ' '.join(text.lower().split())
    words = ' '.join(text.lower().split()).split()


    rupee_amount = ""
    paisa_amount = ""

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

    return rupee_amount,paisa_amount



def extract_amount(text):

    rupee_amount,paisa_amount = detect_rupee_paisa_part(text.lower())

    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
        "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "lac":100000 ,"#": 0
            }
    rupee_amount = " ".join([i for i in rupee_amount.split() if i in num_dict or i in currancy_list])
    paisa_amount = " ".join([i for i in paisa_amount.split() if i in num_dict or i in currancy_list])


    # define currancy words
    currancy_list = ["rupee","paisa","paise","rupees","rs","rupay"]

    #checking if currancy word is present in input text
    common_elements = set(currancy_list) & set(text.split())

    result = ""

    if common_elements:

        try:
            x = f"{text_to_num(rupee_amount)}" # converting rupee amount part 
        except:
            x = ""
        try:
            y = f"{text_to_num(paisa_amount):02}" # converting paisa amount part
        except:
            y = ""

        if x and y=="":
            print("Onlr Rupee Found!")
            result = x
        elif x and y:
            print("Rupee and Paisa Found!")
            result = x+"."+y
        elif x == "" and y:
            print("Only Paisa Found!")
            result = "0."+y

    else:
        # if out of currancy list words are present then directly passing text
        try:
            print("No currancy word found!")
            x = f"{text_to_num(text.lower())}"
            result = x
        except:
            print("Fail to fetch amount.")

    return result
