import tkinter as tk

def calculate_fare():
   start = start_station.get()
   stop = stop_station.get()

   if start in stn_VL:
      start_line = stn_VL

   elif start in stn_YL:
     start_line = stn_YL


   elif start in stn_BL:
     start_line = stn_BL
   else:
      start_line = stn_PL
  
   if stop in stn_VL:
      stop_line = stn_VL

   elif stop in stn_YL:
      stop_line= stn_YL

   elif stop in stn_BL:
     stop_line= stn_BL
   else:
      stop_line = stn_PL
  
   if start_line is stop_line:
      n_stops = abs(start_line.index(stop) - start_line.index(start))
      if start in stn_VL:
       start_index= start_line.index(start)
       start_x= x_pos_VL[start_index]
       start_y= y_pos_VL[start_index]
       stop_index= stop_line.index(stop)
       stop_x= x_pos_VL[stop_index]
       stop_y= y_pos_VL[stop_index]
       c.create_line(start_x, start_y, stop_x, stop_y, fill="lime", width=2)

      if start in stn_PL:
          start_index= start_line.index(start)
          start_x1= x_pos_PL[start_index]
          start_y1= y_pos_PL[start_index]
          stop_index= stop_line.index(stop)
          stop_x1= x_pos_PL[stop_index]
          stop_y1= y_pos_PL[stop_index]
          c.create_line(start_x1, start_y1, stop_x1, stop_y1, fill="lime",width=2)

      if start in stn_YL:
         start_index= start_line.index(start)
         start_x= x_pos_YL[start_index]
         start_y= y_pos_YL[start_index]
         stop_index= stop_line.index(stop)
         stop_x= x_pos_YL[stop_index]
         stop_y= y_pos_YL[stop_index]
         c.create_line(start_x, start_y, stop_x, stop_y, fill="lime",width=2)

      if start in stn_BL:
         start_index= start_line.index(start)
         start_x= x_pos_BL[start_index]
         start_y= y_pos_BL[start_index]
         stop_index= stop_line.index(stop)
         stop_x= x_pos_BL[stop_index]
         stop_y= y_pos_BL[stop_index]
         c.create_line(start_x, start_y, stop_x, stop_y, fill="lime",width=2)

   else:
     if start_line== stn_VL and stop_line == stn_PL or start_line== stn_PL and stop_line == stn_VL:
       
       n_stops = abs(start_line.index('Khan Market') - start_line.index(start))
       n_stops = n_stops + abs(stop_line.index(stop) - stop_line.index('Khan Market'))
       if start in stn_VL:
         start_index= start_line.index(start)
         start_x= x_pos_VL[start_index]
         start_y= y_pos_VL[start_index]
         stop_index= start_line.index('Khan Market')
         stop_x= x_pos_VL[stop_index]
         stop_y= y_pos_VL[stop_index]
         stop_index_2= stop_line.index(stop)
         stop_index_2x= x_pos_PL[stop_index_2]
         stop_index_2y= y_pos_PL[stop_index_2]
         c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
         c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)

       if start in stn_PL:
          start_index= start_line.index(start)
          start_x= x_pos_PL[start_index]
          start_y= y_pos_PL[start_index]
          stop_index= stop_line.index('Khan Market')
          stop_x= x_pos_VL[stop_index]
          stop_y= y_pos_VL[stop_index]
          stop_index_2= stop_line.index(stop)
          stop_index_2x= x_pos_VL[stop_index_2]
          stop_index_2y= y_pos_VL[stop_index_2]
          c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
          c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
     


     elif start_line == stn_YL and stop_line == stn_VL or start_line==stn_VL and stop_line==stn_YL:
       n_stops = abs(start_line.index('Kashmere Gate') - start_line.index(start))
       n_stops = n_stops + abs(stop_line.index(stop) - stop_line.index('Kashmere Gate'))

       if start in stn_VL:
          start_index= start_line.index(start)
          start_x= x_pos_VL[start_index]
          start_y= y_pos_VL[start_index]
          stop_index= start_line.index('Kashmere Gate')
          stop_x= x_pos_VL[stop_index]
          stop_y= y_pos_VL[stop_index]
          stop_index_2= stop_line.index(stop)
          stop_index_2x= x_pos_YL[stop_index_2]
          stop_index_2y= y_pos_YL[stop_index_2]
          c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
          c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)

       if start in stn_YL:
           start_index= start_line.index(start)
           start_x= x_pos_YL[start_index]
           start_y= y_pos_YL[start_index]
           stop_index= stop_line.index('Kashmere Gate')
           stop_x= x_pos_VL[stop_index]
           stop_y= y_pos_VL[stop_index]
           stop_index_2= stop_line.index(stop)
           stop_index_2x= x_pos_VL[stop_index_2]
           stop_index_2y= y_pos_VL[stop_index_2]
           c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
           c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
         
     elif start_line == stn_YL and stop_line == stn_PL:
       n_stops = abs(start_line.index('Kashmere Gate') - start_line.index(start))
       n_stops= n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Khan Market'))
       
       start_index= start_line.index(start)
       start_x= x_pos_YL[start_index]
       start_y= y_pos_YL[start_index]
       stop_index= stn_VL.index('Kashmere Gate')
       stop_x= x_pos_VL[stop_index]
       stop_y= y_pos_VL[stop_index]
       stop_index_2= stn_VL.index('Khan Market')
       stop_index_2x= x_pos_VL[stop_index_2]
       stop_index_2y= y_pos_VL[stop_index_2]
       stop_index_3=stop_line.index(stop)
       stop_index_3x= x_pos_PL[stop_index_3]
       stop_index_3y= y_pos_PL[stop_index_3]
       c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
       c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
       c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)
     
     elif start_line == stn_PL and stop_line == stn_YL:
      n_stops = abs(start_line.index('Khan Market') - start_line.index(start))
      n_stops= n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Kashmere Gate'))

      start_index= start_line.index(start)
      start_x= x_pos_PL[start_index]
      start_y= y_pos_PL[start_index]
      stop_index= stn_VL.index('Khan Market')
      stop_x= x_pos_VL[stop_index]
      stop_y= y_pos_VL[stop_index]
      stop_index_2= stn_VL.index('Kashmere Gate')
      stop_index_2x= x_pos_VL[stop_index_2]
      stop_index_2y= y_pos_VL[stop_index_2]
      stop_index_3=stop_line.index(stop)
      stop_index_3x= x_pos_YL[stop_index_3]
      stop_index_3y= y_pos_YL[stop_index_3]
      c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
      c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
      c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)


     elif start_line == stn_YL and stop_line == stn_BL or start_line==stn_BL and stop_line==stn_YL:
      n_stops = abs(start_line.index('Rajiv Chowk') - start_line.index(start))
      n_stops = n_stops + abs(stop_line.index(stop) - stop_line.index('Rajiv Chowk'))


      if start in stn_YL:
          start_index= start_line.index(start)
          start_x= x_pos_YL[start_index]
          start_y= y_pos_YL[start_index]
          stop_index= stop_line.index('Rajiv Chowk')
          stop_x= x_pos_BL[stop_index]
          stop_y= y_pos_BL[stop_index]
          stop_index_2= stop_line.index(stop)
          stop_index_2x= x_pos_BL[stop_index_2]
          stop_index_2y= y_pos_BL[stop_index_2]
          c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
          c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)

      if start in stn_BL:
           start_index= start_line.index(start)
           start_x= x_pos_BL[start_index]
           start_y= y_pos_BL[start_index]
           stop_index= start_line.index('Rajiv Chowk')
           stop_x= x_pos_BL[stop_index]
           stop_y= y_pos_BL[stop_index]
           stop_index_2= stop_line.index(stop)
           stop_index_2x= x_pos_YL[stop_index_2]
           stop_index_2y= y_pos_YL[stop_index_2]
           c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
           c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)

     elif start_line == stn_PL and stop_line == stn_BL or start_line==stn_BL and stop_line==stn_PL:
      n_stops = abs(start_line.index('Ashram') - start_line.index(start))
      n_stops = n_stops + abs(stop_line.index(stop) - stop_line.index('Ashram'))

      if start in stn_PL:
          start_index= start_line.index(start)
          start_x= x_pos_PL[start_index]
          start_y= y_pos_PL[start_index]
          stop_index= stop_line.index('Ashram')
          stop_x= x_pos_BL[stop_index]
          stop_y= y_pos_BL[stop_index]
          stop_index_2= stop_line.index(stop)
          stop_index_2x= x_pos_BL[stop_index_2]
          stop_index_2y= y_pos_BL[stop_index_2]
          c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
          c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)

      if start in stn_BL:
           start_index= start_line.index(start)
           start_x= x_pos_BL[start_index]
           start_y= y_pos_BL[start_index]
           stop_index= start_line.index('Ashram')
           stop_x= x_pos_BL[stop_index]
           stop_y= y_pos_BL[stop_index]
           stop_index_2= stop_line.index(stop)
           stop_index_2x= x_pos_PL[stop_index_2]
           stop_index_2y= y_pos_PL[stop_index_2]
           c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
           c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
        
     elif start_line == stn_VL and stop_line ==stn_BL:
       n1= start_line.index(start)
       n2= start_line.index('Kashmere Gate')
       n3= start_line.index('Khan Market')
       if abs(n1-n2)> abs(n1-n3) or abs(n1-n2)== abs(n1-n3) :
         n_stops = abs(start_line.index('Khan Market') - start_line.index(start))
         n_stops = n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Ashram'))
         
         start_index= start_line.index(start)
         start_x= x_pos_VL[start_index]
         start_y= y_pos_VL[start_index]
         stop_index= stn_VL.index('Khan Market')
         stop_x= x_pos_VL[stop_index]
         stop_y= y_pos_VL[stop_index]
         stop_index_2= stn_BL.index('Ashram')
         stop_index_2x= x_pos_BL[stop_index_2]
         stop_index_2y= y_pos_BL[stop_index_2]
         stop_index_3=stop_line.index(stop)
         stop_index_3x= x_pos_BL[stop_index_3]
         stop_index_3y= y_pos_BL[stop_index_3]
         
         c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
         c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
         c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)
       else:
        n_stops = abs(start_line.index('Kashmere Gate') - start_line.index(start))
        n_stops = n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Rajiv Chowk'))

        start_index= start_line.index(start)
        start_x= x_pos_VL[start_index]
        start_y= y_pos_VL[start_index]
        stop_index= stn_VL.index('Kashmere Gate')
        stop_x= x_pos_VL[stop_index]
        stop_y= y_pos_VL[stop_index]
        stop_index_2= stn_BL.index('Rajiv Chowk')
        stop_index_2x= x_pos_BL[stop_index_2]
        stop_index_2y= y_pos_BL[stop_index_2]
        stop_index_3=stop_line.index(stop)
        stop_index_3x= x_pos_BL[stop_index_3]
        stop_index_3y= y_pos_BL[stop_index_3]

        c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
        c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
        c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)
         
     elif start_line==stn_BL and stop_line==stn_VL:
       n1= start_line.index(start)
       n2= start_line.index('Rajiv Chowk')
       n3= start_line.index('Ashram')
       if abs(n1-n2)> abs(n1-n3) or abs(n1-n2)== abs(n1-n3) :
         n_stops = abs(start_line.index('Ashram') - start_line.index(start))
         n_stops = n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Khan Market'))
         
         start_index= start_line.index(start)
         start_x= x_pos_BL[start_index]
         start_y= y_pos_BL[start_index]
         stop_index= stn_BL.index('Ashram')
         stop_x= x_pos_BL[stop_index]
         stop_y= y_pos_BL[stop_index]
         stop_index_2= stn_VL.index('Khan Market')
         stop_index_2x= x_pos_VL[stop_index_2]
         stop_index_2y= y_pos_VL[stop_index_2]
         stop_index_3=stop_line.index(stop)
         stop_index_3x= x_pos_VL[stop_index_3]
         stop_index_3y= y_pos_VL[stop_index_3]

         c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
         c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
         c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)
       else:
         n_stops = abs(start_line.index('Rajiv Chowk') - start_line.index(start))
         n_stops = n_stops + 2 + abs(stop_line.index(stop) - stop_line.index('Kashmere Gate'))
         start_index= start_line.index(start)
         start_x= x_pos_BL[start_index]
         start_y= y_pos_BL[start_index]
         stop_index= stn_BL.index('Rajiv Chowk')
         stop_x= x_pos_BL[stop_index]
         stop_y= y_pos_BL[stop_index]
         stop_index_2= stn_VL.index('Kashmere Gate')
         stop_index_2x= x_pos_VL[stop_index_2]
         stop_index_2y= y_pos_VL[stop_index_2]
         stop_index_3=stop_line.index(stop)
         stop_index_3x= x_pos_VL[stop_index_3]
         stop_index_3y= y_pos_VL[stop_index_3]
         
         c.create_line(start_x,start_y,stop_x,stop_y,fill="lime",width=2)
         c.create_line(stop_x,stop_y,stop_index_2x,stop_index_2y,fill="lime",width=2)
         c.create_line(stop_index_2x,stop_index_2y,stop_index_3x,stop_index_3y,fill='lime',width=2)
        
   
   fare = n_stops*20
   fare_label.configure(text = 'FARE - INR ' + str(fare))
   
