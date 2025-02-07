import fitz

search_text = 'João Antonio Schuh'

doc = fitz.open('C:/Users/JoaoSchuh/Desktop/DirecaoDefensiva.pdf')

text = doc[0].get_text()

start_index = text.find(search_text)

print(start_index)

print(text)
    
