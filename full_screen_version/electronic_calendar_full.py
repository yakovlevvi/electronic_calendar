from tkinter import *
from tkinter import messagebox as mb 
import calendar
import datetime


def back(event):
    global month, year, background, bg, era, morf
    month -=1
    canvas1.delete(background)
    if month == 0:
        month = 12
        year -= 1
    bg = PhotoImage(file = "files\months_full\{}.png".format(month))
    canvas1.create_image(0, 0, image = bg, anchor = "nw")
    canvas1.create_image(30, 30, image = era, anchor = "nw")
    canvas1.create_image(w-30, 30, image = morf, anchor = "ne")
    fill()


def next(event):
    global month, year, background, bg, era, morf
    canvas1.delete(background)
    month += 1
    if month == 13:
        month = 1
        year += 1
    bg = PhotoImage(file = "files\months_full\{}.png".format(month))
    canvas1.create_image(0, 0, image = bg, anchor = "nw")
    canvas1.create_image(30, 30, image = era, anchor = "nw")
    canvas1.create_image(w-30, 30, image = morf, anchor = "ne")
    fill()


def show_info(event):
    global days, month, year, holiday_photo, monthhh, era, morf, file1
    button_text = event.widget.cget('text')
    try:
        filename = 'files\docs\{}\{}.{}.txt'.format(str(month), str(button_text),str(month))
        file1 = open(filename, "r", encoding='utf-8')
    except FileNotFoundError:
        file1.close()
        mb.showinfo(title=None, message="Нет информации о празднике в этот день")
        event.widget["state"] = DISABLED
    else:
        fig = Toplevel()
        fig.title('В этот день:')
        fig.geometry('1600x600')
        fig.resizable(False, False)
        fig.wm_iconbitmap('files\calendar.ico')
        
        canvas_photo = Canvas(fig, width=400, height =600)
        canvas_photo.place(x=50, y=0)
        holiday_photo = PhotoImage(file = "files\pics\{}\{}.png".format(str(month), str(button_text)))
        canvas_photo.create_image(0, 0, anchor=NW, image = holiday_photo)
        canvas_text = Canvas(fig, width=1150, height =600)
        canvas_text.place(x=450, y=0)
        canvas_text.create_image(50, 30, anchor=NW, image = era)
        canvas_text.create_image(1100, 30, image = morf, anchor = "ne")
        
        line1 = file1.readline()
        
        monthhh = ''
        if calendar.month_name[month] == 'January':
            monthhh = 'января'
        if calendar.month_name[month] == 'February':
            monthhh = 'февраля'
        if calendar.month_name[month] == 'March':
            monthhh = 'марта'
        if calendar.month_name[month] == 'April':
            monthhh = 'апреля'
        if calendar.month_name[month] == 'May':
            monthhh = 'мая'
        if calendar.month_name[month] == 'June':
            monthhh = 'июня'
        if calendar.month_name[month] == 'July':
            monthhh = 'июля'
        if calendar.month_name[month] == 'August':
            monthhh = 'августа'
        if calendar.month_name[month] == 'May':
            monthhh = 'мая'
        if calendar.month_name[month] == 'September':
            monthhh = 'сентября'
        if calendar.month_name[month] == 'October':
            monthhh = 'октября'
        if calendar.month_name[month] == 'November':
            monthhh = 'ноября'
        if calendar.month_name[month] == 'December':
            monthhh = 'декабря'
        font_size = 24
        canvas_text.create_text(575, 200, text=str(button_text)+' '+monthhh, anchor = N, justify='center', font=("Century Gothic", font_size))
        
        lens = list()
        for line in line1:
            lens.append(len(line.rstrip()))
        if len(lens) >= 60:
            font_size = 20
        if len(lens) >= 80:
            font_size = 16
        if len(lens) >= 100:
            font_size = 12
        if len(lens) >= 120:
            font_size = 11
        if len(lens) >= 140:
            font_size = 10
        
        canvas_text.create_text(575, 240, text=line1, anchor = N, justify='center', font=("Century Gothic", font_size))
        canvas_text.create_line(300, 290, 850, 290, fill='black', width=2)

        line2 = file1.readlines()
        n = 0
        for line in line2:
            canvas_text.create_text(50, 300+n, text=line.strip(), anchor = NW, justify='left', font=("Century Gothic", 12))
            n+=20

        canvas_text.create_text(575, 100, text='ВОЕННЫЙ ИННОВАЦИОННЫЙ ТЕХНОПОЛИС "ЭРА" \n Лаборатория гидрометеорологического и геофизического обеспечения', 
                                anchor = S, fill='red', justify='center', font=("Century Gothic", 14))
        file1.close()


