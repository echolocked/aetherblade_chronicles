import pygame
from phases.game_phase import GamePhaseTypes, BattlePhase
from units.player_hero_unit import PlayerHeroUnit

class PlayerIdlePhase(BattlePhase):
    def __init__(self, game_state, callbacks=None):
        super().__init__(game_state, callbacks)
        self.game_state.cursor_color = (0, 255, 0)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                selected_unit = self.game_state.get_unit_at_cursor()
                if selected_unit and isinstance(selected_unit, PlayerHeroUnit):
                    self.callbacks['change_phase'](GamePhaseTypes.PLAYER_UNIT_MOVE)
                    self.game_state.selected_unit = selected_unit
                else:
                    pass
            elif event.key == pygame.K_UP:
                self.game_state.cursor_position = (self.game_state.cursor_position[0], max(0, self.game_state.cursor_position[1] - 1))                    
            elif event.key == pygame.K_DOWN:
                self.game_state.cursor_position = (self.game_state.cursor_position[0], min(self.game_state.map_size[1] - 1, self.game_state.cursor_position[1] + 1))
            elif event.key == pygame.K_LEFT:
                self.game_state.cursor_position = (max(0, self.game_state.cursor_position[0] - 1), self.game_state.cursor_position[1])
            elif event.key == pygame.K_RIGHT:
                self.game_state.cursor_position = (min(self.game_state.map_size[0] - 1, self.game_state.cursor_position[0] + 1), self.game_state.cursor_position[1])