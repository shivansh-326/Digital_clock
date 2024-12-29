from tkinter import *
import datetime

def update_time():
    current_time = datetime.datetime.now()
    
    # Time
    hour = current_time.strftime('%I')
    minute = current_time.strftime('%M')
    second = current_time.strftime('%S')
    am_pm = current_time.strftime('%p')
    
    # Date
    date = current_time.strftime('%d')
    month = current_time.strftime('%B')
    year = current_time.strftime('%Y')
    day = current_time.strftime('%A')
    
    # Update labels
    time_label.config(text=f"{hour}:{minute}:{second} {am_pm}")
    date_label.config(text=f"{day}, {month} {date}, {year}")
    
    # Update every second
    time_label.after(1000, update_time)

# Create the main window
root = Tk()
root.title('Digital Clock')
root.geometry('400x200')
root.config(bg='black')

# Time label
time_label = Label(root, text='', font=('Helvetica', 40), fg='white', bg='black')
time_label.pack(pady=20)

# Date label
date_label = Label(root, text='', font=('Helvetica', 18), fg='white', bg='black')
date_label.pack()

# Run the update_time function to start the clock
update_time()

root.mainloop()

