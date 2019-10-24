'''								BATALHA NAVAL
	      						PROGRAMACAO E BASE DE DADOS
		  					       CATARINA ALVES
'''
#_______________________________________________________________________________________________________________________________________________#
#DEFINICAO DAS FUNCOES UTILIZADAS NO JOGO

#Funcao que desenha os tabuleiros de jogo. Recebe como argumento uma lista de listas (board)

def draw_board(board):
	for row in board:
		print(row[0]+ row[1]+ row[2]+ row[3]+ row[4]+ row[5]+ row[6]+ row[7]+ row[8]+ row[9]+ row[10])

#Funcao que realiza a conversao da coluna inserida (A-J) em numeros (1-10).

def letter_conversion(letter):
	if letter=='A':
		col=1
	elif letter=='B':
		col=2
	elif letter=='C':
		col=3
	elif letter=='D':
		col=4
	elif letter=='E':
		col=5
	elif letter=='F':
		col=6
	elif letter=='G':
		col=7
	elif letter=='H':
		col=8
	elif letter=='I':
		col=9
	elif letter=='J':
		col=10
	return(col)

#Funcao que valida o valor de linha introduzido.

def line_validation(line):
	hypothesis=['1','2','3','4','5','6','7','8','9','10']
	while line not in hypothesis:
		print 'Invalid option! Please tipe a number in range 1-10'
		line=raw_input("Line:")
	line=int(line)
	return(line)

#Funcao que valida o valor de coluna introduzido.

def col_validation(col):
	hypothesis=['A','B','C','D','E','F','G','H','I','J']
	while col not in hypothesis:
		print 'Invalid option! Please tipe a letter between A-J'
		col=raw_input("Column:")
	col=letter_conversion(col)
	return(col)
		
#Funcao que realiza a insercao dos barcos no tabuleiro. Recebe como argumentos o tipo e nome do barco a ser inserido. Retorna uma lista dos tuplos que traduzem as posicoes das pecas do barco.

