# PokemonEvaluator

Use Pokéapi (https://pokeapi.co/) to evaluate the type advantages of two Pokémon. While you may use any programming language, we prefer Python or Javascript. Include a requirements.txt if using Python or a package.json if using Javascript.
The program should take two Pokémon names or IDs as arguments and output to stdout the name of the Pokémon with a favourable type advantage.
In the case of no type advantage the program should output the name of the Pokémon with the highest base stats. In the case of a tie the program should output the name of the first Pokémon passed to it.


###Example Invocation 

```
./program bulbasaur charmander
```
Expected Output

```
charmander
```

##Getting Start

This project is written by Python 3.7.0. Please make sure that the test environment is based on Python 3.6 or later.

###Install and Implement Test Environment

```buildoutcfg
pip install virtualenv
virtualenv PokemonEvaluator
source PokemonEvaluator/venv/bin/activate
```

###Install Essential Site Package

```buildoutcfg
pip install -r requirements.txt
``` 

### Main Program

```
./scripts/run bulbasaur charmander
```

## Authors

* **Shawn Xu** - Programmer

  shawnxu0420@gmail.com