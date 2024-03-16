from enum import Enum

class GamePhaseTypes(Enum):
    UNIT_SELECTION = "unit_selection"
    UNIT_ACTION = "unit_action"
    ENEMY_ACTION = "enemy_action"
    PLAYER_VICTORY = "player_victory"
    PLAYER_DEFEAT = "player_defeat"
    PLAYER_IDLE = "player_idle"
    PLAYER_UNIT_MOVE = "player_unit_move"
    PLAYER_UNIT_ACTION = "player_unit_action"

class GamePhase:
    def __init__(self):
        pass

    def enter_state(self):
        pass

    def exit_state(self):
        pass

    def update(self, events):
        pass

    def render(self, screen):
        pass

class BattlePhase(GamePhase):
    def __init__(self, game_state, callbacks=None):
        super().__init__()
        self.game_state = game_state
        self.callbacks = callbacks
        self.cursor_color = (0, 255, 0)