def insert_ship(type,Name):
	position=0
	if type =='submarin':
		print "Please insert your submarin position:"
		line=raw_input("Line:")
		line=line_validation(line)
		col=raw_input("Column:")
		col=col_validation(col)
		while board3[line][col]!='  ':
			print 'Invalid position'
			line=raw_input("Line:")
			line=int(line_validation(line))
			col=raw_input("Column:")
			col=int(col_validation(col))
				
		board1[line][col]=' S'
		board3[line][col]=' S'
		alter_board3(line,col)
		position=line,col
		position=str(position)
		bship.execute('''INSERT INTO SHIP (GameID,Name,Length,Sink,Player) VALUES (%s,%s,%s,%s,%s)''', (GameID,Name, 1,0,Player1ID))
		battleship.commit()
		ShipID=int(bship.execute('''SELECT ID FROM SHIP ORDER BY ID DESC'''))	
		bship.execute('''INSERT INTO COORDINATE (Coordinate,ShipID) VALUES (%s, %s)''', (position, ShipID))
		battleship.commit()
	if type=='two_cannon':
		print "Please insert your two cannon ship position:"
		line1=raw_input("Line:")
		line1=int(line_validation(line1))
		col1=raw_input("Column:")
		col1=int(col_validation(col1))
		line2=raw_input("Line:")
		line2=int(line_validation(line2))
		col2=raw_input("Column:")
		col2=int(col_validation(col2))
		while board3[line1][col1]!='  ' or board3[line2][col2]!='  ':
			print 'Invalid position'
			line1=raw_input("Line:")
			line1=int(line_validation(line1))
			col1=raw_input("Column:")
			col1=int(col_validation(col1))
			line2=raw_input("Line:")
			line2=int(line_validation(line2))
			col2=raw_input("Column:")
			col2=int(col_validation(col2))
		
		board1[line1][col1]=' T' 
		board1[line2][col2]=' T'
		board3[line1][col1]=' T' 
		board3[line2][col2]=' T'
		alter_board3(line1, col1)
		alter_board3(line2, col2)
		position=[str((line1,col1)),str((line2,col2))]
		bship.execute('''INSERT INTO SHIP (GameID,Name,Length,Sink,Player) VALUES (%s, %s, %s,%s,%s)''', (GameID,Name, 2,0,Player1ID))
		battleship.commit()
		ShipID=int(bship.execute('''SELECT ID FROM SHIP ORDER BY ID DESC'''))
		for i in position:
			bship.execute('''INSERT INTO COORDINATE (Coordinate,ShipID) VALUES (%s, %s)''', (i, ShipID))

	if type=='three_cannon':
		print "Please insert your three cannon ship position:"
		line1=raw_input("Line:")
		line1=int(line_validation(line1))
		col1=raw_input("Column:")
		col1=int(col_validation(col1))
		line2=raw_input("Line:")
		line2=int(line_validation(line2))
		col2=raw_input("Column:")
		col2=int(col_validation(col2))
		line3=raw_input("Line:")
		line3=int(line_validation(line3))
		col3=raw_input("Column:")
		col3=int(col_validation(col3))
		while board3[line1][col1]!='  ' or board3[line2][col2]!='  ' or board3[line3][col3]!='  ':
			print 'Invalid position'
			line1=raw_input("Line:")
			line1=int(line_validation(line1))
			col1=raw_input("Column:")
			col1=int(col_validation(col1))
			line2=raw_input("Line:")
			line2=int(line_validation(line2))
			col2=raw_input("Column:")
			col2=int(col_validation(col2))
			line3=raw_input("Line:")
			line3=int(line_validation(line3))
			col3=raw_input("Column:")
			col3=int(col_validation(col3))
	
		board1[line1][col1]=' H' 
		board1[line2][col2]=' H'
		board1[line3][col3]=' H'
		board3[line1][col1]=' H' 
		board3[line2][col2]=' H'
		board3[line3][col3]=' H'
		alter_board3(line1,col1)
		alter_board3(line2,col2)
		alter_board3(line3,col3)
		position=[str((line1,col1)),str((line2,col2)),str((line3,col3))]
		bship.execute('''INSERT INTO SHIP (GameID,Name,Length,Sink,Player) VALUES (%s,%s, %s,%s,%s)''', (GameID,Name, 3,0,Player1ID))
		battleship.commit()
		ShipID=int(bship.execute('''SELECT ID FROM SHIP ORDER BY ID DESC'''))
		for i in position:
			bship.execute('''INSERT INTO COORDINATE (Coordinate,ShipID) VALUES (%s, %s)''', (i, ShipID))
	
	if type=='four_cannon':
		print "Please insert your four-cannon ship position:"
		line1=raw_input("Line:")
		line1=int(line_validation(line1))
		col1=raw_input("Column:")
		col1=int(col_validation(col1))
		line2=raw_input("Line:")
		line2=int(line_validation(line2))
		col2=raw_input("Column:")
		col2=int(col_validation(col2))
		line3=raw_input("Line:")
		line3=int(line_validation(line3))
		col3=raw_input("Column:")
		col3=int(col_validation(col3))
		line4=raw_input("Line:")
		line4=int(line_validation(line4))
		col4=raw_input("Column:")
		col4=int(col_validation(col4))
		while board3[line1][col1]!='  ' or board3[line2][col2]!='  ' or board3[line3][col3]!='  ' or board3[line4][col4]!='  ':
			print 'Invalid position'
			line1=raw_input("Line:")
			line1=int(line_validation(line1))
			col1=raw_input("Column:")
			col1=int(col_validation(col1))
			line2=raw_input("Line:")
			line2=int(line_validation(line2))
			col2=raw_input("Column:")
			col2=int(col_validation(col2))
			line3=raw_input("Line:")
			line3=int(line_validation(line3))
			col3=raw_input("Column:")
			col3=int(col_validation(col3))
			line4=raw_input("Line:")
			line4=int(line_validation(line4))
			col4=raw_input("Column:")
			col4=int(col_validation(col4))		
		board1[line1][col1]=' F' 
		board1[line2][col2]=' F'
		board1[line3][col3]=' F'
		board1[line4][col4]=' F'
		board3[line1][col1]=' F' 
		board3[line2][col2]=' F'
		board3[line3][col3]=' F'
		board3[line4][col4]=' F'
		alter_board3(line1,col1)
		alter_board3(line2,col2)
		alter_board3(line3,col3)
		alter_board3(line4,col4)	
		position=[str((line1,col1)),str((line2,col2)),str((line3,col3)),str((line4,col4))]
		bship.execute('''INSERT INTO SHIP (GameID,Name,Length,Sink,Player) VALUES (%s,%s, %s,%s,%s)''', (GameID,Name,4,0,Player1ID))
		battleship.commit()
		ShipID=int(bship.execute('''SELECT ID FROM SHIP ORDER BY ID DESC'''))	
		for i in position:
			bship.execute('''INSERT INTO COORDINATE (Coordinate,ShipID) VALUES (%s, %s)''', (i, ShipID))	

	if type=='airplane_porter':
		print "Please insert your airplane porter position:"
		line1=raw_input("Line:")
		line1=int(line_validation(line1))
		col1=raw_input("Column:")
		col1=int(col_validation(col1))
		line2=raw_input("Line:")
		line2=int(line_validation(line2))
		col2=raw_input("Column:")
		col2=int(col_validation(col2))
		line3=raw_input("Line:")
		line3=int(line_validation(line3))
		col3=raw_input("Column:")
		col3=int(col_validation(col3))
		line4=raw_input("Line:")
		line4=int(line_validation(line4))
		col4=raw_input("Column:")
		col4=int(col_validation(col4))
		line5=raw_input("Line:")
		line5=int(line_validation(line5))
		col5=raw_input("Column:")
		col5=int(col_validation(col5))
		while board3[line1][col1]!='  ' or board3[line2][col2]!='  ' or board3[line3][col3]!='  ' or board3[line4][col4]!='  ' or board3[line5][col5]!='  ':
			print 'Invalid position'
			line1=raw_input("Line:")
			line1=int(line_validation(line1))
			col1=raw_input("Column:")
			col1=int(col_validation(col1))
			line2=raw_input("Line:")
			line2=int(line_validation(line2))
			col2=raw_input("Column:")
			col2=int(col_validation(col2))
			line3=raw_input("Line:")
			line3=int(line_validation(line3))
			col3=raw_input("Column:")
			col3=int(col_validation(col3))
			line4=raw_input("Line:")
			line4=int(line_validation(line4))
			col4=raw_input("Column:")
			col4=int(col_validation(col4))
			line5=raw_input("Line:")
			line5=int(line_validation(line5))
			col5=raw_input("Column:")
			col5=int(col_validation(col5))
		
		board1[line1][col1]=' A' 
		board1[line2][col2]=' A'
		board1[line3][col3]=' A'
		board1[line4][col4]=' A'
		board1[line5][col5]=' A'
		board3[line1][col1]=' A' 
		board3[line2][col2]=' A'
		board3[line3][col3]=' A'
		board3[line4][col4]=' A'
		board3[line5][col5]=' A'
		alter_board3(line1,col1)
		alter_board3(line2,col2)
		alter_board3(line3,col3)	
		alter_board3(line4,col4)
		alter_board3(line5,col5)
		position=[str((line1,col1)),str((line2,col2)),str((line3,col3)),str((line4,col4)),str((line5,col5))]
		bship.execute('''INSERT INTO SHIP (GameID,Name,Length,Sink,Player) VALUES (%s,%s, %s,%s,%s)''', (GameID,Name,5,0,Player1ID))
		battleship.commit()
		ShipID=int(bship.execute('''SELECT ID FROM SHIP ORDER BY ID DESC'''))	
		for i in position:
			bship.execute('''INSERT INTO COORDINATE (Coordinate,ShipID) VALUES (%s, %s)''', (i, ShipID))

	draw_board(board1)
	print '\n'

	draw_board(board2)            
	print '\n' 

	
	return position

