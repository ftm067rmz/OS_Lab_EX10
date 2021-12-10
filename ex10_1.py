import arcade

height = 500
width = 500
color1 = arcade.color.RED
color2 = arcade.color.BLUE
w = 10
h = 10

arcade.open_window(width, height, "Complex Loops")
arcade.set_background_color(arcade.color.WHITE_SMOKE)
arcade.start_render() 


for i in range(100, width-100, 25):
    for j in range(100, height-100, 25):
        if i%2==0:
            if j%2==0:
                arcade.draw_rectangle_filled(i, j, w, h, color1, 45)
            else:
                arcade.draw_rectangle_filled(i, j, w, h, color2, 45)
        else:
            if j%2 == 0:
                arcade.draw_rectangle_filled(i, j, w, h, color2, 45)
            else:
                arcade.draw_rectangle_filled(i, j, w, h, color1, 45)


arcade.finish_render()
arcade.run()