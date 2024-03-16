from phases.game_phase import GamePhaseTypes
from phases.player_idle_phase import PlayerIdlePhase
from phases.player_unit_move_phase import PlayerUnitMovePhase
from phases.player_unit_action_phase import PlayerUnitActionPhase

class PhaseMachine:
    def __init__(self, game_state, current_phase_type):
        self.game_state = game_state
        self.callbacks = {
            'change_phase': self.change_phase,
        }
        self.current_phase_type = current_phase_type
        self.phases = {
            GamePhaseTypes.PLAYER_IDLE: PlayerIdlePhase(self.game_state, self.callbacks),
            GamePhaseTypes.PLAYER_UNIT_MOVE: PlayerUnitMovePhase(self.game_state, self.callbacks),
            GamePhaseTypes.PLAYER_UNIT_ACTION: PlayerUnitActionPhase(self.game_state, self.callbacks)
        }
        self.current_phase = self.phases[self.current_phase_type] \
            if self.current_phase_type in self.phases else self.phases[GamePhaseTypes.PLAYER_IDLE]


    def handle_event(self, event):
        self.current_phase.handle_event(event)

    def change_phase(self, new_phase):
        if new_phase in self.phases:
            self.current_phase = self.phases[new_phase]
            self.game_state.current_phase = new_phase
            self.game_state.cursor_color = self.phases[new_phase].cursor_color
            print(f"Changed to {new_phase}")

    def update(self):
        pass

    def render(self, screen):
        if self.active_state:
            self.active_state.render(screen)
