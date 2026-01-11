# Modellering og Simulation 

## Faglige mål 
- Forstå inheritance og Polymorfi
    - Recap: inheritance
- Abstract classes og metoder
    - Polymorfi
    - DRY (Don't Repeat Yourself) principle
- Configuration dictionaries
    - unpacking dictionaries 
- List comprehensions (recap)
- Data Visualization
    - Matplotlib Animation
- Agent Based Modelling (ABM)  
- Videnskabsteori
    - Naturvidenskabelig metode
        - Labtoratorie- og felteksperiment
        - Modeller 
        - Hypotetisk-deduktive metode



## Materialer
- [Emprisk og formel](https://vidensmoenstre.systime.dk/?id=129)
- [Deduktion og induktion](https://vidensmoenstre.systime.dk/?id=143)

## Further reading 
- [Agent based modelling (ABM)](https://complexityexplorer.s3.amazonaws.com/Mesa+ABM/epstein_axtell.pdf)
- [Game Theory by ABM](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Agent-Based_Evolutionary_Game_Dynamics_(Izquierdo_Izquierdo_and_Sandholm)/02%3A_Our_first_agent-based_evolutionary_model/2.01%3A_Our_very_first_model)



## Abstract Klasser og Polymorfi

- Læs https://docs.python.org/3/library/abc.html
- Læs https://www.geeksforgeeks.org/python/polymorphism-in-python/


- Forklar begreber 
    - Nedarvning
    - Polymorphism 
- forklare hvad en abstract class er, og hvorfor man bruger abc

    *The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system". The principle has been formulated by Andy Hunt and Dave Thomas in their book The Pragmatic Programmer. They apply it quite broadly to include database schemas, test plans, the build system, even documentation.When the DRY principle is applied successfully, a modification of any single element of a system does not require a change in other logically unrelated elements. Additionally, elements that are logically related all change predictably and uniformly, and are thus kept in sync.(wikipedia)*

- implementere egne klasser, der overholder et fælles interface

- anvende **kwargs og dictionary-unpacking i constructors


### Do it yourself

- Læs artiklen https://realpython.com/instance-class-and-static-methods-demystified/
- Implementer klasser `Rectangle` og `Circle` i filen models/Shape.py
    - **Inheritance**: `Circle` skal nedarve fra `Shape`
    - **Constructor (__init__)**
        - Circle skal bruge **kwargs som input
        - Circle skal gemme radius som et attribut
    - **abstractmetod**: Implementér metoden area(), der skal returnere cirklens areal.
    - **classmetode**: Implementér metoden from_config(cls, config), der skal 
        - modtage en dictionary
        - validere input
        - oprette og returnere et Circle-objekt
    - **staticmetode** Implementér static metode validate_config(config) der skal:
        - sikre at "radius" findes i dictionary
        - sikre at radius er et positivt tal
        - Hvis input er forkert, skal der raises en ValueError



## Agent Based Modelling
:raising_hand: _Hvad er ABM?_

- Læs artiklen om agent based modelling https://math.libretexts.org/Bookshelves/Applied_Mathematics/Agent-Based_Evolutionary_Game_Dynamics_(Izquierdo_Izquierdo_and_Sandholm)/01%3A_Introduction/1.02%3A_Introduction_to_agent-based_modeling
- En video on net-logo og ABM https://www.youtube.com/watch?v=ocp3OdOvrZM
- Net-logo: https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Biology/Virus.nlogox

## Bygge Simulationsmodellen 
- Læs artiklen om prey og predator model https://rf.mokslasplius.lt/agent-based-prey-predator-model/

### Regler
:raising_hand: _Hvilke regler skal modellen have?_

### Klasse Agent
- Implementere klasse `Agent`som en abstract class
- Diskussion:
    - Hvilke metoder kunne en agent have?

### Klasse Prey
- Implementere klasser `Prey` og `Predator`, ved at implementere abstrakt klasse `Agent`. 
    - :raising_hand: Hvilke attribute skal en `Prey` have?
    - Implementere de abstrakte metoder af `Agent`
        - **move**
        - **eat**
        - **reproduce**
    - :raising_hand: Hvordan teste man metoderne?

### Klasse Predator
- Komplet Klasse `Pedator` ved at implementere de abstrakte klasse `Agent`.
- :raising_hand: Er der noget flere attributer eller metoder `Predator` skal have? 




### Simulerings Engine

- Simuleringsløkke: for hvert tidskridt 
    - Bevægelse
    - Interaktioner (Spise, jage)
    - Reproduktion
    - Fjern døde
    - Registrer statistik








