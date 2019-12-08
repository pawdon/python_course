import tkinter as tk


def simple01():
    main_window = tk.Tk()
    main_window.title("First application")
    main_window.geometry('800x600')

    label_01 = tk.Label(main_window, text='Hello world', bg='#ff8811', fg='#5555ff',
                        font=("Times", "24", "bold italic"))
    label_01.pack(side=tk.LEFT)

    def command_01():
        print(f'Clicked')
        label_01.configure(text='Clicked')

    button_01 = tk.Button(main_window, text='My button', font=("Times", "24"), command=command_01)
    button_01.pack(side=tk.LEFT)

    main_window.mainloop()


if __name__ == '__main__':
    simple01()
