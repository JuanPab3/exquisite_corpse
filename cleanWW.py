import os

def clean_chat(name_c:str):

    file_path = f'/media/jpi/Data/Plataforma_Bogota/HACKTIVIDAD-AUTOMATAS_CELULARES/predict_chat/clean_chats/{name_c}_chat.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        pass


    with open(f'chats/{name_c}.txt','r') as f:


        # Delete date
        for i in f:
            count = 0
            for j in i:
                if j == ',':
                    count += 1
                    break
                else:
                    count += 1
            # Delete time
            n_line = i[count+9:-1]


            # Delete UserName
            count2 = 0
            for i in n_line:
                if i == ":":
                    count2 += 1
                    break
                else:
                    count2 += 1
            n_line = n_line[count2:]


            #Remove unnesesary signs
            n_line = n_line.lower()
            # n_line = n_line.replace('.','')
            # n_line = n_line.replace(',','')
            # n_line = n_line.replace('?','')
            n_line = n_line.replace('*','')
            n_line = n_line.replace('~','')
            n_line = n_line.replace('(','')
            n_line = n_line.replace(')','')
            n_line = n_line.replace('-','')
            n_line = n_line.replace('_','')
            n_line = n_line.replace('\n','')


            # Last filter
            words  = n_line.split(" ")
            condition = 0
            for word in words:
                if ('http' in word) or ('<media' in word) or ('omitted>' in word)  or (len(word) > 25):# or (len(n_line) <= 0):
                   condition += 1
                else:
                    continue

            # Write in file

            if (condition == 0) and (len(n_line)>0):
                with open(f'clean_chats/{name_c}_chat.txt','a+') as f2:
                    f2.write(f'{n_line} ')


def clean_clau(name_c:str):

    file_path = f'/media/jpi/Data/Plataforma_Bogota/HACKTIVIDAD-AUTOMATAS_CELULARES/predict_chat/clean_chats/{name_c}_chat.txt'
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        pass


    with open(f'chats/{name_c}.txt','r') as f:


        # Delete date
        for i in f:
            count = 0
            for j in i:
                if j == ':':
                    count += 1
                    break
                else:
                    count += 1
            # Delete time
            n_line = i[count:-1]


            # Delete UserName
            count2 = 0
            for i in n_line:
                if i == ":":
                    count2 += 1
                    break
                else:
                    count2 += 1
            n_line = n_line[count2:]


            #Remove unnesesary signs
            n_line = n_line.lower()
            # n_line = n_line.replace('.','')
            # n_line = n_line.replace(',','')
            # n_line = n_line.replace('?','')
            n_line = n_line.replace('*','')
            n_line = n_line.replace('~','')
            n_line = n_line.replace('(','')
            n_line = n_line.replace(')','')
            n_line = n_line.replace('-','')
            n_line = n_line.replace('_','')
            n_line = n_line.replace('\n','')


            # Last filter
            words  = n_line.split(" ")
            condition = 0
            for word in words:
                if ('http' in word) or ('<multimedia' in word) or ('omitido>' in word)  or (len(word) > 25):# or (len(n_line) <= 0):
                   condition += 1
                else:
                    continue

            # Write in file

            if (condition == 0) and (len(n_line)>0):
                with open(f'clean_chats/{name_c}_chat.txt','a+') as f2:
                    f2.write(f'{n_line} ')
