import sqlite3
import os

def LEER_2():
    con = sqlite3.connect('DB/config.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM B01_Bancos")
    res=cursor.fetchall()
    return res
    

def CargarCorreo():
    con = sqlite3.connect('DB/config.db')
    cursor=con.cursor()

    correo=input("Indique correo a configurar:   ").lower()
    host=input("indique host a configurar:       ")
    puerto=input("indique el puerto del correo:  ")
    pas=input("indique la ontraseña del correo:  ")
    # utsf rynk rkbv bxku"
    insert= F'INSERT INTO C01_Correo VALUES ("{correo}","{pas}","{puerto}","{host}")'
    cursor.execute(insert)
    con.commit()
    
def LEER() :
    con = sqlite3.connect('DB/config.db')
    cursor=con.cursor()
    cursor.execute("SELECT * FROM C01_CORREO")
    res=cursor.fetchone()
    con.commit()
    return res

def buscar_Banco(var) :
    con = sqlite3.connect('DB/config.db')
    cursor=con.cursor()
    cursor.execute(F"SELECT * FROM B01_BANCOS WHERE B01_NOMBRE='{var}'")
    res=cursor.execute(F"SELECT * FROM B01_BANCOS WHERE B01_NOMBRE='{var}'")
    res=res.fetchone()
    if str(res) == "None":
        return False
    else:
        if  res[3] == var:
            return res
        
def CrearTabla_Correo():
    if  input().lower() == "s":
        os.mkdir("DB")
        os.mkdir("DB/BVC")
        os.mkdir("DB/BNC")
        con = sqlite3.connect('DB/config.db')
        query_create="CREATE TABLE C01_Correo (	C01_Correo	TEXT NOT NULL,	C01_CONTRASEÑA	TEXT NOT NULL COLLATE BINARY,	C01_PUERTO 	INTERGER NOT NULL,	C01_HOST TEXT NOT NULL  )"
        cursor= con.cursor()
        cursor.execute(query_create)
        CargarCorreo()
        con.commit()
        con.close

def CrearTabla_Bancos():
    con = sqlite3.connect('DB/config.db')
    query_create='CREATE TABLE B01_Bancos (	"B01_BANCOS" 	INTEGER NOT NULL UNIQUE, "B01_RIF" TEXT NOT NULL, "B01_CUENTA" TEXT NOT NULL,	"B01_NOMBRE"	TEXT NOT NULL,	"B01_USUARIO"	TEXT NOT NULL,	"B01_CLAVE"	INTEGER NOT NULL,	PRIMARY KEY("B01_BANCOS" AUTOINCREMENT));'
    cursor= con.cursor()
    cursor.execute(query_create)
    con.commit()
    con.close()

def CrearTabla_error():
    con = sqlite3.connect('DB/Log.db')
    query_create='CREATE TABLE E01_Error (	"E01_Error" INTEGER NOT NULL UNIQUE, "E01_DESCRIPCION" TEXT NOT NULL,	PRIMARY KEY("E01_Error" AUTOINCREMENT))'
    cursor= con.cursor()
    cursor.execute(query_create)
    con.commit()
    con.close()

def Error(er):
    con = sqlite3.connect('DB/Log.db')
    query_create= f"INSERT INTO E01_Error (E01_DESCRIPCION)  VALUES ('{er}' )"
    cursor= con.cursor()
    cursor.execute(query_create)
    con.commit()
    con.close()
    
def CrearTabla_enviado():
    con = sqlite3.connect('DB/Log.db')
    query_create='CREATE TABLE E02_ENVIADOS (	"E02_ENVIADOS" INTEGER NOT NULL UNIQUE, E02_DESCRIPCION TEXT ,"E02_ESTATUS" TEXT NOT NULL,E02_FECHA  TEXT NOT NULL ,PRIMARY KEY("E02_ENVIADOS" AUTOINCREMENT))'
    cursor= con.cursor()
    cursor.execute(query_create)
    con.commit()
    con.close()


def enviado(en,st,fh):
    con = sqlite3.connect('DB/Log.db')
    query_create= f"INSERT INTO E02_ENVIADOS (E02_DESCRIPCION,E02_ESTATUS,E02_FECHA)  VALUES ('{en}','{st}','{fh}' )"
    cursor= con.cursor()
    cursor.execute(query_create)
    con.commit()
    con.close()

def Insert_Banco():
    con = sqlite3.connect('DB/config.db')
    #Variables predefinidas
    # ban="BFC"
    # us="6191020091127724"
    # cla="Max*626026"
    #Inputs
    ban=input("Indique el banco con su diminutivo de 3 letras:  ").upper()
    us=input("Usuario de ingreso :   ")
    rif=input("indique rif :").upper()
    cue=input("indique Cuenta :")
    cla=input("Contraseña : ")
    query_create= f"INSERT INTO B01_Bancos (B01_NOMBRE,B01_RIF ,B01_CUENTA, B01_USUARIO, B01_CLAVE)  VALUES ('{ban}','{rif}','{cue}', '{us}' , '{cla}' )"
    cursor= con.cursor()
    res=buscar_Banco(ban)
    # cursor.execute(query_create)
    # con.commit()
    # con.close()

    if res:
        print("banco ya registrado")
    else: 
        print("registro realizado")
        cursor.execute(query_create)
        con.commit()
        con.close()

try:
    con = sqlite3.connect('DB/config.db')

    
    
except sqlite3.OperationalError as error:
    if  str(error) =="unable to open database file":
        print(f"Ocurrió un error operacional: {error}")
        print(' Crear Base de datos ?? \n s/n')
        CrearTabla_Correo()
        CrearTabla_Bancos()
        Insert_Banco()
        CrearTabla_error()
        CrearTabla_enviado()


