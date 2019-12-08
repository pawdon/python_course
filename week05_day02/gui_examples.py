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

    button_02 = tk.Button(main_window, text='Add label', font=("Times", "24"), command=command_02)
    button_02.pack(side=tk.RIGHT)

    main_window.mainloop()


if __name__ == '__main__':
    simple01()
