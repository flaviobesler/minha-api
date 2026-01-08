from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

from typing import Optional

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*'],
    allow_headers = ['*'],
    )

class Dividas(BaseModel):
    despesa: str
    pagValor: float
    pagParcial: Optional [float] = None
    faltaQuanto: Optional [float] = None
    

@app.post('/api/dividas')
def create_divida(divida: Dividas):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO dividas ( despesa, pagValor, pagParcial, faltaQuanto) VALUES(?, ?, ?, ?)',
        ( divida.despesa, divida.pagValor, divida.pagParcial, divida.faltaQuanto)
        )
    conn.commit()
    conn.close()
    return{'message':'despesa inserida com sucesso'}


@app.get('/api/dividas')
def select_divida():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, despesa, pagValor, pagParcial, faltaQuanto, pagData FROM DIVIDAS')
    row = cursor.fetchall()

    conn.close()

    return[
        {   'id':i[0],
            'despesa':i[1],
            'pagValor':i[2],
            'pagParcial':i[3],
            'faltaQuanto':i[4]
            
            }
            for i in row]


@app.patch('/api/dividas/{id}')
def patch_dividas (id:int, divida: Dividas):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    #estrutura generalista de um update
    cursor.execute(
                    '''
                    
                    UPDATE dividas
                    SET pagValor = ?, pagParcial = ?, faltaQuanto = ?,  
                    WHERE id= ?''',
                   (
                    divida.despesa,
                    divida.pagValor,
                    divida.pagParcial,
                    divida.faltaQuanto,
                    id))
    conn.commit()
    conn.close()
    return{'message':'divida atualizada'}


@app.delete('/api/dividas/{id}')
def update_dividas(id:int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM dividas WHERE id=?',
        (id,))
    conn.commit()
    conn.close()

    return{'message':'divida deletetada com sucesso'}


class Ganhos (BaseModel):
    id: int
    ganhoValor : float
    descricao: Optional [str] = None

    descricaoServ: Optional [str] = None

@app.post('/api/ganhos')
def create_ganho(ganho: Ganhos):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        '''INSERT INTO ganhos (ganhoValor, descricao, descricaoServ) VALUES (?, ?, ?)''', 
            (ganho.ganhoValor, ganho.descricao,  ganho.descricaoServ))
    conn.commit()
    conn.close()
    return{'message':'ganho criado com sucesso'}

@app.get('/api/ganhos')
def select_ganho():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, ganhoValor, descricao, descricaoServ')
    row = cursor.fetchall()
    cursor.close()

    return[
        {   'id':i[0],
            'ganhoValor':i[1],
            'descricao':i[2],
            'descricaoServ':i[3]}
            for i in row]
@app.patch('/api/ganhos/{id}')
def update_ganhos(id:int, ganho: Ganhos): #em todo patch ou put, caso vc declare {id}, precisa declarar id:int em def update
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
                   UPDATE ganhos SET ganhoValor = ?, descricao = ?, descricaoServ = ? 
                   WHERE id=?''',
                    (ganho.ganhoValor,
                     ganho.descricao,
                     ganho.descricaoServ,
                     id))
    conn.commit()
    conn.close()
    return{'message':'despesa atualizada com sucesso'}

@app.delete('/api/ganhos/{id}')
def delete_ganhos(id:int):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM ganhos WHERE id=?',
        (id,))
    conn.commit()
    conn.close()
    return{'message':'ganho deletado com sucesso'}