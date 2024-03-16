import pygame
from phases.game_phase import GamePhaseTypes, BattlePhase

class PlayerUnitMovePhase(BattlePhase):
    def __init__(self, game_state, callbacks=None):
        super().__init__(game_state, callbacks)
        self.game_state.cursor_color = (0, 0, 255)

    def handle_event(self, event):
        selected_unit = self.game_state.selected_unit
        cursor_position = self.game_state.cursor_position
        move_distance = abs(selected_unit.position[0] - cursor_position[0]) + abs(selected_unit.position[1] - cursor_position[1])
        if move_distance > selected_unit.vocation.base_move:
            self.game_state.cursor_color = (128, 128, 128)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if move_distance <= selected_unit.vocation.base_move:
                    if not self.game_state.get_unit_at(cursor_position):
                        self.game_state.move_unit(selected_unit, cursor_position)
                        self.callbacks['change_phase'](GamePhaseTypes.PLAYER_IDLE)

            elif event.key == pygame.K_UP:
                self.game_state.cursor_position = (self.game_state.cursor_position[0], max(0, self.game_state.cursor_position[1] - 1))                    
            elif event.key == pygame.K_DOWN:
                self.game_state.cursor_position = (self.game_state.cursor_position[0], min(self.game_state.map_size[1] - 1, self.game_state.cursor_position[1] + 1))
            elif event.key == pygame.K_LEFT:
                self.game_state.cursor_position = (max(0, self.game_state.cursor_position[0] - 1), self.game_state.cursor_position[1])
            elif event.key == pygame.K_RIGHT:
                self.game_state.cursor_position = (min(self.game_state.map_size[0] - 1, self.game_state.cursor_position[0] + 1), self.game_state.cursor_position[1])