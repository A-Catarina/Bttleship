#							  BATTLESHIP-base de dados
#							PROGRAMAÇÃO E BASE DE DADOS
#							      CATARINA ALVES



#Criação do utilizador battleship

CREATE USER 'battleship'@'localhost' IDENTIFIED BY 'catarina_work';

#Acesso ao utilizador battleship. password de acesso: catarina_work

mysql -h localhost -u battleship -p  

create database battleship; 

use battleship;
              
create table PLAYER(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20)); 

create table GAME(ID INT  PRIMARY KEY AUTO_INCREMENT, Player1 INT, Player2 INT,Date DATE, Winner INT, FOREIGN KEY (Player1) REFERENCES PLAYER(ID),FOREIGN KEY (Player2) REFERENCES PLAYER(ID));

create table SHIP(ID INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20), Length INT,GameID INT,Sink INT,Player INT, FOREIGN KEY (Player) REFERENCES PLAYER(ID), FOREIGN KEY (GameID) REFERENCES GAME(ID));

create table MOVE(ID INT PRIMARY KEY AUTO_INCREMENT,Player INT, FOREIGN KEY (Player) REFERENCES PLAYER(ID), GameID INT, FOREIGN KEY (GameID) REFERENCES GAME(ID));

create table COORDINATE(ID INT PRIMARY KEY AUTO_INCREMENT, Coordinate CHAR(10), ShipID INT, FOREIGN KEY (ShipID) REFERENCES SHIP(ID));   

create table OPONENT_ANSWER(ID INT PRIMARY KEY AUTO_INCREMENT, MoveID INT, Answer VARCHAR(20),Hit INT, Sink INT, FOREIGN KEY (MoveID) REFERENCES MOVE(ID));

create table PLAYER_SHOT(ID INT PRIMARY KEY AUTO_INCREMENT, MoveID INT, Coordinate VARCHAR(10), FOREIGN KEY (MoveID) REFERENCES MOVE(ID));


create table OPONENT_SHOT(ID INT PRIMARY KEY AUTO_INCREMENT, MoveID INT, Coordinate VARCHAR(20), ShipID INT, FOREIGN KEY (MoveID) REFERENCES MOVE(ID), FOREIGN KEY (ShipID) REFERENCES SHIP(ID));


