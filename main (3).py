#!/usr/bin/env python3

from typing import IO
import random

class Circle:
    #Circle class
    
    def __init__(self, cir: tuple, col: tuple):
    #Circle class constructor
    
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
        
def drawCircle(f: IO[str], t: int, c: Circle):
    #drawCircle method
    
    ts: str = "   " * t
    
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green},\
    {c.blue})" fill-opacity="{c.op}"></circle>'
    
    f.write(f"{ts}{line}\n")
        

class Rectangle:
    #Rectangle class
    
    def __init__(self, rect: tuple, col_op: tuple):
    #Rectangle class constructor    
        
        self.position_x: int = rect[0]
        self.position_y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.color_R: int = col_op[0]
        self.color_G: int = col_op[1]
        self.color_B: int = col_op[2]
        self.opacity: float = col_op[3] 
    

def drawRectangle(file: IO[str], lineSpace: int, rect: Rectangle):
    #drawRectangle method
    
    space: str = "   " * lineSpace
    
    line: str = f'<rect x="{rect.position_x}" y="{rect.position_y}" width="{rect.width}"\
    height="{rect.height}" fill="rgb({rect.color_R},{rect.color_G},{rect.color_B})" fill-opacity="{rect.opacity}"></rect>'
    
    file.write(f"{space}{line}\n")
    
class ProEpilogue():
    #ProEpilogue class
    
    temp_file: IO[str] = None
    
    def __init__(self):
    #ProEpilogue class constructor
    
       ProEpilogue.makefile(self)
       generateShapes()
       ProEpilogue.CloseHTMLFile(self)
       
   
    def makefile(self):
    #makefile method
    
        self.file = open ("Part_1.html", "w")
        self.file.write("<html>\n<head>\n    <title>PART_1 ART</title>\n</head>\n<body>\n")
        defintion: str = "Define SVG Drawing Board"
        self.file.write(f"\n   <!--{defintion}-->")
        self.file.write('\n   <svg width="1000" height="600">\n')
        ProEpilogue.temp_file = self.file
        
    def CloseHTMLFile(self):
    #CloseHTMLFile method
    
        self.file.write("\n   </svg>\n</body>\n</html>")
        self.file.close() 
        
    def get_file():
    #get_file method
    
        return ProEpilogue.temp_file

class GenRandom():
    #GenRandom class
    
    def random_raduis(self):
    #rand_raduis method
    
        rand_num: int = random.randrange(10,100)
        return rand_num
        
    def random_position(self):
    #random_position method
    
        rand_num: int = random.randrange(10,1000)
        return rand_num
        
    def random_width_height(self):
    #random_width_height method
        
        rand_num: int = random.randrange(10,100)
        return rand_num
        
    def random_color(self):
    #random_color method  
        
        rand_num: int = random.randrange(0,255,10)
        return rand_num
    
    def random_opacity(self):
    #random_opacity method
    
         rand_num: float = round(random.uniform(0,1.0), 2)
         return rand_num
        
class ArtConfig():
    #ArtConfig class
    
    def __init__(self):
        genRand = GenRandom()
        self.rand_x = genRand.random_position()
        self.rand_y = genRand.random_position()
        self.rand_raduis = genRand.random_raduis()
        self.rand_width = genRand.random_width_height()
        self.rand_height = genRand.random_width_height()
        self.rand_R = genRand.random_color()
        self.rand_G = genRand.random_color()
        self.rand_B = genRand.random_color()
        self.rand_op = genRand.random_opacity()

class ShapesSummary:
    #ShapesSummary class
  
  def DispTags(self):
    #DispTags method
  
      print("\nShapes:")
      print("1 : Rectangle\n2 : Circle\n")
      print("CNT  SHA      X     Y   RAD     W     H     R     G     B     OP")
     
  def DispData(self,counter: int , shape: int ,pos_x: int, pos_y: int, raduis: int, width: int, height: int,\
  col_R: int, col_G: int, col_B: int, op: float ):
    #DispData method
  
      print("{" ":" "=3d}".format(counter)," {" ":" "=3d}".format(shape),"   {" ":" "=3d}".format(pos_x), " " ,\
      "{" ":" "=3d}".format(pos_y), " " ,"{" ":" "=3d}".format(raduis), " " , "{" ":" "=3d}".format(width),\
      " " , "{" ":" "=3d}".format(height), " " , "{" ":" "=3d}".format(col_R), " " ,\
      "{" ":" "=3d}".format(col_G), " " , "{" ":" "=3d}".format(col_B), " " ,"{:.2f}".format(op))
      
    
def generateShapes():
    #generateShapes method
    
    ShpS = ShapesSummary()
    ShpS.DispTags()
    count = -1
    while count < 999:
     
        count = count + 1
        
        AC = ArtConfig()
        AC_2 = ArtConfig()
        
        drawRectangle(ProEpilogue.get_file(), 1, Rectangle((AC.rand_x, AC.rand_y, AC.rand_width, AC.rand_height),\
        (AC.rand_R, AC.rand_G, AC.rand_B, AC.rand_op)))
        
        ShpS.DispData(count, 1, AC.rand_x, AC.rand_y, 0, AC.rand_width, AC.rand_height, AC.rand_R,\
        AC.rand_G, AC.rand_B, AC.rand_op)
        
        count = count + 1
        
        drawCircle(ProEpilogue.get_file(), 1, Circle((AC_2.rand_x, AC_2.rand_y, AC_2.rand_raduis),\
        (AC_2.rand_R, AC_2.rand_G, AC_2.rand_B, AC_2.rand_op)))
        
        ShpS.DispData(count, 2, AC_2.rand_x, AC_2.rand_y, AC_2.rand_raduis, 0, 0, AC_2.rand_R, AC_2.rand_G,\
        AC_2.rand_B, AC_2.rand_op)
  
    

def main():
    #main method
    
    ProEpilogue()

main()

                                                                                                                                                                                                                                                                                                        
