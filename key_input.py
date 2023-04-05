import pygame


def get_key_pressed(event):
               
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                return "A"

               
            # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")
               
            # checking if key "P" was pressed
            if event.key == pygame.K_p:
                print("Key P has been pressed")
             
            # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")