window = tk. Tk( )
window.title("Delhi's Kiddie Metro Map")
window.geometry("600x600+50+100")
window.resizable(False, False)
window.configure(bg = 'salmon')

c = tk. Canvas(window, width = 500, height = 500)
c.configure(bg= 'black')
c.pack( )

stn_VL = ['Moolchand', 'Sarai', 'Kashmere Gate', 'JLN', 'Khan Market', 'Jasolla',
'Okhla']
stn_PL=  ['Shiv Vihar','Gokulpuri','Khan Market','Jaffrabad','Ashram','Shakurpur','INA Market']
stn_YL=  ['Model Town','Civil lines', 'Kashmere Gate', 'Chandi Chowk', 'Rajiv Chowk', 'Saket','Minar']
stn_BL=  ['Karol Bagh','Mandi house','Rajiv Chowk','Kakarduma','Ashram','Yamuna','Pragati']

x_s = 50
y_s = 200
d_stn = 70
r_stn = 6
x_pos_VL=[]
y_pos_VL=[]
for stn in stn_VL:
 if stn != stn_VL[-1]:
  c.create_line(x_s, y_s, x_s + d_stn, y_s, width = 2, fill = 'violet')
 c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='violet')
 c.create_text(x_s, y_s + 30 , text = stn, fill = 'violet',font='Helvetica 6 bold')
 x_pos_VL.append(x_s+r_stn)
 y_pos_VL.append(y_s+r_stn)
 x_s = x_s + d_stn

