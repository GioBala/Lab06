from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        # TODO
        automobili = []
        cnx= get_connection()
        import mysql.connector
        #mysql = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="pa")
        #mysql = mysql.connector.connect(option_files="database/connector.cnf")
        cursor = cnx.cursor()
        query_re = "SELECT * FROM `automobile`"
        cursor.execute(query_re)
        for row in cursor:
            automobili.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        cnx.close()
        #print("ciao")
        return automobili


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        automobili = []
        cnx= get_connection()
        # mysql = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="pa")
        cursor = cnx.cursor()
        query_se = "SELECT * FROM automobile WHERE modello= %s"
        cursor.execute(query_se,(modello,))
        for row in cursor:
            automobili.append(Automobile(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        cnx.close()
        return automobili

