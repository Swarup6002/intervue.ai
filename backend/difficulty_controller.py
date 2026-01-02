class DifficultyController:
    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def adjust_difficulty(self, current_level, score):
        idx = self.levels.index(current_level)
        
        if score >= 8:
            new_idx = min(idx + 1, len(self.levels) - 1)
        elif score <= 4:
            new_idx = max(idx - 1, 0)
        else:
            new_idx = idx
            
        return self.levels[new_idx]