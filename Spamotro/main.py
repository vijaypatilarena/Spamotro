import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Loading the data from csv file into a pandas dataframe
raw_mail_data = pd.read_csv('mail_data.csv')

# Replace the null values with null strings
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')
mail_data.loc[mail_data['Category']=='spam', 'Category'] = 0
mail_data.loc[mail_data['Category']=='ham', 'Category'] = 1

# Separating the data as texts and label
X = mail_data['Message']
y = mail_data['Category']
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_features = feature_extraction.fit_transform(X)
y = y.astype('int')

model = LogisticRegression()

model.fit(X_features, y)


def predict_mail():
    input_msg = input_text.get("1.0", tk.END).strip()
    input_msg_features = feature_extraction.transform([input_msg])
    ans = model.predict(input_msg_features)
    if ans == 1:
        messagebox.showinfo("Prediction", "Ham mail")
    else:
        messagebox.showinfo("Prediction", "Spam mail")


# GUI Setup
window = tk.Tk()
window.title("Mail Classifier")

label = tk.Label(window, text="Enter the message:")
label.pack()

input_text = tk.Text(window, height=5, width=30)
input_text.pack()

predict_button = tk.Button(window, text="Predict", command=predict_mail)
predict_button.pack()

window.mainloop()
