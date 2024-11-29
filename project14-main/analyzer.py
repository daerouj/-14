import pymorphy3

# Ініціалізація морфологічного аналізатора
morph = pymorphy3.MorphAnalyzer(lang="uk")

def analyze_verb(word):
    """Функція для перевірки, чи є слово дієсловом."""
    parsed_word = morph.parse(word)  # Отримуємо всі варіанти аналізу слова
 

    for p in parsed_word:
        if 'VERB' in p.tag:  
            return f"{word} - дієслово"
        else:
            return f"{word} - не дієслово"

        