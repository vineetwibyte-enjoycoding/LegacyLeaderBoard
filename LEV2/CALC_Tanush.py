import tkinter as tk
import math 

def press_num(num):
		text_in_box = entr_label.cget("text")
		# Prevent multiple decimals in one number
		if num == '.' and '.' in text_in_box:
				return
		entr_label.configure(text=text_in_box + str(num))

def press_op(operator):
		text_in_box = entr_label.cget("text")
		text_in_expr = expr_label.cget("text")

		# If we just finished a calculation, start fresh
		if "=" in text_in_expr:
				text_in_expr = ""

		if text_in_box != "":
				# Move current number and operator to the top history label
				expr_label.configure(text=text_in_expr + text_in_box + operator)
				entr_label.configure(text='')
		elif text_in_expr != "" and text_in_expr[-1] in "+-*/":
				# Allow user to change their mind on the operator
				expr_label.configure(text=text_in_expr[:-1] + operator)

def press_eq():
		text_in_box = entr_label.cget("text")
		text_in_expr = expr_label.cget("text")

		if "=" in text_in_expr or (text_in_box == "" and text_in_expr == ""):
				return

		full_expression = text_in_expr + text_in_box

		try:
				# Evaluate the string safely
				result = eval(full_expression, {"sqrt": math.sqrt, "__builtins__": None})
				expr_label.configure(text=full_expression + ' = ')
				entr_label.configure(text=str(round(result, 8))) 
		except Exception:
				entr_label.configure(text='ERROR')

def press_sqrt():
		text_in_box = entr_label.cget("text")
		if text_in_box != "":
				# Wraps the current entry in sqrt()
				entr_label.configure(text=f"sqrt({text_in_box})")

def press_pct():
		"""
		Standard Calculator Percentage Logic:
		If '100 +' is in the expr_label and '10' is in the entr_label, 
		pressing % converts the '10' into '10.0' (10% of 100).
		"""
		text_in_box = entr_label.cget("text")
		text_in_expr = expr_label.cget("text")

		if text_in_box == "":
				return

		try:
				current_val = float(text_in_box)

				# Check if there's a base number to calculate a percentage of
				if text_in_expr != "" and text_in_expr[-1] in "+-*/":
						# Extract the expression before the operator
						base_expr = text_in_expr[:-1].strip()
						# Calculate the value of the base expression (handles sqrt or previous math)
						base_val = eval(base_expr, {"sqrt": math.sqrt, "__builtins__": None})

						# Result = (Base * Percent Input) / 100
						percentage_val = (base_val * current_val) / 100
						entr_label.configure(text=str(percentage_val))
				else:
						# Fallback for simple division: 50 % -> 0.5
						entr_label.configure(text=str(current_val / 100))
		except:
				entr_label.configure(text='ERROR')

def press_C():
		entr_label.configure(text='')
		expr_label.configure(text='')

# --- UI Setup ---
window = tk.Tk()
window.title("TI-108")
window.geometry("320x420")
window.resizable(0, 0)

# Grid weights for responsiveness
for i in range(4): window.grid_columnconfigure(i, weight=1)
for i in range(2, 7): window.grid_rowconfigure(i, weight=1)

# Displays
expr_label = tk.Label(window, text="", bg='#e0e0e0', anchor="e", padx=10, height=2)
expr_label.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=(5, 0))

entr_label = tk.Label(window, text="", bg='white', font=('Arial Bold', 20), anchor="e", padx=10, height=2, borderwidth=2, relief="sunken")
entr_label.grid(row=1, column=0, columnspan=4, sticky="ew", padx=5, pady=(0, 10))

# Button Helper Function
def create_btn(text, row, col, cmd, color='white', span=1, rspan=1, font_style=('Arial', 12)):
		b = tk.Button(window, text=text, bg=color, command=cmd, font=font_style, relief="raised")
		b.grid(row=row, column=col, columnspan=span, rowspan=rspan, sticky="nsew", padx=2, pady=2)

# --- Layout ---
# Row 2
create_btn('C', 2, 0, press_C, color='red')
create_btn('√', 2, 1, press_sqrt, color='grey')
create_btn('%', 2, 2, press_pct, color='grey')
create_btn('/', 2, 3, lambda: press_op('/'), color='grey')

# Row 3
create_btn('7', 3, 0, lambda: press_num(7))
create_btn('8', 3, 1, lambda: press_num(8))
create_btn('9', 3, 2, lambda: press_num(9))
create_btn('*', 3, 3, lambda: press_op('*'), color='grey')

# Row 4
create_btn('4', 4, 0, lambda: press_num(4))
create_btn('5', 4, 1, lambda: press_num(5))
create_btn('6', 4, 2, lambda: press_num(6))
create_btn('-', 4, 3, lambda: press_op('-'), color='grey')

# Row 5
create_btn('1', 5, 0, lambda: press_num(1))
create_btn('2', 5, 1, lambda: press_num(2))
create_btn('3', 5, 2, lambda: press_num(3))
create_btn('+', 5, 3, lambda: press_op('+'), color='grey')

# Row 6
create_btn('0', 6, 0, lambda: press_num(0), span=2)
create_btn('.', 6, 2, lambda: press_num('.'))
create_btn('=', 6, 3, press_eq, color='green', font_style=('Arial Bold', 12))

tk.mainloop()