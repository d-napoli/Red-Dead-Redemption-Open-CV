![enter image description here](https://raw.githubusercontent.com/d-napoli/Red-Dead-Redemption-Open-CV/main/Images/Main-Github-Photo.png)

# Python Read Dead Redemption AI

Code made with **Python** using **Open CV** 👁️

## Read Dead Redemption 2 🎮
Red Dead Redemption 2 is a 2018 action-adventure game developed and published by Rockstar Games. The game is the third entry in the Red Dead series and is a prequel to the 2010 game Red Dead Redemption. [Wikipedia](https://en.wikipedia.org/wiki/Red_Dead_Redemption_2)

## What this code does? 🖥️
The main goal is make the main character walk by itself on Red Dead.<br>
When a destination is set on the minimap, we get a red stripe with the destination route.<br>
This stripe is the compass for the **open cv** to guide itself.

![enter image description here](https://raw.githubusercontent.com/d-napoli/Red-Dead-Redemption-Open-CV/main/Images/minimap_red.png)

### CV must see only the red path
For making the cv only see the red path, we use the image manipulation to transform the colors and keep only the red

![enter image description here](https://raw.githubusercontent.com/d-napoli/Red-Dead-Redemption-Open-CV/main/Images/minimap_white.png)

### Centering the mouse and running
After the code is able to only see the path, I use the mouse to always center it, so this way we know that the character is walking/running in the **right direction**. Every now and then, the code presses the **left shift** button on the keyboard, so the character can run faster.