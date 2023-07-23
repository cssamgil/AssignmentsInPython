# Carlos Sanchez COP4045 Assignment 5
In this assignment we were asked to create a simple program for performing addition and subtraction using colors.

I divided this program into 4:
- **created class:** this class will be called in later on in my call to set the values. 

```python
class Color:
    def __init__(self, red, green, blue):
        self.red = self.check(red)
        self.green = self.check(green)
        self.blue = self.check(blue)

    def check(self, num):
        if num < 0:
            return 0
        elif num > 1:
            return 1
        else:
            return num

    def __add__(self, x):
        return Color(self.red + x.red, self.green + x.green, self.blue + x.blue)

    def __sub__(self, x):
        return Color(self.red - x.red, self.green - x.green, self.blue - x.blue)

    def __str__(self):
        return "({:.1f},{:.1f},{:.1f})".format(self.red, self.green, self.blue)

    def __eq__(self, other):
        if isinstance(other, Color):
            if self.red == other.red and self.green == other.green and self.blue == other.blue:
              return True
        else:
            return False
```

- **Dictionary: ** created by the values given in the assignment pdf.

```python
colors = {"red":        Color(1, 0, 0),
          "green":      Color(0, 1, 0),
          "blue":       Color(0, 0, 1),
          "cyan":       Color(0, 1, 1),
          "magenta":    Color(1, 0, 1),
          "yellow":     Color(1, 1, 0),
          "black":      Color(0, 0, 0),
          "white":      Color(1, 1, 1)
          }
```

- **Promp user: ** in this part I gave the user the oportunity to pick if they want to input the color name or the color value, after that the dictionary and class is called. if result values are equal to value in dictionary, it will print key value name in the dictionary.

```python
print("Welcome to the Color app\nIn this program you will be able to perform \naddition and subtraction using colors. ")
print()

color_one = ""
color_two = ""
decision = input("Color by name (N) or color by value (V): ").upper()
if decision == "N":
    color_one = str(input("Enter color 1 name: "))
    color_one = colors[color_one]

elif decision == "V":
    a = float(input("Insert first color value: "))
    b = float(input("Insert second color value: "))
    c = float(input("Insert third color value: "))
    color_one = Color(a, b, c)


decision = input("Color by name (N) or color by value (V): ").upper()
if decision == "N":
    color_two = str(input("Enter color 2 name: "))
    color_two = colors[color_two]


elif decision == "V":
    a = float(input("Insert first color value: "))
    b = float(input("Insert second color value: "))
    c = float(input("Insert third color value: "))
    color_two = Color(a, b, c)

add = color_one + color_two
sub = color_one - color_two

for name, value in colors.items():
    if value == add:
        add = name

for name, value in colors.items():
    if value == sub:
        sub = name
```

- **Pretty print: **

```python
print()
print("Color 1 + Color 2 =", add)
print("Color 1 - Color 2 =", sub)
```