all_stations= stn_VL
start_station=tk.StringVar()
drop_start=tk.OptionMenu(window, start_station,*all_stations)
drop_start.place(x=50, y=400)


stop_station=tk.StringVar()
drop_stop=tk.OptionMenu(window, stop_station,*all_stations)
drop_stop.place(x=150, y=400)

button=tk.Button(window, text='Calculate Fare', command= calculate_fare)
button.pack()
fare_label=tk.Label(window, text='Fare =',font=('Helvetica 6 bold'))
fare_label.pack()


x_s = 330
y_s = 40
d_stn = 70
r_stn = 6
x_pos_PL=[]
y_pos_PL=[]
for stn in stn_PL:
 if stn != stn_PL[-1]:
  c.create_line(x_s, y_s, x_s , y_s+ d_stn, width = 2, fill = 'deep pink')
 c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='deep pink')
 c.create_text(x_s +40 , y_s , text = stn, fill = 'deep pink',font='Helvetica 6 bold')
 x_pos_PL.append(x_s+r_stn)
 y_pos_PL.append(y_s+r_stn)
 y_s = y_s + d_stn

all_stations= stn_VL + stn_PL
start_station=tk.StringVar()
drop_start=tk.OptionMenu(window, start_station,*all_stations)
drop_start.place(x=50, y=400)


