from PIL import Image, ImageDraw
import numpy as np

min_x,max_x = -2.2,2.2  #Need same absolute value
min_y,max_y = -1.8,1.8  #Need same absolute value

img_width = 300 #How many pixels wide
img_height = 200 #How many pixels high

diverge_val = 2 #Absolute value needed for c to diverge
n_loops = 30    #How many loops to go through until we say c doesn't diverge
cf_r,cf_g,cf_b = 5,14,4 #color values diverging values should get (the later they diverge, the more color they get)
cr,cg,cb = 100,230,90   #color values non-diverging values get

#Sets up the pixel arrays and their complex values, then inserts corresponding color values using the bound method
def generate_pixel_arr():
    x_width = max_x-min_x
    x_factor = x_width/img_width
    y_height = max_y-min_y
    y_factor = y_height/img_height
    points = [[complex(x*x_factor+min_x,y*y_factor+min_y) for x in range(0,img_width)] for y in range(0,img_height)]
    diverge_points = [[bound(c) for c in line] for line in points]
    make_image(diverge_points)

#Checks if c is bound, applying c(n+1)=c(n)^2+c
def bound(c):
    c_t = c
    for i in range(0,n_loops):
        c_t = c_t*c_t+c
        if abs(c_t) > diverge_val:
            return (i*cf_r,i*cf_g,i*cf_b)
    return (cr,cg,cb)
#Generates a RGB png file using pillow and an input array of color values
def make_image(points):
    arr = np.array(points)
    img = Image.fromarray(arr.astype("uint8"),"RGB")
    img.save("image.png")

#Starts the image creation
generate_pixel_arr()