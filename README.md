#Introduction

Bangla Wordnet is a lexical database for the bengali language inspired from the [WordNet](wordnet.princeton.edu) developed at Princeton.

#Usage

1. Download the compressed release of your choice(zip/tar) and decompress it in any of your folder's.

2. Set up a working installation of django,preferrably inside a virtual environment.

3. Download and install MongoDB [here](http://www.mongodb.org/downloads),pymongo and NLTK.

4. Start the mongod server.

5. Run load.py file from the *load* directory.

6. Start the Mongo shell and create a database- "online": ``use online``

7. Create a user named root and add roles for it: ``db.createUser({user:"root",pwd:"root",roles:[{role:"readWrite",db:"online"},]}).

8. Run the django server and point to your [localhost](http://127.0.0.1:8000/index)

9. There's no step 9.


  
