from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_hard_difficulty_range():
    # Hard difficulty should return a range of 1-500
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 500

def test_update_score_too_high():
    # Too High should not add or subtract points
    new_score = update_score(100, "Too High", 1)
    assert new_score == 100

def test_update_score_too_low():
    # Too Low should not add or subtract points
    new_score = update_score(100, "Too Low", 1)
    assert new_score == 100
