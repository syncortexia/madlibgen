from colorama import init, Fore, Style
import random
import time

init()

stories = {
    1: {
        "title": "A Day at the Zoo",
        "template": """Yesterday, I went to the {adjective} zoo. In the first exhibit, I saw a {adjective} 
{noun} {verb_ing} up and down. In the next exhibit, a {adjective} {noun} was {verb_ing} with 
a {noun}. Later, I watched a {adjective} {noun} {verb_ing} while eating a {adjective} 
{noun}. What a {adjective} day!""",
        "words": ["adjective", "adjective", "noun", "verb_ing", "adjective", "noun", "verb_ing",
                 "noun", "adjective", "noun", "verb_ing", "adjective", "noun", "adjective"]
    },
    2: {
        "title": "Space Adventure",
        "template": """In the year {number}, a {adjective} spacecraft took off from {place}. 
The {adjective} captain {verb_ed} the {noun} as they zoomed past {number} {plural_noun}. 
Suddenly, a {adjective} {noun} appeared on the radar! The crew had to {verb} quickly to avoid a 
collision. "That was {adjective}!" exclaimed the captain.""",
        "words": ["number", "adjective", "place", "adjective", "verb_ed", "noun", "number",
                 "plural_noun", "adjective", "noun", "verb", "adjective"]
    },
    3: {
        "title": "The Magic Recipe",
        "template": """In a {adjective} kitchen, a {adjective} chef was creating a new recipe. First, they 
{verb_ed} {number} {plural_noun} into a bowl. Then, they {verb_ed} in some {adjective} {noun} 
and sprinkled {plural_noun} on top. After {verb_ing} for {number} minutes, the dish turned 
{adjective}! Everyone who tasted it became {adjective}.""",
        "words": ["adjective", "adjective", "verb_ed", "number", "plural_noun", "verb_ed", "adjective",
                 "noun", "plural_noun", "verb_ing", "number", "adjective", "adjective"]
    },
    4: {
        "title": "Superhero Origins",
        "template": """One {adjective} day, while {verb_ing} at {place}, {name} discovered their 
{adjective} superpower. They could {verb} any {noun} by just {verb_ing} at it! They decided to 
become {article} {adjective} superhero called '{adjective} {noun}'. Their arch-nemesis was 
the {adjective} Dr. {noun}.""",
        "words": ["adjective", "verb_ing", "place", "name", "adjective", "verb", "noun", "verb_ing",
                 "article", "adjective", "adjective", "noun", "adjective", "noun"]
    },
    5: {
        "title": "Camping Adventure",
        "template": """Last weekend, I went camping with my {adjective} friend at {place}. We packed our 
{adjective} {noun} and {number} {plural_noun}. While {verb_ing} in the woods, we saw a 
{adjective} {noun} that was {verb_ing} near our tent! We {verb_ed} so fast, we forgot our 
{adjective} {noun} behind.""",
        "words": ["adjective", "place", "adjective", "noun", "number", "plural_noun", "verb_ing",
                 "adjective", "noun", "verb_ing", "verb_ed", "adjective", "noun"]
    }
}

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    """Print text with color and style."""
    print(f"{style}{color}{text}{Style.RESET_ALL}")

def get_word_input(word_type, current_num, total_num):
    """Get user input for a specific type of word with proper formatting and progress counter."""
    prompts = {
        "noun": "Enter a noun (person, place, or thing)",
        "plural_noun": "Enter a plural noun (people, places, or things)",
        "verb": "Enter a verb (action word)",
        "verb_ing": "Enter a verb ending in -ing",
        "verb_ed": "Enter a verb in past tense (-ed)",
        "adjective": "Enter an adjective (descriptive word)",
        "place": "Enter a place",
        "number": "Enter a number",
        "name": "Enter a name",
        "article": "Enter an article (a/an/the)"
    }
    
    prompt = prompts.get(word_type, f"Enter a {word_type}")
    print_colored(f"\n[{current_num}/{total_num}] {prompt}: ", Fore.CYAN, Style.BRIGHT)
    return input().strip()

def play_madlibs():
    """Main game function."""
    while True:
        print_colored("\n=== Available Stories ===", Fore.YELLOW, Style.BRIGHT)
        for num, story in stories.items():
            print_colored(f"{num}. {story['title']}", Fore.YELLOW)
        print_colored("0. Exit", Fore.YELLOW)
        
        choice = input("\nChoose a story number (or 0 to exit): ").strip()
        if choice == "0":
            break
        
        try:
            story_num = int(choice)
            if story_num not in stories:
                raise ValueError
        except ValueError:
            print_colored("Invalid choice! Please try again.", Fore.RED)
            continue
        
        print_colored(f"\nLet's create '{stories[story_num]['title']}'!", Fore.GREEN, Style.BRIGHT)
        total_words = len(stories[story_num]['words'])
        words = {}
        for i, word_type in enumerate(stories[story_num]['words'], 1):
            words[f"{word_type}_{i}"] = get_word_input(word_type, i, total_words)
        
        story = stories[story_num]['template']
        for i, word_type in enumerate(stories[story_num]['words'], 1):
            story = story.replace("{" + word_type + "}", words[f"{word_type}_{i}"])
        
        print_colored("\n=== Your Mad Libs Story ===", Fore.MAGENTA, Style.BRIGHT)
        time.sleep(1)
        print_colored(story, Fore.WHITE, Style.BRIGHT)
        
        print_colored("\nWould you like to create another story? (y/n): ", Fore.CYAN)
        if input().lower().strip() != 'y':
            break

def main():
    """Main program function."""
    print_colored("""
    ===============================
    Welcome to Mad Libs Generator!
    ===============================
    """, Fore.GREEN, Style.BRIGHT)
    
    play_madlibs()
    
    print_colored("\nThanks for playing Mad Libs! Goodbye!", Fore.GREEN, Style.BRIGHT)

if __name__ == "__main__":
    main() 