from agents import CommandLineAgent, DeepQLearningAgent, ReinforceMeanBaselineAgent, RandomAgent
from environments.tictactoe import TicTacToeGameState
from runners import run_for_n_games_and_print_stats, run_step

if __name__ == "__main__":
    gs = TicTacToeGameState()
    agent0 = ReinforceMeanBaselineAgent(
        state_space_size=gs.get_vectorized_state().shape[0],
        action_space_size=gs.get_action_space_size())
    agent1 = RandomAgent()

    for i in range(100):
        run_for_n_games_and_print_stats([agent0, agent1], gs, 1000)

    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([agent0, CommandLineAgent()], gs_clone)
        print(gs_clone)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([CommandLineAgent(), agent1], gs_clone)
        print(gs_clone)
