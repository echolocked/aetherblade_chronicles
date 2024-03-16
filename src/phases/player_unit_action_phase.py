from src.phases.game_phase import GamePhase, BattlePhase

class PlayerUnitActionPhase(BattlePhase):
    def __init__(self, game_state, callbacks=None):
        super().__init__(game_state, callbacks)
        self.cursor_color = (255, 0, 0)

    def handle_event(self, event):
        pass