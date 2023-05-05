import tkinter as tk

class GameTile(tk.Frame):
    value: int
    key: tuple[int]
    exposed: bool
    flagged: bool
    depressed: bool
    current: bool
    active: bool
    image_label: tk.Label

    def __init__(self, master, mine: bool = False):
        super().__init__(master, width = 20, height = 20, relief=tk.RAISED, bd=2)        

        if mine == True:
            self.value = -1
        else:
            self.value = 0
        self.exposed = False
        self.flagged = False
        self.depressed = False
        self.current = False
        self.active = False
        self.pack_propagate(0)
        self.image_label = tk.Label(self, height=20, width = 20)#, text = self.value
        self.bind_events()
        self.image_label.pack()
    
    def bind_events(self):
        self.image_label.bind('<ButtonPress>', self.click_press)
        self.image_label.bind('<ButtonRelease>', self.click_release)

    def unbind(self):
        self.image_label.bind('<ButtonPress>', '')
        self.image_label.bind('<ButtonRelease>', '')

    def click_press(self, event: tk.Event):
        if not self.flagged:
            self.master.current_key = self.key
            self.master.active = True
            if self.exposed:            
                self.master.press_surrounding(self)
            else:
                self.image_label.bind('<Leave>', self.leave) #bind enter/leave events when pressed
                self.image_label.bind('<Enter>', self.enter)
                if event.num == 1:
                    self.press()

    def leave(self, event: tk.Event):
        if self.key == self.master.current_key:
            self.active = False
            if not self.exposed:
                self.unpress()

    def enter(self, event: tk.Event):
        if self.key == self.master.current_key:
            self.active = True
            self.press()

    def click_release(self, event: tk.Event):
        self.image_label.bind('<Enter>', '') #unbind enter/leave events for this tile on release
        self.image_label.bind('<Leave>', '')

        if self.key == self.master.current_key and self.master.active:
            mouse_button = event.num
            if mouse_button == 1:
                self.master.primary_click(self)
            else:
                self.master.secondary_click(self)                
        else:
            self.unpress()

        #reset current click status
        self.master.current_key = None
        self.master.active = False

    '''def press_exposed(self):
        self.master.press_surrounding(self)'''

    def expose(self):
        self.exposed = True
        self.press()
        # no image for zero
        if self.value != 0:
            img = self.master.settings.get_image(self.value)
            self.image_label.image = img
            self.image_label.config(image=img)

    def press(self):
        self.depressed = True
        self.config(relief=tk.SUNKEN)

    def unpress(self):
        if not self.exposed:
            self.depressed = False
            self.config(relief=tk.RAISED)

    def flag_tile(self):
        if not self.exposed:
            self.flagged = True
            img = self.master.settings.get_image('flag')
            self.image_label.image = img
            self.image_label.config(image=img)

    def unflag_tile(self):
        if not self.exposed and self.flagged:
            self.flagged = False
            self.image_label.image = None
            self.image_label.config(image=None)

    def incorrect(self):
        if not self.exposed and self.flagged:
            img= self.master.settings.get_image('x')
            self.image_label.image = img
            self.image_label.config(image=img)

    def selected_mine(self):
        self.config(bg='red')
        self.image_label.config(bg='red')

