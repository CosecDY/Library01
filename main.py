running = True
game_started = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started and start_button_rect.collidepoint(event.pos):
                game_started = True  # เมื่อปุ่ม "เริ่มเกม" ถูกคลิกเราจะเริ่มเกม
                start_game()  # เรียกฟังก์ชันเริ่มเกม

    screen.fill((255, 255, 255))  
    
    if not game_started:
        screen.blit(start_button_image, start_button_rect)  

    pygame.display.flip()

pygame.quit()


def start_game():