import pygame
from phases.phase_machine import PhaseMachine
from rendering.state_renderer import StateRenderer
from phases.game_phase import GamePhaseTypes

class GameEngine:
    def __init__(self, screen, game_state, image_loader):
        self.screen = screen
        self.game_state = game_state
        self.image_loader = image_loader
        self.phase_machine = PhaseMachine(self.game_state, GamePhaseTypes.PLAYER_IDLE)
        self.state_renderer = StateRenderer(screen, self.game_state, self.image_loader)
        self.running = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            else:
                self.phase_machine.handle_event(event)
    
    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        clock = pygame.time.Clock()

        while self.game_state.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state.running = False
                else:
                    self.phase_machine.handle_event(event)

            self.phase_machine.update()
            self.screen.fill((0, 0, 0))
            self.state_renderer.render()  
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
