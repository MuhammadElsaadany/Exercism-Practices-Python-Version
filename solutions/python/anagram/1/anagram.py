def find_anagrams(word, candidates):
    anagrams = []
    word_lwr = word.lower()

    for candidate in candidates:
        candidate_lwr = candidate.lower()

        if candidate_lwr == word_lwr:
            continue

        target_letters = list(word_lwr)
        remaining_candidate_letters = list(candidate_lwr)

        for candidate_letter in candidate_lwr:
            if candidate_letter in target_letters:
                target_letters.remove(candidate_letter)
                remaining_candidate_letters.remove(candidate_letter)

        if not target_letters and not remaining_candidate_letters:
            anagrams.append(candidate)
            
    return anagrams