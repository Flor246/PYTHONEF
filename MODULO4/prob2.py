# Escriba una expresión regular para validar un correo
regex = r""

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']
for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("El email {email_example} es valido".format(email_example=example))
    else:
        print("El correo {email_example} es invalido".format(email_example=example)) 