#Funcao que altera o tabuleiro 3 em funcao dos barcos inseridos. O tabuleiro 3 e usado para validar as posicoes dos barcos e nunca e imprimido durante o jogo. Para cada tipo de barco, as posicoes vizinhas sao preenchidas com um X o que impede a insercao de barcos em contacto uns com os outros, garantindo desta forma o cumprimento das regras do jogo. Recebe como atributos os valores da linha e coluna de cada peca dos barcos.

def alter_board3(line, col):
	if line!=10 and col!=10 and line!=1 and col!=1:	
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line+1][col+1]=='  ':
			board3[line+1][col+1]=' X'
		if board3[line+1][col-1]=='  ':
			board3[line+1][col-1]=' X'
		if board3[line-1][col+1]=='  ':
			board3[line-1][col+1]=' X'
		if board3[line-1][col-1]=='  ':
			board3[line-1][col-1]=' X'
	elif line==1 and col==1:
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line+1][col+1]=='  ':
			board3[line+1][col+1]=' X'
	elif line==10 and col==10:
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line-1][col-1]=='  ':
			board3[line-1][col-1]=' X'	
	elif line==10 and col==1:
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line-1][col+1]=='  ':
			board3[line-1][col+1]=' X'
	elif line==1 and col==10:
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line+1][col-1]=='  ':
			board3[line+1][col-1]=' X'
	elif line==10 and col!=10:
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line-1][col+1]=='  ':
			board3[line-1][col+1]=' X'
		if board3[line-1][col-1]=='  ':
			board3[line-1][col-1]=' X'
	elif line==1 and col!=1:
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line+1][col+1]=='  ':
			board3[line+1][col+1]=' X'
		if board3[line+1][col-1]=='  ':
			board3[line+1][col-1]=' X'
	
	elif col==10 and line!=10:
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col-1]=='  ':
			board3[line][col-1]=' X'
		if board3[line+1][col-1]=='  ':
			board3[line+1][col-1]=' X'
		if board3[line-1][col-1]=='  ':
			board3[line-1][col-1]=' X'
	elif col==1 and line!=1:
		if board3[line+1][col]=='  ':
			board3[line+1][col]=' X'
		if board3[line-1][col]=='  ':
			board3[line-1][col]=' X'
		if board3[line][col+1]=='  ':
			board3[line][col+1]=' X'
		if board3[line+1][col+1]=='  ':
			board3[line+1][col+1]=' X'
		if board3[line-1][col+1]=='  ':
			board3[line-1][col+1]=' X'
	
			
