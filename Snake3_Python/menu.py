# menu 
# (might change this menu to a graphical interface later on)

def printStartMenu():
    print('''
        -----------
        |  SNAKE  |
        -----------
                            
        INSTRUKSJONER:
        - Styr slangen med tastene ASDW eller piltastene
        - Ikke treff kantene eller deg selv (slangen din)
        - Spise mat gir poeng:
                
                RØD sirkel      1 poeng
                GUL trekant     3 poeng
                HVIT skilpadde  5 poeng

        - Trykk Q for aa pause spillet (SHIFT + Q for aa avslutte)
          
        VELG DITT BRETT:
        1. lite
        2. middels
        3. stort
        '''
        # Tidligere versjon hadde et 4. valg:
        # 4. egendefinert vindu **
    )

def choose():
    return input("Valg: >> ")

def newChoice():
    print('Velg et tall fra menyen (+ Enter). Tallet 0 viser menyen igjen. ')
    return choose()


'''
**  TIDLIGERE hadde jeg mulighet for brukerstyrt vindusstoerrelse i main-fil
    elif choice == '4':
        fortsett_igjen = True
        while fortsett_igjen:
            width = int(input('Skriv inn bredde: '))
            height = int(input('Skriv inn hoyde: '))
            if (width < 250 or height < 250 or width > 1200 or height > 900):
                print('Bredde og hoyde maa være minst 250. Bredde max 1200 og hoyde max 900.')
            else:
                fortsett_igjen = False
        fortsett = False 
'''