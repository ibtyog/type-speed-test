import datetime
import tkinter as tk
import random
with open('phrases.txt') as file:
    phrases = file.readlines()



window = tk.Tk()
window.geometry('600x400')
missed_chars = 0
window.title('Speed typing test')

def text_change(*args):
    global start
    global missed_chars
    end_time = datetime.datetime.now()
    for char in range(0,len(test_area.get())):
        if test_area.get()[char] != title['text'][char]:
            missed_chars += 1
            sv.set(test_area.get()[:char])

    if test_area.get() == title['text']:
        end_text = (f'Ended in {str(end_time - start)[3:]}! {missed_chars} missed characters.')
        title['text'] = end_text
def start_test():
    global start
    test_area['state'] = 'normal'
    solution = random.choice(phrases).rstrip()
    title['text'] = solution
    test_area.focus_set()
    start = datetime.datetime.now()
sv = tk.StringVar()
sv.trace("w", text_change)




title = tk.Label(text="Typing speed test")
title.pack()

test_area = tk.Entry(textvariable=sv)
test_area['state'] = 'disabled'
test_area.pack()
start_button = tk.Button(text="Start", command=start_test)
start_button.pack()

window.mainloop()