#Funcao que permite a insercao dos tiros do jogador e da consequente resposta do jogador adversario. Aceita como atributo a variavel global 'total_sink' que define o numero de barcos afundados do adversario, e retorna o seu valor atualizado com base nas respostas. Este valor e usado para definir quando o adversario perde (quando todos os seus barcos forem afundados).
 
def player1_shot(total_sink):
	bship.execute('''INSERT INTO MOVE (GameID, Player) VALUES (%s,%s)''', (GameID, Player1ID))
	battleship.commit()
	MoveID=bship.execute('''SELECT ID FROM MOVE ORDER BY ID DESC''')	
	print "\nPlease insert your shots coordinates:"
	for i in range(3):
		line=raw_input("Line:")
		line=line_validation(line)
		col=raw_input("Column:")
		col=col_validation(col)
		coordinate=line,col
		coordinate=str(coordinate)
		while coordinate in player1_shots:
			print "Invalid shot"
			line=raw_input("Line:")
			line=line_validation(line)
			col=raw_input("Column:")
			col=col_validation(col)
			coordinate=line,col
			coordinate=str(coordinate)
		player1_shots.append(coordinate)
		bship.execute('''INSERT INTO PLAYER_SHOT (MoveID, Coordinate) VALUES (%s,%s)''', (MoveID,coordinate))
	answer=' '
	while answer!='E':
		print "\nPlease insert your oponent response:"
		answer=raw_input("Ship(S,T,H,F,A), All in water(W), Exit(E):")
		ShipType=0	
		Hit=0
		Sink=0
		if answer=='S':
			ShipType='submarin'
		if answer=='T':
			ShipType='two-cannon'
		if answer=='H':
			ShipType='three-cannon'
		if answer=='F':
			ShipType='four-cannon'
		if answer=='A':
			ShipType='airplane-porter'
		if answer=='W':
			ShipType='all in water'
		if answer!='W' and answer!='E':		
			HS=raw_input("Hit(H) or Sink(S)?")
			if HS=='H':
				Sink=0
				Hit=1
			if HS=='S':
				Sink=1
				Hit=0
				total_sink+=1
		if answer!='E':
			bship.execute('''INSERT INTO OPONENT_ANSWER (MoveID, Answer, Hit, Sink) VALUES (%s,%s,%s,%s)''', (MoveID,ShipType,Hit,Sink))
			battleship.commit()
	
	return total_sink