def fill():
    global file1
    monthhh = ''
    if calendar.month_name[month] == 'January':
        monthhh = 'Январь'
    if calendar.month_name[month] == 'February':
        monthhh = 'Февраль'
    if calendar.month_name[month] == 'March':
        monthhh = 'Март'
    if calendar.month_name[month] == 'April':
        monthhh = 'Апрель'
    if calendar.month_name[month] == 'May':
        monthhh = 'Май'
    if calendar.month_name[month] == 'June':
        monthhh = 'Июнь'
    if calendar.month_name[month] == 'July':
        monthhh = 'Июль'
    if calendar.month_name[month] == 'August':
        monthhh = 'Август'
    if calendar.month_name[month] == 'May':
        monthhh = 'Май'
    if calendar.month_name[month] == 'September':
        monthhh = 'Сентябрь'
    if calendar.month_name[month] == 'October':
        monthhh = 'Октябрь'
    if calendar.month_name[month] == 'November':
        monthhh = 'Ноябрь'
    if calendar.month_name[month] == 'December':
        monthhh = 'Декабрь'
    
    info_label['text'] = monthhh + ', ' + str(year) + ' г.'
    
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        back_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        back_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]

    for n in range(month_days):
        days[n + week_day]['text'] = n + 1
        days[n + week_day]['fg'] = 'black'
        days[n + week_day]['activeforeground'] = 'black'
        days[n + week_day]['disabledforeground'] = 'black'
        #button_text = event.widget.cget('text') 
        if year == now.year and month == now.month and n == now.day:  #сегодняшний день
            days[n + week_day - 1]['bg'] = '#FFCBA0'  #сегодняшний день
            days[n + week_day - 1]['activebackground'] = '#99FF00'
            days[n + week_day - 1]['fg'] = 'black'  #сегодняшний день
            days[n + week_day - 1]['activeforeground'] = '#FF0079'
            days[n + week_day - 1]['disabledforeground'] = '#FF0079'
            days[n + week_day]['bg'] = '#A0FFFF'
            button_border = Frame(root, highlightbackground = "black", highlightthickness = 2, bd=0)
            # days[n + week_day - 1]['bd'] = '2p'
            # days[n + week_day - 1]['relief'] = 'ridge'
        else:
            days[n + week_day]['bg'] = '#A0FFFF'  #остальные дни
            days[n + week_day]['activebackground'] = '#A0FFFF'
        try:
            filename = 'files\docs\{}\{}.{}.txt'.format(str(month), str(n+1),str(month))
            file1 = open(filename, "r", encoding='utf-8')
        except FileNotFoundError:
            file1.close()
        else:
            file1.close()
            days[n + week_day]['fg'] = 'red'  #остальные дни
            days[n + week_day]['activeforeground'] = '#A60000'
            days[n + week_day]['disabledforeground'] = '#A60000'
            # days[n + week_day]['text'] = '*'+str(n + 1) + '*'

    for n in range(week_day):  #предыдущий месяц
        days[week_day - n - 1]['text'] = back_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        days[week_day - n - 1]['activeforeground'] = 'gray'
        days[week_day - n - 1]['disabledforeground'] = 'gray'
        days[week_day - n - 1]['bg'] = '#f3f3f3'
        days[week_day - n - 1]['activebackground'] = '#f3f3f3'
        try:
            filename = 'files\docs\{}\{}.{}.txt'.format(str(month), str(back_month_days - n),str(month))
            file1 = open(filename, "r", encoding='utf-8')
        except FileNotFoundError:
            file1.close()
        else:
            file1.close()
            days[week_day - n - 1]['fg'] = '#A60000'  #остальные дни
            days[week_day - n - 1]['activeforeground'] = '#A60000'
            days[week_day - n - 1]['disabledforeground'] = '#A60000'
            # days[n + week_day]['text'] = '*'+str(n + 1) + '*'
            days[week_day - n - 1]['bg'] = '#f3f3f3'
            days[week_day - n - 1]['activebackground'] = '#f3f3f3'
    
    for n in range(6*7 - month_days - week_day):  #следующий месяц
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray'
        days[week_day + month_days + n]['activeforeground'] = 'gray'
        days[week_day + month_days + n]['disabledforeground'] = 'gray'
        days[week_day + month_days + n]['bg'] = '#f3f3f3'
        days[week_day + month_days + n]['activebackground'] = '#f3f3f3'
        try:
            filename = 'files\docs\{}\{}.{}.txt'.format(str(month), str(n+1),str(month))
            file1 = open(filename, "r", encoding='utf-8')
        except FileNotFoundError:
            file1.close()
        else:
            file1.close()
            days[week_day + month_days + n]['fg'] = '#A60000'  #остальные дни
            days[week_day + month_days + n]['activeforeground'] = '#A60000'
            days[week_day + month_days + n]['disabledforeground'] = '#A60000'
            # days[n + week_day]['text'] = '*'+str(n + 1) + '*'
            days[week_day + month_days + n]['bg'] = '#f3f3f3'
            days[week_day + month_days + n]['activebackground'] = '#f3f3f3'


def next_year(event):
    global year, month, background, bg, era, morf
    year = 2024
    month = 1
    canvas1.delete(background)
    bg = PhotoImage(file = "files\months_full\{}.png".format(month))
    canvas1.create_image(0, 0, image = bg, anchor = "nw")
    canvas1.create_image(30, 30, image = era, anchor = "nw")
    canvas1.create_image(w-30, 30, image = morf, anchor = "ne")
    fill()


