# -*- coding: utf-8 -*-
"""
Created on Sun May 12 09:14:48 2019

@author: Reborn
"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd

def setbusca():

    esc1=('https://www.publishnews.com.br/ranking')
    html=urlopen(str(esc1))
    resposta=bs(html,'lxml')
    periodos=[]
    semana=[]
    mes=[]
    ano=[]
    period=resposta.find_all('a',{'class':'pn-periodos-periodo'})
    
    
    for p in period: 
            periodos.append(p.get_text())

    for element in periodos:
        if len(element)==10:
            semana.append(element)
        elif len(element)==7:
            mes.append(element)
        else:
            ano.append(element)
    print('Digite 1 para fazer uma consulta do ranking por SEMANA.')
    print('Digite 2 para fazer uma consulta por ranking por MÊS.')
    print('Digite 3 para fazer uma consulta do ranking por ANO.')
    escolha=input('Digite o número da sua escolha: ')
    global target
    global choice
    if escolha=='1':
        print('VOCÊ TEM '+str(len(semana))+' SEMANAS DISPONÍVEIS:')
        print(semana)
        choice=input('Digite exatamente a semana no formato XX/XX/XXXX: ')
        pieces=choice.split('/')
        target='https://www.publishnews.com.br/ranking/semanal/0/'+str(pieces[2])+'/'+str(pieces[1])+'/'+str(pieces[0])+'/'+'0/0'
        print(target)                                                               
    elif escolha=='2':
        print('VOCÊ TEM '+str(len(mes))+' MESES DISPONÍVEIS:')
        print(mes)
        choice=input('Digite exatamente o mês no formato XX/XXXX: ')
        pieces=choice.split('/')
        target='https://www.publishnews.com.br/ranking/mensal/0/'+str(pieces[1])+'/'+str(pieces[0])+'/'+'0/0'
        print(target)        
    elif escolha=='3':
        print('VOCÊ TEM '+str(len(ano))+' ANOS DISPONÍVEIS:')
        print(ano)
        choice=input('Digite exatamente a ano no formato XXXX: ')
        target='https://www.publishnews.com.br/ranking/anual/0/'+choice+'/'+'0/0'
        print(target)        
    else:
        print('Sua escolha não foi válida')
    
            
            
setbusca() 

def extrailivro():        

    print('Busca no endereço:'+''+ target)
    esc1=(target)
    html=urlopen(str(esc1))
    resposta=bs(html,'lxml')
    
    #print(resposta.prettify())
    #csvFile=open('teste.csv', 'w' )
    #writer=csv.writer(csvFile)
    
    categorias=['pn-ranking-livros-posicao-numero',
                'pn-ranking-livros-posicao-volume',
                'pn-ranking-livro-nome',
                'pn-ranking-livro-autor',
                'pn-ranking-livro-editora',
                'pn-ranking-livro-isbn',
                'pn-ranking-livro-categoria',
                'pn-ranking-livro-preco',
                'pn-ranking-livro-paginas']
    
    categ=[]
    for c in categorias:
        nomecat=c.split('-')[-1]
        categ.append(nomecat)
    
    data={}
    
    for d in categorias:
        valores=[]
        ordem=resposta.find_all('div',{'class':d})
        for y in ordem: 
                valores.append(y.get_text())
                data[categ[categorias.index(d)]]= valores
       
    
    df=pd.DataFrame(data).set_index('numero')
    
    df.to_csv('Consulta'+choice.replace('/','')+'.csv')
    
    print('TOP FIVE:')
    print(df.head())
    print()
    print('Gravado arquivo com o nome: '+'Consulta'+choice.replace('/','')+'.csv')
    print('TAREFA CONCLUIDA')
    print()
    
extrailivro()

while True:
    print('QUER FAZER NOVA CONSULTA ?') 
    print() 
     
    print('DIGITE 1 PARA SIM OU DIGITE 2 PARA SAIR.')
    repete=input('DIGITE O NÚMERO DA SUA ESCOLHA :')
    if repete=='1':
        setbusca()
        extrailivro()
    else:
        print('ATÉ A PRÓXIMA !')
        break
 