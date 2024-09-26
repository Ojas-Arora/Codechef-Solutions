def check_win(wins, draws, losses):
    team_points = wins + 0.5 * draws
    opponent_points = losses + 0.5 * draws
    remaining_matches = 4 - (wins + draws + losses)
    
    if team_points > opponent_points:
        return "Yes"
    
    if team_points + remaining_matches > opponent_points:
        return "Yes"
    
    return "No"

wins, draws, losses = map(int, input().split())
print(check_win(wins, draws, losses))
