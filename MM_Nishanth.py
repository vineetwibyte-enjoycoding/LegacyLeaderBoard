import tkinter as tk

def calculate_cost():
  start = start_station.get()
  stop = stop_station.get()  

  if start in stn_sl:
    start_line = stn_sl
  else:
    start_line = stn_Rl

  if stop in stn_sl:
    stop_line = stn_sl
  else:
    stop_line = stn_Rl


  if start_line is stop_line:
    n_stops = abs(start_line.index(start) - start_line.index(stop))
  else:
    n_stops = start_line.index(start) - start_line.index('Ameerpet')
    n_stops = abs(n_stops) + abs(stop_line.index('Ameerpet') - stop_line.index(stop))
  
  
  cost = n_stops*10
  tax = 5/100*cost
  total_cost = cost + tax
  
  #This is a bonus offer if you travel onlu on the red line
  if start_line == stop_line == stn_Rl:
    cost = cost - (7/100*cost)

  
  costLabel.config(text = "COST(INCLUDING tax) = INR" + str(total_cost))
  
  pass


window = tk.Tk()
window.title("Hydrabad Metro Rail")
window.geometry("900x600+50+100")
window.configure(bg = "blue")

c = tk.Canvas(window, width = 850, height = 550, bg = "white")
c.pack()

# Blue Line

stn_sl = ['Nagole', 'Uppal', 'Stadium', 'NGRI', 'Habsiguda', 'Tarnaka', 'Mettuguda', 'Secundrabad', 'Begumpet', 'Ameerpet', 'Jubille Hills']

x_s = 50
y_s = 250
d_stn = 70
r_stn = 6

for stn in stn_sl:
  if stn != stn_sl[-1]:
    c.create_line(x_s, y_s, x_s + d_stn, y_s, width = 3, fill = 'blue')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, width = 2, fill = 'light blue')
  c.create_text(x_s, y_s + 30, text = stn, font = ('Arial', 7,'bold'), fill = 'blue')
  x_s = x_s + d_stn


# Red Line

stn_Rl = ['Miyapur', 'KPHB Colony', 'Kukatpally', 'Erragadda','Ameerpet', 'Panjagutta', 'Lakdi-ka-pul' , 'LB Nagar']

x_s = 680
y_s = 10
d_stn = 60
r_stn = 6

for stn in stn_Rl:
  if stn != stn_Rl[-1]:
    c.create_line(x_s, y_s, x_s, y_s + d_stn, width = 3, fill = 'red')
  c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, width = 2, fill = 'light pink')
  c.create_text(x_s + 40, y_s , text = stn, font = ('Arial', 7,'bold'), fill = 'red')
  y_s = y_s + d_stn


all_stations = stn_sl + stn_Rl
all_stations.remove('Ameerpet')

c.create_text(70, 90, text = 'Start', font=('Arial',10,'bold' ))
start_station = tk.StringVar()
drop_start = tk.OptionMenu(window, start_station, *all_stations)
drop_start.place(x = 70, y = 100)

c.create_text(270, 90, text = 'Destination', font=('Arial',10,'bold' ))
stop_station = tk.StringVar()
drop_stop = tk.OptionMenu(window, stop_station, *all_stations)
drop_stop.place(x = 250, y = 100)


button = tk.Button(window, text = 'Calculate Cost', command= calculate_cost)
button.pack()


costLabel = tk.Label(window, text = 'Cost : ', font = ('Helvetica', 15, 'bold'))
costLabel.pack()

c.create_text(150, 50, text= 'Travel on the RED line to get 7% discount', font= ('Arial',10))

tk.mainloop()