#Funcao que define quando os barcos do jogador se afundam com base no seu comprimento e no numero de tiros do adversario que acertaram nesse barco. Aceita como atributo o ID que permite a identificacao do barco e retorna o valor da diferenca entre o numero de tiros e o comprimento. 

def is_ship_sink(shipID):
	bship.execute('''select count(ID) from OPONENT_SHOT where ShipID=%s''',(shipID,))
	data=bship.fetchall()
	n_hit=int(data[0][0])
	bship.execute('''select SHIP.Length from SHIP where SHIP.ID=%s''',(shipID,))
	data=bship.fetchall()
	length=int(data[0][0])
	return n_hit-length

#Funcao que, com base nos tiros do adversario, retorna a consequente resposta.

def print_results(shots):
	sub_sink=0
	two_sink=0
	two_hit=0
	three_sink=0
	three_hit=0
	four_sink=0
	four_hit=0
	airplane_sink=0
	airplane_hit=0
	
	for i in range(n_two_cannon):
		globals()['two%s_sink' % i]=0
		globals()['two%s_hit' % i]=0
	for i in range(n_three_cannon):
		globals()['three%s_sink' % i]=0
		globals()['three%s_hit' % i]=0
	for i in range(n_four_cannon):
		globals()['four%s_sink' % i]=0
		globals()['four%s_hit' % i]=0
	for i in range(n_airplane_porter):
		globals()['airplane%s_sink' % i]=0
		globals()['airplane%s_hit' % i]=0
	water=0
	for i in shots:
		if i[0]=='submarin':
			sub_sink+=1
		for j in range(n_two_cannon):
			if i[0]=='two-cannon%s'% j and i[1]==1:
				globals()['two%s_sink' % j]+=1
			elif i[0]=='two-cannon%s'% j and i[1]==0:
				globals()['two%s_hit' % j]+=1
		for j in range(n_three_cannon):
			if i[0]=='three-cannon%s'% j and i[1]==1:
				globals()['three%s_sink' % j]+=1
			elif i[0]=='three-cannon%s'% j and i[1]==0:
				globals()['three%s_hit' % j]+=1
		for j in range(n_four_cannon):
			if i[0]=='four-cannon%s'% j and i[1]==1:
				globals()['four%s_sink' % j]+=1
			elif i[0]=='four-cannon%s'% j and i[1]==0:
				globals()['four%s_hit' % j]+=1
		for j in range(n_airplane_porter):
			if i[0]=='airplane-porter%s'% j and i[1]==1:
				globals()['airplane%s_sink' % j]+=1
			elif i[0]=='airplane-porter%s'% j and i[1]==0:
				globals()['airplane%s_hit' % j]+=1
		if i[0]=='water':
			water+=1
	
	if sub_sink>0:
		print "Sink", sub_sink, "submarine(s)!"
	for i in range(n_two_cannon):	
		if globals()['two%s_sink' % i]==1:
			two_sink+=1
		elif globals()['two%s_hit' % i]>0:
			two_hit+=1
	if two_sink>0:
		print "Sink",two_sink,"two-cannon ship(s)!"
	if two_hit>0:
		print "Hit",two_hit,"two-cannon ship(s)!"
	for i in range(n_three_cannon):	
		if globals()['three%s_sink' % i]==1:
			three_sink+=1
		elif globals()['three%s_hit' % i]>0:
			three_hit+=1
	if three_sink>0:
		print "Sink",three_sink,"three-cannon ship(s)!"
	if three_hit>0:
		print "Hit",three_hit,"three-cannon ship(s)!"
	for i in range(n_four_cannon):	
		if globals()['four%s_sink' % i]==1:
			four_sink+=1
		elif globals()['four%s_hit' % i]>0:
			four_hit+=1
	if four_sink>0:
		print "Sink",four_sink,"four-cannon ship(s)!"
	if four_hit>0:
		print "Hit",four_hit,"four-cannon ship(s)!"
	for i in range(n_airplane_porter):	
		if globals()['airplane%s_sink' % i]==1:
			airplane_sink+=1
		elif globals()['airplane%s_hit' % i]>0:
			airplane_hit+=1
	if airplane_sink>0:
		print "Sink the airplane-porter!"
	if airplane_hit>0:
		print "Hit the airplane-porter!"
	if water==3:
		print "All in water!"

