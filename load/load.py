import nltk
import pymongo
from pymongo import MongoClient

a=nltk.data.load('corpora/bangla/exp.yaml')

client=MongoClient()
db=client['online']
collection=db['synset']

for i in range(len(a)):
  syn=[]
  l=a[i]['SYNSET-BENGALI'].split(',')
  for j in l:
    c=j.strip(' ')
    syn.append(c)
  for k in range(len(syn)):
    cat=a[i]['CAT']
    concept=a[i]['CONCEPT']
    example=a[i]['EXAMPLE']
    word=syn[k]
    synset=syn
    db.synset.insert({'word':word,'cat':cat,'concept':concept,'example':example,'synset':synset})
        
        
