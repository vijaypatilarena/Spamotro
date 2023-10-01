from tkinter import *
from textblob import TextBlob
def load_dataset(file_path):
    dataset = {}
    with open(file_path, 'r') as file:
        for line in file:
            correct_word, wrong_word = line.strip().split(':')
            dataset[wrong_word] = correct_word
    return dataset
def check_spelling():
    text = spell_check.get()
    blob = TextBlob(text)
    misspelled_words = []
    corrected_words = []
    for word in blob.words:
        if word.spellcheck()[0][0] != word:
            misspelled_words.append(word)
            corrected_words.append(word.spellcheck()[0][0])
            # Display the corrected words, if any
    if len(corrected_words) == 0:
        not_found_text.config(text="No misspelled words found!")
    else:
        corrected_text = "Corrected text:"
    for i in range(len(misspelled_words)):
        corrected_text += f"\n{misspelled_words[i]} -> {corrected_words[i]}"
        not_found_text.config(text=corrected_text)
    
window =Tk()
window.title("Spelling Checker")
window.geometry("1500x800")
window.config(background="yellow")

text_heading = Label(window, text="Spelling Checker", font=("Arial", 50, "bold"), bg="black", fg="lightpink")
text_heading.pack()

text_check = Label(window, text="Enter your text or word", font=("Arial", 30, "bold"), bg="black", fg="pink")
text_check.pack()

spell_check = Entry(window, font=("Arial", 20, "bold"), bg="orange", width=200)
spell_check.pack()

check_button = Button(window, text="Check!", font=("Arial", 30, "bold"), bg="orange", fg="white", command=check_spelling)
check_button.pack()

not_found_text = Label(window, text="", font=("Arial", 15, "bold"), bg="red")
not_found_text.pack()

# Load the dataset from an external file
dataset = load_dataset("aspell.txt")

window.mainloop()
