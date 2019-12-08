import tkinter as tk


def run():
    main_window = tk.Tk()
    main_window.title("Klawisz")
    main_window.geometry('700x700')

    panel_width = 500
    panel_height = 500
    label_width = 100
    label_height = 25

    available_width = panel_width - label_width
    available_height = panel_height - label_height

    panel = tk.Frame(main_window, bg='#ffff00', height=500, width=500)
    panel.grid(row=0, column=1)

    label = tk.Button(panel, bg='#00ffff')
    label.place(width=100, height=25)

    vertical_var = tk.DoubleVar()
    horizontal_var = tk.DoubleVar()
    vertical_var.set(0)
    horizontal_var.set(0)

    def set_text():
        label.configure(text=f'x={horizontal_var.get()}, y={vertical_var.get()}')

    def move(val):
        # val jest aktualną wartością slidera, który wywołał tą funkcję
        # ale my tego nie potrzebujemy, bo mamy vertical_var i horizontal_var
        label.place(width=label_width, height=label_height,
                    x=horizontal_var.get() * available_width,
                    y=vertical_var.get() * available_height)
        set_text()

    slider_vertical = tk.Scale(main_window, variable=vertical_var, from_=0, to=1, resolution=0.01,
                               orient=tk.VERTICAL, showvalue=False, command=move)
    slider_vertical.grid(row=0, column=0, sticky=tk.NS)

    slider_horizontal = tk.Scale(main_window, variable=horizontal_var, from_=0, to=1, resolution=0.01,
                                 orient=tk.HORIZONTAL, showvalue=False, command=move)
    slider_horizontal.grid(row=1, column=1, sticky=tk.EW)

    set_text()

    main_window.mainloop()


if __name__ == '__main__':
    run()
