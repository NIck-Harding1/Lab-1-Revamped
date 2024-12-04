import os

class VotingSystem:

    def __init__(self):
        self.candidates = ["John", "Jane"]
        self.votes = [0, 0]
        self.file_name = "votes.txt"
        self.load_votes()

    def load_votes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                lines = file.readlines()
                if len(lines) == 2:
                    self.votes = [int(line.strip()) for line in lines]
        else:
            self.save_votes()

    def save_votes(self):
        with open(self.file_name, "w") as file:
            file.writelines(f"{vote}\n" for vote in self.votes)

    def cast_vote(self, candidate_index: int):
        if 0 <= candidate_index < len(self.candidates):
            self.votes[candidate_index] += 1
            self.save_votes()
        else:
            raise ValueError("Invalid candidate index.")

    def get_results(self):
        total_votes = sum(self.votes)
        return {self.candidates[i]: self.votes[i] for i in range(len(self.candidates))}, total_votes
