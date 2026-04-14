"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from pathlib import Path
from recommender import load_songs, recommend_songs

DATA_PATH = Path(__file__).parent.parent / "data" / "songs.csv"

def main() -> None:
    songs = load_songs(DATA_PATH)
    print(f"Loaded songs: {len(songs)}")

    # Taste profile: target values for each scored feature.
    # genre / mood: the user's preferred category (matched via one-hot encoding).
    # target_energy: 0.0 (very calm) → 1.0 (very intense).
    # target_acousticness: 0.0 (electronic/produced) → 1.0 (fully acoustic).
    # target_danceability: 0.0 (not danceable) → 1.0 (highly danceable).
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "target_energy": 0.80,
        "target_acousticness": 0.20,
        "target_danceability": 0.85,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    divider = "─" * 44
    print(f"\n{divider}")
    print(f"  Top {len(recommendations)} Recommendations")
    print(f"  Genre: {user_prefs['genre']}  |  Mood: {user_prefs['mood']}")
    print(divider)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']} by {song['artist']}")
        print(f"       Score: {score:.2f} / 10.00")
        print(f"       Why:")
        for reason in explanation.split(", "):
            print(f"         - {reason}")

    print(f"\n{divider}\n")


if __name__ == "__main__":
    main()
