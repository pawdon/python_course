import tkinter as tk


def simple01():
    main_window = tk.Tk()
    main_window.title("First application")
    main_window.geometry('800x600')

    label_01 = tk.Label(main_window, text='Hello world', bg='#ff8811', fg='#5555ff',
                        font=("Times", "24", "bold italic"))
    label_01.pack(side=tk.LEFT)

    def command_01():
        print(label_01.cget('font'), type(label_01.cget('font')))
        if label_01.cget('text') == 'Hello world':
            label_01.configure(text='Clicked')
        else:
            label_01.configure(text='Hello world')

    button_01 = tk.Button(main_window, text='My button', font=("Times", "24"), command=command_01)
    button_01.pack(side=tk.LEFT)

    def command_02():
        tk.Label(main_window, text='add').pack(side=tk.BOTTOM)
        button_01.invoke()

    button_02 = tk.Button(main_window, text='Add label', font=("Times", "24"), command=command_02)
    button_02.pack(side=tk.RIGHT)
    button_02.invoke()
    button_02.invoke()

    main_window.mainloop()


def simple02():
    main_window = tk.Tk()
    main_window.title("Second application")

    canvas_height = 200
    canvas_width = 200

    c1 = tk.Canvas(main_window, bg='#ffff00', height=canvas_height, width=canvas_width)
    c1.grid(row=0, column=0, sticky=tk.NSEW)

    c2 = tk.Canvas(main_window, bg='#ff9911', height=canvas_height, width=canvas_width)
    c2.grid(row=0, column=1, sticky=tk.NSEW)

    c3 = tk.Canvas(main_window, bg='#00ffff', height=canvas_height, width=canvas_width)
    c3.grid(row=1, column=0, sticky=tk.NSEW)

    c4 = tk.Canvas(main_window, bg='#ff00ff', height=canvas_height, width=canvas_width)
    c4.grid(row=1, column=1, sticky=tk.NSEW)

    for x in [main_window, c1, c2, c3, c4]:
        tk.Grid.rowconfigure(x, 0, weight=1)
        tk.Grid.columnconfigure(x, 0, weight=1)

    for i in range(5):
        tk.Label(c3, bg='#00ff00', text=f'0{i}').grid(row=0, column=i, sticky=tk.NSEW)
        tk.Label(c3, bg='#00ff00', text=f'{i}0').grid(row=i, column=0, sticky=tk.NSEW)

    tk.Label(c3, bg='#00ff00', text=f'---col 2---').grid(row=1, column=2, rowspan=2, columnspan=1, sticky=tk.NSEW)
    tk.Label(c3, bg='#00ff00', text=f'-------col 2+3-------').grid(row=3, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW)

    check_button_int = tk.IntVar()
    label_str = tk.StringVar()

    def command_01():
        print(check_button_int.get())
        label_str.set(f'Value {check_button_int.get()}')

    tk.Checkbutton(c2, text='checkbutton', command=command_01, variable=check_button_int).pack()\

    tk.Label(c1, textvariable=label_str).pack()

    label2_str = tk.StringVar()
    label2_str.set('Zero')
    tk.Label(c4, textvariable=label2_str).pack(side=tk.TOP)

    radio_button_value = tk.IntVar()
    def radio_button_command():
        label2_str.set(f'Value {radio_button_value.get()}')

    radio_button_value2 = tk.IntVar()
    tk.Radiobutton(c4, text="Option A1", variable=radio_button_value, value=1, command=radio_button_command).pack(side=tk.TOP)
    tk.Radiobutton(c4, text="Option A2", variable=radio_button_value, value=2, command=radio_button_command).pack(side=tk.TOP)
    tk.Radiobutton(c4, text="Option A3", variable=radio_button_value, value=2, command=radio_button_command).pack(side=tk.TOP)

    tk.Radiobutton(c4, text="Option B4", variable=radio_button_value2, value=4, command=radio_button_command).pack(side=tk.TOP)
    tk.Radiobutton(c4, text="Option B5", variable=radio_button_value2, value=5, command=radio_button_command).pack(side=tk.TOP)

    main_window.mainloop()


