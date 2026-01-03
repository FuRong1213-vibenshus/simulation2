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
- Implementer klasser `Rectangle` og `Circle` i filen models/Shape.py
- Forklar begreber 
    - Nedarvning
    - Polymorphism 



## Agent Based Modelling
:raising_hand: _Hvad er ABM?_

- Læs artiklen om agent based modelling https://math.libretexts.org/Bookshelves/Applied_Mathematics/Agent-Based_Evolutionary_Game_Dynamics_(Izquierdo_Izquierdo_and_Sandholm)/01%3A_Introduction/1.02%3A_Introduction_to_agent-based_modeling
- En video on net-logo og ABM https://www.youtube.com/watch?v=ocp3OdOvrZM



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








