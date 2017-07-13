import random
import re
def riddle():


    list_riddle=[{"answer":"I see!"},{"answer":"Oh o:"},{"answer":"okay!"},{"answer":"Hmm"},{"answer":"Mhmm?"},{"answer":"Hmm?"},{"answer":"o_o"},{"answer":"Ah, I see"},{"answer":"No"},{"answer":"Yes"},{"answer":"okay!"},{"answer":"Hahahah"},{"answer":"That's alright"},{"answer":"kay!"},{"answer":"Alright"},{"answer":"O:"},{"answer":"Bored"},{"answer":"Hahahah"},{"answer":"xD"},{"answer":"*sushhh*"}]
    random_riddle = random.choice(list_riddle)
    
    return random_riddle["answer"]
   


def talk(stuff):
   if 'hi' in stuff: return 'Hello'
   elif 'hello' in stuff: return 'hi'
   elif 'hey' in stuff: return 'hey!'
   elif 'how are you' in stuff: return 'I am doing good :)'
   elif 'noob' in stuff: return 'ya thats you xD'
   elif 'morning' in stuff: return 'Good Morning'
   elif 'night' in stuff: return 'Good Night'
   elif 'sleep' in stuff: return 'Go Sleep'
   elif 'hmm' in stuff: return 'mhm?'
   elif 'bored' in stuff: return 'o: I am random , talk to me!'
   elif 'lol' in stuff: return 'xD'
   elif 'lmao' in stuff: return 'LMAO'
   elif 'lel' in stuff: return 'lol'
   elif 'bye' in stuff: return 'bye'
   elif 'hibiki' in stuff: return 'Hello I am Hibiki :)'
   elif 'slap' in stuff: return 'slap you'
   elif 'invite' in stuff: return '<http://bit.ly/2t9MX1E> ;D'
   elif 'hug' in stuff: return '(づ￣ ³￣)づ'
   elif 'angry' in stuff: return '（▼へ▼メ）'
   elif 'flip' in stuff: return '(╯°□°）╯︵ ┻━┻'
   elif 'sorry' in stuff: return '๑•́ㅿ•̀๑) ᔆᵒʳʳᵞ'
   else:return riddle()