#Funcao que permite a insercao dos tiros do adversario.

def oponent_shot():
	bship.execute('''INSERT INTO MOVE (GameID, Player) VALUES (%s,%s)''', (GameID, Player2ID))
	battleship.commit()
	MoveID=bship.execute('''SELECT ID FROM MOVE ORDER BY ID DESC''')
	shots=[]
	print "\nPlease insert your oponent shots coordinates:"
	for i in range(3):
		line=raw_input("Line:")
		line=line_validation(line)
		col=raw_input("Column:")
		col=col_validation(col)
		coordinate=line,col
		coordinate=str(coordinate)
		while coordinate in oponent_shots:
			print "Invalid shot"
			line=raw_input("Line:")
			line=line_validation(line)
			col=raw_input("Column:")
			col=col_validation(col)
			coordinate=line,col
			coordinate=str(coordinate)
		oponent_shots.append(coordinate)
		bship.execute('''select SHIP.ID from SHIP,COORDINATE where COORDINATE.Coordinate=%s and SHIP.GameID=%s  and COORDINATE.ShipID=SHIP.ID''' ,(coordinate, GameID))
		data=bship.fetchall()
		if data==():
			shipName='water'
			sink=' '
		else:
			shipID=int(data[0][0])
			battleship.commit()
			bship.execute('''INSERT INTO OPONENT_SHOT (MoveID, Coordinate,ShipID) VALUES (%s,%s,%s)''', (MoveID,coordinate,shipID))
			battleship.commit()
			bship.execute('''select Name from SHIP where ID=%s''',(shipID,))
			data=bship.fetchall()
			shipName=str(data[0][0])
			sink=0
			sink_result=is_ship_sink(shipID)
			if sink_result==0:
				bship.execute('''update SHIP set Sink=1 where ID=%s''', (shipID,))
				battleship.commit()
				sink=1
				player_game_over(GameID)
		shots.append((shipName,sink))
	print '\n'	
	print_results(shots)

#Funcao que permite ao jogador alterar livremente o tabuleiro 2 com base nos palpites que tem sobre o jogo do adversario.

def alter_board2():
	line=0
	col=0
	mark=0
	end=0
	answer=0
	while answer!='No':
		answer=raw_input("\nPlace the marks on your oponent's board. Press Enter to continue or 'No' to pass ")
		if answer!='No':
			print '''\n - Ships (S,T,H,F,A)
 - Water (X)
 - Doubt (?)'''
			line=raw_input("Line:")
			line=line_validation(line)
			col=raw_input("Column:")
			col=col_validation(col)
			mark=' '+raw_input("Mark:")
			board2[line][col]=mark
			
			draw_board(board2)
#Funcao que define quando o jogador perde. Recebe como atributo o ID que permite a identificacao do jogo.

