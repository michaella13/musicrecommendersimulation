"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from recommender import load_songs, recommend_songs

WIDTH = 54


def print_recommendation(rank: int, song: dict, score: float, reasons: list) -> None:
    bar = "─" * WIDTH
    title = song["title"]
    score_str = f"Score: {score:.2f}"
    # Pad title and score so they fill the line
    gap = WIDTH - len(f"  #{rank}  {title}  {score_str}")
    header = f"  #{rank}  {title}{' ' * max(1, gap)}{score_str}"
    print(header)
    print(f"  {bar}")
    for reason in reasons:
        print(f"      • {reason}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.8,
        "tempo_bpm": 120,
        "danceability": 0.8,
        "acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\n  Top {len(recommendations)} Recommendations")
    print(f"  {'═' * WIDTH}\n")
    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print_recommendation(rank, song, score, reasons)


if __name__ == "__main__":
    main()
