import json
import random


f = open("words.json")
data = json.load(f)
klucze = list(data.keys())
######## Losowość \/ #########
def losowanie():
    los_temat = random.randint(0,len(klucze)-1)
    a = data[klucze[los_temat]]
    los_haslo = random.randint(0,len(a)-1)
    return  data[klucze[los_temat]][los_haslo],klucze[los_temat] # Zwraca słowo oraz temat ( użyte przy podpowiedzi w formie tematu)

class gra():
    def __init__(self,hp=10):
        self.hp = hp
        self.word = "x"
        self.secret  = "-"
        self.word_li = ['x']
        self.guessed = []
    def set_word(self, word):
        secret = ""
        word_li = list(word.lower())
        for j in word_li:
            if (j == " "):
                secret += " "
            else:
                secret += "_"
        self.secret = secret
        self.word_li = word_li
        self.word = word
    
    def guess_letter(self,letter):
        if letter == self.word:
            self.secret = letter
            return
        guessed = self.guessed
        secret = ""
        word_li = self.word_li
        if not letter in guessed: 
            self.guessed.append(letter)
            for j in word_li:
                if j in guessed:
                    secret += j
                elif (j == " "):
                    secret += " "
                else:
                    secret += "_"

            self.secret = secret
        if not letter in self.word_li:
            self.hp -= 1
        
            




def zagraj():
    haslo, temat = losowanie()
    a = gra(10)
    a.set_word(haslo)
    while(True):   
        print(f"\n"*50)
        print(f"Kategoria: {temat}")
        print(f"HP: {a.hp} \n{a.secret}")
        text = input(f"Podaj Litere \n> ").strip()
        a.guess_letter(text)
        if a.hp == 0:
            print("ale bambik. Nie masz życiek")
            break 
        if a.secret ==  a.word.lower():
            print(f'Zgadłeś hasło: "{a.secret}"!!! Gratulacje ;)')
            break
        
while(True):
    zagraj()
    
