import tkinter as tk
from tkinter import messagebox
import random
import time

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors - Premium Edition")
        self.root.geometry("600x700")
        self.root.config(bg="#0f0f1a")
        self.root.resizable(True, True)
        
        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.streak = 0
        self.choices = ["Rock", "Paper", "Scissors"]
        self.animation_running = False
        
        # Emoji mappings
        self.emoji_map = {
            "Rock": "🪨", "Paper": "📄", "Scissors": "✂️"
        }
        
        # Initialize UI
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        """Create welcome screen"""
        self.welcome_frame = tk.Frame(self.root, bg="#0f0f1a")
        self.welcome_frame.pack(fill="both", expand=True)
        
        # Title
        title = tk.Label(
            self.welcome_frame,
            text="ROCK PAPER SCISSORS",
            font=("Arial", 36, "bold"),
            bg="#0f0f1a",
            fg="#00ffff"
        )
        title.pack(pady=50)
        
        # Subtitle
        subtitle = tk.Label(
            self.welcome_frame,
            text="✨ Ultimate Battle Arena ✨",
            font=("Arial", 16, "italic"),
            bg="#0f0f1a",
            fg="#c4c4c4"
        )
        subtitle.pack(pady=10)
        
        # Start button
        self.start_btn = tk.Button(
            self.welcome_frame,
            text="START GAME",
            font=("Arial", 20, "bold"),
            bg="#00ffff",
            fg="#0f0f1a",
            padx=40,
            pady=15,
            bd=0,
            cursor="hand2",
            command=self.start_game
        )
        self.start_btn.pack(pady=40)
        
        # Instructions
        instructions = tk.Label(
            self.welcome_frame,
            text="Best of 5 Rounds • Track Your Streak • Beat the Computer!",
            font=("Arial", 11),
            bg="#0f0f1a",
            fg="#888888"
        )
        instructions.pack(pady=20)
        
        # Credit
        creator = tk.Label(
            self.welcome_frame,
            text="🎮 Premium Edition 🎮",
            font=("Arial", 10),
            bg="#0f0f1a",
            fg="#555555"
        )
        creator.pack(side="bottom", pady=20)
        
    def start_game(self):
        """Transition to main game"""
        self.welcome_frame.destroy()
        self.create_game_screen()
        
    def create_game_screen(self):
        """Create main game interface"""
        # Main container with scrolling
        self.canvas = tk.Canvas(self.root, bg="#0f0f1a", highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#0f0f1a")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Header section
        header_frame = tk.Frame(self.scrollable_frame, bg="#1a1a2e", height=100)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Game title
        title = tk.Label(
            header_frame,
            text="⚔️ ROCK PAPER SCISSORS ⚔️",
            font=("Arial", 20, "bold"),
            bg="#1a1a2e",
            fg="#00ffff"
        )
        title.pack(pady=25)
        
        # Stats frame
        stats_frame = tk.Frame(self.scrollable_frame, bg="#0f0f1a")
        stats_frame.pack(pady=10)
        
        # Player Score Card
        player_frame = tk.Frame(stats_frame, bg="#1a1a2e", relief="raised", bd=2)
        player_frame.pack(side="left", padx=20, pady=10)
        
        tk.Label(player_frame, text="PLAYER", font=("Arial", 14, "bold"), 
                bg="#1a1a2e", fg="#00ff88").pack(pady=5)
        self.player_score_label = tk.Label(player_frame, text="0", font=("Arial", 36, "bold"),
                                          bg="#1a1a2e", fg="#00ff88")
        self.player_score_label.pack(pady=5)
        
        # VS Label
        tk.Label(stats_frame, text="VS", font=("Arial", 24, "bold"),
                bg="#0f0f1a", fg="#ff4444").pack(side="left", padx=20)
        
        # Computer Score Card
        computer_frame = tk.Frame(stats_frame, bg="#1a1a2e", relief="raised", bd=2)
        computer_frame.pack(side="left", padx=20, pady=10)
        
        tk.Label(computer_frame, text="COMPUTER", font=("Arial", 14, "bold"),
                bg="#1a1a2e", fg="#ff4444").pack(pady=5)
        self.computer_score_label = tk.Label(computer_frame, text="0", font=("Arial", 36, "bold"),
                                            bg="#1a1a2e", fg="#ff4444")
        self.computer_score_label.pack(pady=5)
        
        # Streak and Round frame
        info_frame = tk.Frame(self.scrollable_frame, bg="#0f0f1a")
        info_frame.pack(pady=10)
        
        self.streak_label = tk.Label(info_frame, text=f"🔥 Streak: {self.streak}",
                                    font=("Arial", 14, "bold"), bg="#0f0f1a", fg="#ffaa00")
        self.streak_label.pack(side="left", padx=20)
        
        self.round_label = tk.Label(info_frame, text=f"Round: {self.rounds_played}/5",
                                   font=("Arial", 14, "bold"), bg="#0f0f1a", fg="#888888")
        self.round_label.pack(side="left", padx=20)
        
        # Game area - Choices display
        game_area = tk.Frame(self.scrollable_frame, bg="#0f0f1a")
        game_area.pack(pady=20)
        
        # User choice
        user_frame = tk.Frame(game_area, bg="#0f0f1a")
        user_frame.pack(side="left", padx=40)
        
        self.user_choice_label = tk.Label(user_frame, text="❓", font=("Arial", 60),
                                         bg="#0f0f1a", fg="#00ff88")
        self.user_choice_label.pack()
        
        self.user_choice_text = tk.Label(user_frame, text="Your Choice", font=("Arial", 12),
                                        bg="#0f0f1a", fg="#888888")
        self.user_choice_text.pack()
        
        # VS Icon
        tk.Label(game_area, text="⚔️", font=("Arial", 40), bg="#0f0f1a", fg="#ff4444").pack(side="left", padx=20)
        
        # Computer choice
        computer_choice_frame = tk.Frame(game_area, bg="#0f0f1a")
        computer_choice_frame.pack(side="left", padx=40)
        
        self.comp_choice_label = tk.Label(computer_choice_frame, text="❓", font=("Arial", 60),
                                         bg="#0f0f1a", fg="#ff4444")
        self.comp_choice_label.pack()
        
        self.comp_choice_text = tk.Label(computer_choice_frame, text="Computer's Choice", font=("Arial", 12),
                                        bg="#0f0f1a", fg="#888888")
        self.comp_choice_text.pack()
        
        # Result label
        self.result_label = tk.Label(self.scrollable_frame, text="Make your move!",
                                    font=("Arial", 20, "bold"), bg="#0f0f1a", fg="#ffffff")
        self.result_label.pack(pady=20)
        
        # Action buttons
        button_frame = tk.Frame(self.scrollable_frame, bg="#0f0f1a")
        button_frame.pack(pady=20)
        
        # Rock button
        self.rock_btn = tk.Button(button_frame, text="🪨 ROCK", font=("Arial", 14, "bold"),
                                 bg="#4e9af1", fg="white", width=12, height=2,
                                 bd=0, cursor="hand2", command=lambda: self.play("Rock"))
        self.rock_btn.pack(side="left", padx=10)
        
        # Paper button
        self.paper_btn = tk.Button(button_frame, text="📄 PAPER", font=("Arial", 14, "bold"),
                                  bg="#00c896", fg="white", width=12, height=2,
                                  bd=0, cursor="hand2", command=lambda: self.play("Paper"))
        self.paper_btn.pack(side="left", padx=10)
        
        # Scissors button
        self.scissors_btn = tk.Button(button_frame, text="✂️ SCISSORS", font=("Arial", 14, "bold"),
                                     bg="#ff6b6b", fg="white", width=12, height=2,
                                     bd=0, cursor="hand2", command=lambda: self.play("Scissors"))
        self.scissors_btn.pack(side="left", padx=10)
        
        # Control buttons
        control_frame = tk.Frame(self.scrollable_frame, bg="#0f0f1a")
        control_frame.pack(pady=30)
        
        reset_btn = tk.Button(control_frame, text="🔄 RESET GAME", font=("Arial", 12, "bold"),
                             bg="#ffaa00", fg="#0f0f1a", width=12, height=1,
                             bd=0, cursor="hand2", command=self.reset_game)
        reset_btn.pack(side="left", padx=10)
        
        exit_btn = tk.Button(control_frame, text="🚪 EXIT", font=("Arial", 12, "bold"),
                            bg="#ff4444", fg="white", width=12, height=1,
                            bd=0, cursor="hand2", command=self.root.destroy)
        exit_btn.pack(side="left", padx=10)
        
        # Bind mouse wheel for scrolling
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def animate_choice(self, label, choice, is_user=True):
        """Animate the choice selection"""
        emoji = self.emoji_map.get(choice, "❓")
        
        # Animation frames
        frames = ["⏳", "⚡", "✨", emoji]
        for frame in frames:
            label.config(text=frame)
            self.root.update()
            time.sleep(0.08)
        
        if is_user:
            self.user_choice_text.config(text=f"You chose {choice}!", fg="#00ff88")
        else:
            self.comp_choice_text.config(text=f"Computer chose {choice}!", fg="#ff4444")
    
    def flash_result(self, color):
        """Flash the result label"""
        original_color = self.result_label.cget("fg")
        for _ in range(3):
            self.result_label.config(fg=color)
            self.root.update()
            time.sleep(0.1)
            self.result_label.config(fg=original_color)
            self.root.update()
            time.sleep(0.1)
    
    def play(self, user_choice):
        """Main game logic with animations"""
        if self.animation_running or self.rounds_played >= 5:
            return
        
        self.animation_running = True
        
        # Disable buttons during animation
        self.rock_btn.config(state="disabled")
        self.paper_btn.config(state="disabled")
        self.scissors_btn.config(state="disabled")
        
        computer_choice = random.choice(self.choices)
        
        # Animate choices
        self.animate_choice(self.user_choice_label, user_choice, True)
        self.animate_choice(self.comp_choice_label, computer_choice, False)
        
        # Determine winner
        if user_choice == computer_choice:
            result = "TIE! 🤝"
            result_color = "#ffaa00"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "YOU WIN! 🎉"
            result_color = "#00ff88"
            self.user_score += 1
            self.streak += 1
        else:
            result = "COMPUTER WINS! 💀"
            result_color = "#ff4444"
            self.computer_score += 1
            self.streak = 0
        
        self.rounds_played += 1
        
        # Update displays
        self.result_label.config(text=result, fg=result_color)
        self.player_score_label.config(text=str(self.user_score))
        self.computer_score_label.config(text=str(self.computer_score))
        self.streak_label.config(text=f"🔥 Streak: {self.streak}")
        self.round_label.config(text=f"Round: {self.rounds_played}/5")
        
        # Animation effects
        self.flash_result(result_color)
        
        # Re-enable buttons
        self.rock_btn.config(state="normal")
        self.paper_btn.config(state="normal")
        self.scissors_btn.config(state="normal")
        
        # Check for game end
        if self.rounds_played >= 5:
            self.root.after(500, self.end_game)
        
        self.animation_running = False
    
    def end_game(self):
        """Handle game end"""
        if self.user_score > self.computer_score:
            message = f"🏆 VICTORY! 🏆\n\nFinal Score: {self.user_score} - {self.computer_score}\nYou are the Champion!"
        elif self.user_score < self.computer_score:
            message = f"💀 DEFEAT! 💀\n\nFinal Score: {self.user_score} - {self.computer_score}\nBetter luck next time!"
        else:
            message = f"🤝 DRAW! 🤝\n\nFinal Score: {self.user_score} - {self.computer_score}\nWell played!"
        
        if messagebox.askyesno("Game Over", f"{message}\n\nWould you like to play again?"):
            self.reset_game()
        else:
            self.root.destroy()
    
    def reset_game(self):
        """Reset game state"""
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.streak = 0
        
        # Reset UI
        self.player_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        self.streak_label.config(text=f"🔥 Streak: 0")
        self.round_label.config(text="Round: 0/5")
        self.result_label.config(text="Game Reset! Make your move!", fg="#ffffff")
        
        # Reset choice displays
        self.user_choice_label.config(text="❓")
        self.comp_choice_label.config(text="❓")
        self.user_choice_text.config(text="Your Choice")
        self.comp_choice_text.config(text="Computer's Choice")
        
        # Enable all buttons
        self.rock_btn.config(state="normal")
        self.paper_btn.config(state="normal")
        self.scissors_btn.config(state="normal")
        
        self.animation_running = False

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()