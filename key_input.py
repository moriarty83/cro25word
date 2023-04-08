import pygame

def get_key_pressed(event):
    
    if event.key == pygame.K_a:
        return "A"               
    if event.key == pygame.K_b:
        return "B"
    if event.key == pygame.K_c:
        return "C"
    if event.key == pygame.K_d:
        return "D"
    if event.key == pygame.K_e:
        return "E"               
    if event.key == pygame.K_f:
        return "F"
    if event.key == pygame.K_g:
        return "G"
    if event.key == pygame.K_h:
        return "H"
    if event.key == pygame.K_i:
        return "I"               
    if event.key == pygame.K_j:
        return "J"
    if event.key == pygame.K_k:
        return "K"
    if event.key == pygame.K_l:
        return "L"
    if event.key == pygame.K_m:
        return "M"               
    if event.key == pygame.K_n:
        return "N"
    if event.key == pygame.K_o:
        return "O"
    if event.key == pygame.K_p:
        return "P"
    if event.key == pygame.K_q:
        return "Q"
    if event.key == pygame.K_r:
        return "R"               
    if event.key == pygame.K_s:
        return "S"
    if event.key == pygame.K_t:
        return "T"
    if event.key == pygame.K_u:
        return "U"
    if event.key == pygame.K_v:
        return "V"               
    if event.key == pygame.K_w:
        return "W"
    if event.key == pygame.K_x:
        return "X"
    if event.key == pygame.K_y:
        return "Y"
    if event.key == pygame.K_z:
        return "Z"
    if event.key == pygame.K_TAB:
        return "tab"
    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
        return "delete"