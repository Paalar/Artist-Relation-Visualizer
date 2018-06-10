# Artist-Relation-Visualizer
This uses the spotify API to see relations between artists and maps them to a connected graph.

This is a qucik hacky solution and very not finished where there is room for optimization and a lot more.
I wrote this since I wanted to see how some artists were related to each other and perhaps an idea of what I can listen to.
It is written in Python.

A known bug is when there are special characters in the artist name. For example "Joey Bad$$" stops the naming of that vertice and the rest of the unamed vertices, though the vertices are still plotted.

A search on Metallica with degree of 4. 
<img src="https://github.com/Paalar/Artist-Relation-Visualizer/blob/master/Screen%20Shot%202018-06-10%20at%2020.28.51.png" />
Further are other zoomed in pictures on this graph.
<img src="https://github.com/Paalar/Artist-Relation-Visualizer/blob/master/Screen%20Shot%202018-06-10%20at%2020.29.31.png" />
<img src="https://github.com/Paalar/Artist-Relation-Visualizer/blob/master/Screen%20Shot%202018-06-10%20at%2020.29.54.png" />

A search on (I believe) Shawn Mendes with a degree of 3
<img src="https://github.com/Paalar/Artist-Relation-Visualizer/blob/master/Screen%20Shot%202018-06-10%20at%2020.29.02.png" />

An unkown search with degree of 2
<img src="https://github.com/Paalar/Artist-Relation-Visualizer/blob/master/Screen%20Shot%202018-06-10%20at%2020.29.11.png" />
