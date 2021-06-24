import click

from war import War

###################################
# Settings
###################################


@click.command()
@click.argument('game_name', type=click.Choice(['War']), default='War')
@click.option('--num_players', type=int, default=2,
              help='Number of players.')
@click.option('--player_names', type=str, default='Player1, Player2',
              help='Custom name of the players.')
def main(game_name, num_players, player_names):
    """
    Game launcher

    :param game_name    : Name of the game
    :param player_names : List of player names
    """  
    war_game = eval(game_name)(player_names=player_names.split(','), num_players=num_players)
    print(war_game.start())


if __name__ == '__main__':
    main()