stop_station=tk.StringVar()
drop_stop=tk.OptionMenu(window, stop_station,*all_stations)
drop_stop.place(x=150, y=400)

x_s = 190
y_s = 40
d_stn = 70
r_stn = 6
x_pos_YL=[]
y_pos_YL=[]
for stn in stn_YL:
 if stn != stn_YL[-1]:
  c.create_line(x_s, y_s, x_s , y_s+ d_stn, width = 2, fill = 'yellow')
 c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='yellow')
 c.create_text(x_s -40 , y_s , text = stn, fill = 'yellow',font='Helvetica 6 bold')
 x_pos_YL.append(x_s+r_stn)
 y_pos_YL.append(y_s+r_stn)
 y_s = y_s + d_stn
 

all_stations= stn_VL + stn_PL + stn_YL
start_station=tk.StringVar()
drop_start=tk.OptionMenu(window, start_station,*all_stations)
drop_start.place(x=50, y=400)


stop_station=tk.StringVar()
drop_stop=tk.OptionMenu(window, stop_station,*all_stations)
drop_stop.place(x=150, y=400)

x_s = 50
y_s = 340
d_stn = 70
r_stn = 6
x_pos_BL=[]
y_pos_BL=[]
for stn in stn_BL:
 if stn != stn_BL[-1]:
  c.create_line(x_s, y_s, x_s+ d_stn , y_s, width = 2, fill = 'deep sky blue')
 c.create_oval(x_s - r_stn, y_s - r_stn, x_s + r_stn, y_s + r_stn, fill='deep sky blue')
 c.create_text(x_s , y_s +20, text = stn, fill = 'deep sky blue',font= 'Helvetica 6 bold')
 x_pos_BL.append(x_s+r_stn)
 y_pos_BL.append(y_s+r_stn)
 x_s = x_s + d_stn

all_stations= stn_VL + stn_PL + stn_YL + stn_BL
all_stations.remove('Kashmere Gate')
all_stations.remove('Rajiv Chowk')
all_stations.remove('Ashram')
all_stations.remove('Khan Market')
start_station=tk.StringVar()
drop_start=tk.OptionMenu(window, start_station,*all_stations)
drop_start.place(x=50, y=400)


stop_station=tk.StringVar()
drop_stop=tk.OptionMenu(window, stop_station,*all_stations)
drop_stop.place(x=150, y=400)



tk.mainloop()