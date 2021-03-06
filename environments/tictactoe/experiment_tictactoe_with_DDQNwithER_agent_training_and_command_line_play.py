from agents import CommandLineAgent, DeepQLearningAgent, DDQNAgentWithER
from environments.tictactoe import TicTacToeGameState
from runners import run_for_n_games_and_print_stats, run_step

if __name__ == "__main__":
    gs = TicTacToeGameState()
    agent0 = DeepQLearningAgent(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent1 = DDQNAgentWithER(action_space_size=gs.get_action_space_size(), neurons_per_hidden_layer=128,
                                hidden_layers=5)
    agent0.alpha = 0.1
    agent0.epsilon = 0.005
    agent1.alpha = 0.1
    agent1.epsilon = 0.005

    for i in range(100):
        run_for_n_games_and_print_stats([agent0, agent1], gs, 1000)

    agent0.epsilon = -1.0
    agent1.epsilon = -1.0
    run_for_n_games_and_print_stats([agent0, agent1], gs, 100)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([agent0, CommandLineAgent()], gs_clone)
        print(gs_clone)

    gs_clone = gs.clone()
    while not gs_clone.is_game_over():
        run_step([CommandLineAgent(), agent1], gs_clone)
        print(gs_clone)
