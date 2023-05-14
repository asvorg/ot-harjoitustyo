## How to use salasana-wallet

Clone the program from github using:
```
git clone https://github.com/asvorg/ot-harjoitustyo
```

Navigate to the root directory of the program and run

```
poetry install
```

Install MongoDB by running

```
apt-get install mongodb
```

If it doesn't work, you can follow the instructions [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

Install the required crypto libraries by running

```
pip install pycryptodome
```


## Starting the program

Navigate to ot-harjoitustyo/salasana_wallet/src/main/main_program.py

and run it with 
```
python3 main_program.py
```

MongoDB should start when the program is run, if not you can just run
```
mongo
```

## Using salasana-wallet

Once the program starts, it will print the relevant keyboard shortcuts on how to use the program, they are quite self-explanatory.
