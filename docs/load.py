import os,nltk
import MySQLdb as m

db=m.connect(host="localhost",user="soumen",passwd="soumen",db="banglawordnet",charset='utf8')
cursor=db.cursor()

path=os.path.expanduser('/home/soumen/projects/Bangla_WordNet_online')
nltk.data.path.append(path)
a=nltk.data.load('docs/words.yaml') 

for i in range(len(a)):
    id_=a[i]['ID:']
    cat=a[i]['CAT:']
    synset=a[i]['SYNSET-BENGALI:']
    example=a[i]['EXAMPLE:']
    concept=a[i]['CONCEPT:']
    cursor.execute("insert into interface_synset(id,category,concept,synsets,example) values(%d,'%s','%s','%s','%s')"%(id_,cat,concept,synset,example))
    db.commit()

db.close()

