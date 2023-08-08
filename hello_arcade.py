import arcade

SCREEN_WIDTH = 600
SCREEN_HIGHT = 800
SCREEN_TITLE = "Hola arcade"

if __name__ == "__main__":
    #Crear ventana
    arcade.open_window(SCREEN_WIDTH,SCREEN_HIGHT, SCREEN_TITLE)
    #Cambiar color de fondo
    arcade.set_background_color(arcade.color.BABY_BLUE)

    #Iniciar render
    arcade.start_render()
    #Funciones para dibujar

    arcade.draw_rectangle_filled(300,400,310,260, arcade.color.BROWN)
    arcade.draw_rectangle_filled(300,400,120,100,arcade.color.SILVER)
    
    #finalizar render
    arcade.finish_render()

    #correr el programa
    arcade.run()