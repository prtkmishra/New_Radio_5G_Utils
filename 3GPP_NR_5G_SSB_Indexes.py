import string
print "\nThis utility is to be used to calculate location of SSB in time domain\nPlease refer to 38.213 Section 4.1"
def first_formula(n):
	global First_Sym
	for i in n:
		Frst_symbol = 2+14*i, 8+14*i
		First_Sym.append(Frst_symbol)

def second_formula(n):
	global First_Sym
	for i in n:
		Frst_symbol = 4+28*i, 8+28*i, 16+28*i, 20+28*i 
		First_Sym.append(Frst_symbol)

def third_formula(n):
	global First_Sym
	for i in n:
		Frst_symbol = 8+56*i,12+56*i,16+56*i,20+56*i,32+56*i,36+56*i,40+56*i,44+56*i
		First_Sym.append(Frst_symbol)		
		
def first_symbol_SSB_3Ghz():
	global Case_choice
	global First_Sym
	Case = Case_choice
	First_Sym = []
	if Case == "A" or Case == "C":
		n_list = [0,1]
		first_formula(n_list)
	elif Case == "B":
		n_list = [0]
		second_formula(n_list)
	First_Sym_str = ''.join(str(x) for x in First_Sym)
	First_Sym_str_replace = string.replace(First_Sym_str,"," , "")
	First_Sym_str_replace1 = string.replace(First_Sym_str_replace,"(" , "")
	First_Sym_str_replace2 = string.replace(First_Sym_str_replace1,")" , " ")
	print "The first symbol indexes for SS block transmission \n %r \n" %First_Sym_str_replace2

def first_symbol_SSB_3to6Ghz():
	global Case_choice
	global First_Sym
	Case = Case_choice
	First_Sym = []
	if Case == "A" or Case == "C":
		n_list = [0,1,2,3]
		first_formula(n_list)
	elif Case == "B":
		n_list = [0,1]
		second_formula(n_list)
	elif Case == "D":
		n_list = [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18]
		second_formula(n_list)	
	elif Case == "E":
		n_list = [0,1,2,3,5,6,7,8]
		third_formula(n_list)
	First_Sym_str = ''.join(str(x) for x in First_Sym)
	First_Sym_str_replace = string.replace(First_Sym_str,"," , "")
	First_Sym_str_replace1 = string.replace(First_Sym_str_replace,"(" , "")
	First_Sym_str_replace2 = string.replace(First_Sym_str_replace1,")" , " ")
	print "The first symbol indexes for SS block transmission \n %r \n" %First_Sym_str_replace2

def first_symbol_SSB_6Ghz():
	global Case_choice
	global First_Sym
	Case = Case_choice
	First_Sym = []
	if Case == "D":
		n_list = [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18]
		second_formula(n_list)
	elif Case == "E":
		n_list = [0,1,2,3,5,6,7,8]
		third_formula(n_list)
	First_Sym_str = ''.join(str(x) for x in First_Sym)
	First_Sym_str_replace = string.replace(First_Sym_str,"," , "")
	First_Sym_str_replace1 = string.replace(First_Sym_str_replace,"(" , "")
	First_Sym_str_replace2 = string.replace(First_Sym_str_replace1,")" , " ")
	print "The first symbol indexes for SS block transmission \n %r \n" %First_Sym_str_replace2

def start():
	global Case_choice
	Case_choice = raw_input("Case> ").upper()
	Carr_Freq = raw_input("""Carr_Freq = \n \t a.<3Ghz \t\t b.3to6Ghz \t\t c.>6Ghz \n>> """)
	Case = ['A', 'B', 'C', 'D', 'E']
	SCS = ['15', '30', '30', '120', '240']
	Index_Case = Case.index(Case_choice)
	Map_SCS = int(SCS.pop(Index_Case))
	print "\n\n'SCS is %r' \n" %Map_SCS
	if Carr_Freq == "a":
		first_symbol_SSB_3Ghz()
	elif Carr_Freq == "b":
		first_symbol_SSB_3to6Ghz()
	else:
		first_symbol_SSB_6Ghz()
start()
raw_input()
