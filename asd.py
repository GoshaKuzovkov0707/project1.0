from tkinter import *

tir = Tk()



can = Canvas(tir, width=600, height=600)

can.create_polygon((200, 0), 
                   (225, 90), 
                   (320, 100), 
                   (250, 125), 
                   (300, 250), 
                   (200, 160), 
                   (100, 250), 
                   (150, 125), 
                   (80, 100), 
                   (165, 90), fill='yellow')

# can.create_polygon((300, 300),
#                    (225, 90), 
#                    (320, 100), 
#                    (250, 125), 
#                    (300, 250), 
#                    (200, 175), 
#                    (100, 250), 
#                    (150, 125), 
#                    (80, 100), 
#                    (165, 90), fill='yellow')
# can.create_rectangle(200, 200, 400, 400)
# can.create_rectangle(240, 240, 440, 440)

# can.create_line(200, 200, 240, 240)
# can.create_line(400, 400, 440, 440)
# can.create_line(400, 200, 440, 240)
# can.create_line(200, 400, 240, 440)

can.pack()

tir.mainloop()