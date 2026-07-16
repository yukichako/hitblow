from pathlib import Path

SCORE_FILE = Path("scores.txt")


def save_score(tries):
    """挑戦回数をファイルに保存する"""
    with open(SCORE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{tries}\n")


def load_scores():
    """保存されたスコアを読み込む"""
    if not SCORE_FILE.exists():
        return []

    with open(SCORE_FILE, "r", encoding="utf-8") as f:
        scores = [int(line.strip()) for line in f if line.strip()]

    return scores


def show_scores():
    """スコア一覧を表示する"""
    scores = load_scores()

    if not scores:
        print("まだスコアはありません。")
        return

    print("\n=== スコア一覧 ===")
    for i, score in enumerate(scores, start=1):
        print(f"{i}回目 : {score}回")

    print("------------------")
    print(f"プレイ回数 : {len(scores)}")
    print(f"最少回数   : {min(scores)}回")
    print(f"平均回数   : {sum(scores)/len(scores):.1f}回")