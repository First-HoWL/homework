while True:
    text = input('Ваш рядок:')

    newtext = text.replace(" ", "").lower() # lower потрібен тому що велика літера не дорівнює маленькій

    rozgornytiitext = newtext[::-1]

    if rozgornytiitext == newtext:
        print('Поліндром')
    else:
        print('Не поліндром')