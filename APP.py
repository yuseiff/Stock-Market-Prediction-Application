
from sklearn.linear_model import LinearRegression
import joblib 
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox

def linear(open_price,high_price,low_price):
    """
    X: a 2D numpy array where the elements are [[open, high, low]]
    y_pred: the prediction value
    
    This fuction is responsible for predict the output using linear regression model
    """
    X = pd.DataFrame({
           'Open' : [open_price],
           'High' : [high_price],
           'Low' : [low_price]
        })
    
    linear_model = joblib.load('linear_model.pkl')
    y_pred = linear_model.predict(X)
    return y_pred


def GUI():
    window = Tk()
    window.title("AI project Stock Market Prediction")
    window.geometry("300x400")
    window.minsize(200,200)
    window.maxsize(600,600)
    

    label_open = Label(window, text="Open Price:")
    label_open.grid(row=0, column=0)
    entry_open = Entry(window)
    entry_open.grid(row=0, column=1)

    label_high = Label(window, text="High Price:")
    label_high.grid(row=1, column=0)
    entry_high = Entry(window)
    entry_high.grid(row=1, column=1)

    label_low = Label(window, text="Low Price:")
    label_low.grid(row=2, column=0)
    entry_low = Entry(window)
    entry_low.grid(row=2, column=1)
    
    def Predict():
        try:
            open_price = float(entry_open.get())
            high_price = float(entry_high.get())
            low_price = float(entry_low.get())

            prediction = linear(open_price, high_price, low_price)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for Open, High, and Low prices.")

        
        resultLabel.configure(text=prediction[0])
        

        
    predict_button = Button(window, text="Predict", command=Predict)
    predict_button.grid(row=3, column=2)
    
    label_close = Label(window, text='Close Price= ')
    label_close.grid(column=0,row=3)
    resultLabel= Label(window, text= '0')
    resultLabel.grid(column=1,row=3)
    window.mainloop()

GUI()