def current_year(event):
    global year, month, background, bg, era, morf
    year = now.year
    month = now.month
    canvas1.delete(background)
    bg = PhotoImage(file = "files\months_full\{}.png".format(month))
    canvas1.create_image(0, 0, image = bg, anchor = "nw")
    canvas1.create_image(30, 30, image = era, anchor = "nw")
    canvas1.create_image(w-30, 30, image = morf, anchor = "ne")
    fill()


def quit(event):
    root.destroy()


days = []
now = datetime.datetime.now()
year = now.year
month = now.month

root = Tk()
root.title('Электронный календарь')
root.wm_iconbitmap('files\calendar.ico')
root.attributes('-fullscreen',True)
#root.state('zoomed')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

canvas1 = Canvas(root, width=w, height = h) #1000 800
canvas1.grid(row=0, rowspan = 8, column=0, columnspan = 7)
bg = PhotoImage(file = "files\months_full\{}.png".format(month))
background = canvas1.create_image(0, 0, image = bg, anchor = "nw")

info_label = Label(root, text='0', height=1, fg='blue')
info_label.configure( font=("Century Gothic", 32))
info_label_canvas = canvas1.create_window(w//2, 50, anchor = "n", window = info_label)

back_button = Button(root, text = '<', width= 2, height = 2, borderwidth=0)
back_button.configure( font=("Century Gothic", 32))
back_button.bind('<Button-1>', back)
back_button_canvas = canvas1.create_window(50, h//2, anchor = "w", window = back_button)

next_button = Button(root, text='>', width=2, height=2, borderwidth=0)
next_button.bind('<Button-1>', next)
next_button.configure( font=("Century Gothic", 32)) 
next_button_canvas = canvas1.create_window(w-100, h//2, anchor = "w", window = next_button)

# Пн-Вс
canvas2 = Canvas(root, width=w-300, height = 30)
canvas2.place(x=150, y =125)
for n in range(7):
    weekdayyy = ''
    if n == 0:
        weekdayyy = 'Пн'
    if n == 1:
        weekdayyy = 'Вт'
    if n == 2:
        weekdayyy = 'Ср'
    if n == 3:
        weekdayyy = 'Чт'
    if n == 4:
        weekdayyy = 'Пт'
    if n == 5:
        weekdayyy = 'Сб'
    if n == 6:
        weekdayyy = 'Вс'

    lbl = Label(root, text=weekdayyy)
    lbl.configure( font=("Century Gothic", 16))
    if n == 5 or n == 6:
        lbl['fg'] = 'red'
    lbl_canvas = canvas2.create_window(70+((w-200)/7)*n, 0, 
                                       anchor = "n",
                                       window = lbl)

# Кнопки дней
for row in range(6):
    for col in range(7):
        lbl = Button(root, text = '0', width= 5, height = 1, borderwidth=0)
        lbl.configure( font=("Century Gothic", 24, 'bold'))
        lbl.bind('<Button-1>', show_info)
        lbl_canvas = canvas1.create_window(170+((w-200)/7)*col, 220+((h-200)/7)*row, anchor = "w", window = lbl)
        days.append(lbl)

# 2024
next_year_button = Button(root, text = 'Перейти на 2024 г.', height = 1, borderwidth=0)
next_year_button.bind('<Button-1>', next_year)
next_year_button.configure( font=("Century Gothic", 30))
next_year_button_canvas = canvas1.create_window(365, h-50, anchor = "s", window = next_year_button)

# Current year
current_year_button = Button(root, text = 'Перейти на текущий месяц', height = 1, borderwidth=0)
current_year_button.bind('<Button-1>', current_year)
current_year_button.configure( font=("Century Gothic", 30))
current_year_button_canvas = canvas1.create_window(w-465, h-50, anchor = "s", window = current_year_button)


# Close
close_button = Button(root, text = 'Закрыть календарь', height = 1, borderwidth=0, fg='red')
close_button.bind('<Button-1>', quit)
close_button.configure( font=("Century Gothic", 14))
close_button_canvas = canvas1.create_window(w-200, 50, anchor = "s", window = close_button)

# ERA logo
era = PhotoImage(file = "files\era.png")
canvas1.create_image(30, 30, image = era, anchor = "nw")

# ERA text
era_label = Label(root, text='ВОЕННЫЙ ИННОВАЦИОННЫЙ ТЕХНОПОЛИС "ЭРА" \n Лаборатория гидрометеорологического и геофизического обеспечения', 
                  fg='red')
era_label.configure( font=("Century Gothic", 14))
canvas1.create_window(w//2, 0, anchor = "n", window = era_label)

# MORF logo
morf = PhotoImage(file = "files\morf.png")
canvas1.create_image(w-30, 30, image = morf, anchor = "ne")


fill()

#Binds
root.bind('<Left>', back)
root.bind('<Right>', next)
root.bind('<space>', current_year)
root.bind('<Return>', next_year)
root.bind('<Escape>', quit)

root.mainloop()