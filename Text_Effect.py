import random
import time

def cool_text_effect(text):
  """Prints text with a cool, randomized character effect."""
  for char in text:
    for _ in range(5):  # Number of random character iterations
      random_char = chr(random.randint(33, 126)) # Printable ASCII range
      print(random_char, end='', flush=True)
      time.sleep(0.02)  # Short delay for the effect
    print(char, end='', flush=True)
    time.sleep(0.05) # Small pause between characters

  print() #newline

def simple_countdown(seconds):
    """A basic countdown timer."""
    for i in range(seconds, 0, -1):
        print(f"T-{i}...", end='\r') #carriage return to overwrite the previous line.
        time.sleep(1)
    print("Blastoff!")

def main():
    cool_text_effect("Initializing...")
    time.sleep(1)
    cool_text_effect("System online.")
    time.sleep(0.5)
    print("Preparing for launch...")
    simple_countdown(5)
    cool_text_effect("Have a great day!")


if __name__ == "__main__":
    main()