def simple03():
    main_window = tk.Tk()
    main_window.title("Second application")

    tk.Grid.rowconfigure(main_window, 0, weight=1)
    tk.Grid.rowconfigure(main_window, 1, weight=1)
    tk.Grid.columnconfigure(main_window, 0, weight=1)
    tk.Grid.columnconfigure(main_window, 1, weight=1)

    canvas_height = 200
    canvas_width = 200

    c1 = tk.Frame(main_window, bg='#ffff00', height=canvas_height, width=canvas_width)
    c1.grid(row=0, column=0, sticky=tk.NSEW)

    c2 = tk.Frame(main_window, bg='#ff9911', height=canvas_height, width=canvas_width)
    c2.grid(row=0, column=1, sticky=tk.NSEW)

    c3 = tk.Frame(main_window, bg='#00ffff', height=canvas_height, width=canvas_width)
    c3.grid(row=1, column=0, sticky=tk.NSEW)

    c4 = tk.Frame(main_window, bg='#ff00ff', height=canvas_height, width=canvas_width)
    c4.grid(row=1, column=1, sticky=tk.NSEW)

    tk.Label(c1, text='HAHA', bg='#ffffff').pack(expand=True, fill=tk.BOTH)

    tk.Grid.rowconfigure(c3, 0, weight=1)
    tk.Grid.rowconfigure(c3, 1, weight=1)
    tk.Grid.rowconfigure(c3, 2, weight=10)  # weight ma znaczenie jesli jest nadmiarowe miejsce
    tk.Grid.rowconfigure(c3, 3, weight=1)
    tk.Grid.rowconfigure(c3, 4, weight=1)
    tk.Grid.columnconfigure(c3, 0, weight=1)
    tk.Grid.columnconfigure(c3, 1, weight=1)
    tk.Grid.columnconfigure(c3, 2, weight=1)
    tk.Grid.columnconfigure(c3, 3, weight=1)
    tk.Grid.columnconfigure(c3, 4, weight=1)
    for i in range(5):
        tk.Label(c3, bg='#00ff00', text=f'0{i}').grid(row=0, column=i, sticky=tk.NSEW)  # sticky is for expanding
        tk.Label(c3, bg='#00ff00', text=f'{i}0').grid(row=i, column=0, sticky=tk.NSEW)

    tk.Label(c3, bg='#00ff00', text=f'---col 2---').grid(row=1, column=2, rowspan=2, columnspan=1, sticky=tk.NSEW)
    tk.Label(c3, bg='#00ff00', text=f'-------col 2+3-------').grid(row=3, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW)

    main_window.mainloop()


def run():
    main_window = tk.Tk()
    main_window.title("Klawisz")
    main_window.geometry('700x700')

    panel = tk.Frame(main_window, bg='#ffff00', height=500, width=500)
    panel.grid(row=0, column=1)
    panel.pack_propagate(0)  # ta magiczna linijka powoduje ze panel nie zmienia rozmiaru przez zawartosc

    label_frame = tk.Frame(panel, width=100, height=25, bg='#ff9900')
    label_frame.pack()
    label_frame.pack_propagate(0)

    tk.Frame(label_frame, width=25, height=25, bg='#ff0000').pack(side=tk.RIGHT)
    # label = tk.Button(panel, bg='#00ffff')
    # label.place(width=100, height=25)

    vertical_var = tk.DoubleVar()
    slider_vertical = tk.Scale(main_window, variable=vertical_var, from_=0, to=1, resolution=0.01, orient=tk.VERTICAL, showvalue=False)
    slider_vertical.grid(row=0, column=0, sticky=tk.NS)

    horizontal_var = tk.DoubleVar()
    slider_horizontal = tk.Scale(main_window, variable=horizontal_var, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, showvalue=False)
    slider_horizontal.grid(row=1, column=1, sticky=tk.EW)

    main_window.mainloop()


if __name__ == '__main__':
    simple03()