def player_game_over(GameID):
	bship.execute('''select count(ID) from SHIP where Sink=0 and GameID=%s''',(GameID,))
	data=bship.fetchall()
	active_ships=int(data[0][0])
	if active_ships == 0:
		print '\n',player2, "won the game!"
		bship.execute('''update GAME set Winner=%s where ID=%s''', (Player2ID,GameID))
		battleship.commit()
		sys.exit()

#_______________________________________________________________________________________________________________________________________________#
#DESENHO DO JOGO

board1=[['  ',' A',' B',' C',' D',' E',' F',' G',' H',' I',' J'],
[' 1','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 2','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 3','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 4','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 5','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 6','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 7','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 8','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 9','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
['10','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']]


board2=[['  ',' A',' B',' C',' D',' E',' F',' G',' H',' I',' J'],
[' 1','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 2','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 3','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 4','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 5','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 6','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 7','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 8','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 9','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
['10','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']]

board3=[['  ',' A',' B',' C',' D',' E',' F',' G',' H',' I',' J'],
[' 1','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 2','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 3','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 4','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 5','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 6','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 7','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 8','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
[' 9','  ','  ','  ','  ','  ','  ','  ','  ','  ','  '],
['10','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ']]

#Numero de barcos de cada tipo a ser considerado no jogo

n_submarines=4
n_two_cannon=3
n_three_cannon=2
n_four_cannon=1
n_airplane_porter=1
total_sink=0
n_total=n_submarines + n_two_cannon + n_three_cannon + n_four_cannon + n_airplane_porter 
		


print '\nWelcome to battleship!!' 
print '\n'
player1=raw_input("Player1:")
player2=raw_input("Player2:")
import datetime
date=datetime.datetime.now().strftime('%Y-%m-%d ')



print '\nYou must place:'  
print '\n-four submarines           S' 
print '\n-three two cannon ships    TT'
print '\n-two three cannon ships    HHH'
print '\n-one four cannon ship      FFFF'
print '\n-one airplane              A\n                          AAA\n                           A'
print '\n'

import MySQLdb
battleship=MySQLdb.connect(user='battleship', password='catarina_work', host='localhost',database='battleship');
bship=battleship.cursor();

bship.execute('''INSERT INTO PLAYER (Name) VALUES (%s)''', (player1,))
battleship.commit()
Player1ID=bship.execute('''SELECT ID FROM PLAYER ORDER BY ID DESC''')
bship.execute('''INSERT INTO PLAYER (Name) VALUES (%s)''', (player2,))
battleship.commit()	
Player2ID=bship.execute('''SELECT ID FROM PLAYER ORDER BY ID DESC''')
bship.execute('''INSERT INTO GAME (Player1, Player2, Date) VALUES (%s,%s,%s)''', (Player1ID, Player2ID, date))
battleship.commit()
GameID=(bship.execute('''SELECT ID FROM GAME ORDER BY ID DESC'''))

print '\n'

draw_board(board1)
print('\n')


draw_board(board2)
print'\n'

for i in range(n_airplane_porter):
	insert_ship('airplane_porter','airplane-porter%s'%(i))
for i in range(n_submarines):
	insert_ship('submarin','submarin')
for i in range(n_two_cannon):
	insert_ship('two_cannon','two-cannon%s'%(i))
for i in range(n_three_cannon):
	insert_ship('three_cannon','three-cannon%s'%(i))
for i in range(n_four_cannon):
	insert_ship('four_cannon','four-cannon%s'%(i))


import sys
oponent_shots=[]
player1_shots=[]
while total_sink!=n_total:
	total_sink=player1_shot(total_sink)
	alter_board2()
	oponent_shot()
	print'\n'	
	draw_board(board1)
	print'\n'
	draw_board(board2)
	print'\n'

if total_sink==n_total:
	print '\n', player1, "won the game!"
	bship.execute('''update GAME set Winner=%s where ID=%s''', (player1,GameID))
	battleship.commit()
	sys.exit()

