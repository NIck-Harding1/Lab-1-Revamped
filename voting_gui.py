import tkinter as tk
from tkinter import messagebox
from voting_system import VotingSystem

class VotingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")
        self.voting_system = VotingSystem()

        self.label = tk.Label(root, text="Vote for your favorite candidate", font=("Arial", 16))
        self.label.pack(pady=10)

        self.john_button = tk.Button(root, text="Vote for John", command=lambda: self.vote(0))
        self.john_button.pack(pady=5)

        self.jane_button = tk.Button(root, text="Vote for Jane", command=lambda: self.vote(1))
        self.jane_button.pack(pady=5)

        self.results_button = tk.Button(root, text="Show Results", command=self.show_results)
        self.results_button.pack(pady=20)

    def vote(self, candidate_index: int):
        try:
            self.voting_system.cast_vote(candidate_index)
            candidate_name = self.voting_system.candidates[candidate_index]
            messagebox.showinfo("Vote Cast", f"You voted for {candidate_name}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_results(self):
        results, total = self.voting_system.get_results()
        results_message = "\n".join([f"{name}: {votes}" for name, votes in results.items()])
        results_message += f"\n\nTotal Votes: {total}"
        messagebox.showinfo("Results", results_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
