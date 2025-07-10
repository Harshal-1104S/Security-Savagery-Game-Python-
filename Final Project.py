#Harshal Mehta
#Security Savagery
#Start date: December 19,2023
#End Date: January 11, 2024


# Import necessary libraries
import pygame
import sys #https://www.geeksforgeeks.org/python-sys-module/
import textwrap #https://docs.python.org/3/library/textwrap.html
import time
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
FPS = 60 #Python - Displaying real time FPS at which webcam/video file is processed using OpenCV - GeeksforGeeks
MAX_LINE_LENGTH = 30
TIME_LIMIT = 15  # Set the time limit in seconds

# Colors
DARK_COLOR = (30, 30, 30)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
QUESTION_BOX_COLOR = (0, 0, 255)  # Blue for the question box
OPTION_BOX_COLOR = (0, 255, 0)    # Green for option boxes

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Security Savagery")

# Fonts
font = pygame.font.Font(None, 28)  # Reduced font size

# Load sounds
pygame.mixer.init()
music1 = pygame.mixer.Sound("powerful trap.mp3")
music2 = pygame.mixer.Sound("happy.wav")
music3 = pygame.mixer.Sound("womp womp.mp3")
music4 = pygame.mixer.Sound("instructions voice.mp3")

# Load backgrounds with resizing
background1 = pygame.transform.scale(pygame.image.load("fox police.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = pygame.transform.scale(pygame.image.load("wrong answer screen.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background3 = pygame.transform.scale(pygame.image.load("winner.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background4 = pygame.transform.scale(pygame.image.load("background5.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background5 = pygame.transform.scale(pygame.image.load("instructions background.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
background6 = pygame.transform.scale(pygame.image.load("credits background.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
loading_background = pygame.transform.scale(pygame.image.load("loading screen2.0.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Buttons/Icons
button_credits = pygame.Rect(50, 100, 200, 50)
button_instructions = pygame.Rect(50, 200, 200, 50)
button_exit = pygame.Rect(50, 300, 200, 50)
button_game = pygame.Rect(50, 400, 200, 50)
button_back = pygame.Rect(50, SCREEN_HEIGHT - 100, 200, 50)
button_reset = pygame.Rect(260, SCREEN_HEIGHT - 100, 200, 50)  # Reset button inside the game

# Game variables
questions = [
    {"question": "What is cybersecurity?", "options": ["A type of online game", "Protecting systems and programs from digital attacks", "A new social media platform"], "correct": 1, "explanation": "Cybersecurity is the practice of protecting computer systems, networks, and programs from digital attacks. This involves implementing measures to ensure the confidentiality, integrity, and availability of information."},
    {"question": "What is two-factor authentication?", "options": ["Using two different passwords", "providing two different authentication factors to verify your identity", "A type of computer virus"], "correct": 1, "explanation": "Two-factor authentication (2FA) is a security process in which a user provides two different authentication factors to verify their identity. It adds an extra layer of security beyond just a username and password."},
    {"question": "How often should you update your passwords?", "options": ["Once a year", "Only when you forget them", "Regularly, at least every 3-6 months"], "correct": 2, "explanation": "Passwords should be updated regularly, typically at least every 3-6 months. Regular password updates help mitigate the risk of unauthorized access and enhance overall account security."},
    {"question": "What is phishing?", "options": ["A way to catch fish", "A type of computer game", "Attempts to obtain information"], "correct": 2, "explanation": "Phishing is a type of cyber attack where attackers attempt to obtain sensitive information, such as usernames, passwords, and credit card details, by posing as a trustworthy entity. This is often done through deceptive emails or fraudulent websites."},
    {"question": "Why is it important to use antivirus software?", "options": ["To play computer games", "Prevent viruses from infecting your computer", "It's not important"], "correct": 1, "explanation": "Antivirus software is essential to prevent viruses and malicious software from infecting your computer. It detects, blocks, and removes various types of malware, safeguarding your system and data from potential threats."},
    {"question": "What does a firewall do?", "options": ["Keeps you warm in winter", "Monitors incoming and outgoing network traffic", "It's a type of computer screen"], "correct": 1, "explanation": "A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, preventing unauthorized access and ensuring data security."},
    {"question": "What is encryption?", "options": ["A way to hide your computer files", "Converting information into code to prevent unauthorized access", "A type of computer bug"], "correct": 1, "explanation": "Encryption is the process of converting information or data into code to prevent unauthorized access. It is commonly used to secure sensitive data during transmission and storage, ensuring that only authorized parties can decipher and access the original information."},
]

# Add 8 more questions
questions.extend([
    {"question": "What is a VPN?", "options": ["Virtual Private Network", "Very Personal Name", "Visual Processing Network"], "correct": 0, "explanation": "A VPN, or Virtual Private Network, is a technology that provides a secure and encrypted connection over a public network, typically the internet."},
    {"question": "What does the term PAN refer to?", "options": ["A type of apple", "Personal Area Network", "A kind of hardware"], "correct": 1, "explanation": "PAN, or Personal Area Network, refers to a network that connects electronic devices within the user's immediate area, typically within the range of an individual person."},
    {"question": "What is a keylogger?", "options": ["A musical instrument", "A device that records keystrokes", "A type of password"], "correct": 1, "explanation": "A keylogger is a type of software or hardware that records the keystrokes made by a user, often used to capture sensitive information such as passwords."},
    {"question": "What is a DDoS attack?", "options": ["Distributed Denial of Service attack", "Dance Dance Online Service", "Digital Data Overload Syndrome"], "correct": 0, "explanation": "DDoS, or Distributed Denial of Service attack, is a malicious attempt to disrupt the regular functioning of a network or website by overwhelming it with a flood of internet traffic from multiple sources."},
    {"question": "What is social engineering in the context of cybersecurity?", "options": ["Making friends online", "Manipulating people into revealing confidential information", "Building social media networks"], "correct": 1, "explanation": "Social engineering involves manipulating individuals into divulging confidential information, often by posing as a trustworthy entity or exploiting human psychology."},
    {"question": "What is a firewall used for?", "options": ["To keep you warm", "To monitor network traffic", "To store files"], "correct": 1, "explanation": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet."},
    {"question": "What is the purpose of biometric authentication?", "options": ["To play games with biological components", "To use biological data for authentication", "To create biological viruses"], "correct": 1, "explanation": "Biometric authentication utilizes unique biological characteristics, such as fingerprints, retinal patterns, or facial recognition, for identity verification purposes."},
    {"question": "What is the best practice for creating strong passwords?", "options": ["Use the same password for everything", "Include personal information in the password", "Use a combination of letters, numbers, and symbols", ], "correct": 2, "explanation": "Creating strong passwords involves using a combination of letters, numbers, and symbols to enhance security. Avoid using easily guessable information like personal details and refrain from using the same password across multiple accounts to minimize the risk of unauthorized access."},
])

current_question = 0
score = 100

# Function to reset game variables
def reset_game():
    global current_question, score
    current_question = 0
    score = 100
    pygame.mixer.Sound.stop(music3)
    pygame.mixer.Sound.play(music1, -1)
#Using and Creating Global Variables in Your Python Functions – Real Python

# Main menu loop
def main_menu():
    while True:
        screen.blit(loading_background, (0, 0))

        # Draw 3D buttons in red
        draw_3d_button(button_credits, "Credits", RED)
        draw_3d_button(button_instructions, "Instructions", RED)
        draw_3d_button(button_exit, "Exit", RED)
        draw_3d_button(button_game, "Start Game", RED)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_credits.collidepoint(event.pos):
                    credits_screen()
                elif button_instructions.collidepoint(event.pos):
                    instructions_screen()
                elif button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif button_game.collidepoint(event.pos):
                    game_loop()

        pygame.time.Clock().tick(FPS) #Python | time.clock() method - GeeksforGeeks

# Helper function to draw 3D button
def draw_3d_button(rect, text, color):
    pygame.draw.rect(screen, color, rect)

    # Draw top edge
    top_edge = pygame.Rect(rect.x + 2, rect.y + 2, rect.width - 4, 4)
    pygame.draw.rect(screen, WHITE, top_edge)

    # Draw left edge
    left_edge = pygame.Rect(rect.x + 2, rect.y + 2, 4, rect.height - 4)
    pygame.draw.rect(screen, WHITE, left_edge)

    # Draw bottom edge
    bottom_edge = pygame.Rect(rect.x + 2, rect.y + rect.height - 6, rect.width - 4, 4)
    pygame.draw.rect(screen, DARK_COLOR, bottom_edge)

    # Draw right edge
    right_edge = pygame.Rect(rect.x + rect.width - 6, rect.y + 2, 4, rect.height - 4)
    pygame.draw.rect(screen, DARK_COLOR, right_edge)

    draw_text(text, rect.x + rect.width // 2, rect.y + rect.height // 2, DARK_COLOR)
#PyGame Drawing Shapes - PyGame Tutorial (ryanstutorials.net)

# Function to display correct/incorrect answer text box
def display_answer_feedback(is_correct, selected_option, explanation):
    pygame.mixer.Sound.stop(music1)

    if is_correct:
        # Display background 1
        pygame.mixer.Sound.play(music2, -1)
        screen.blit(background1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(2000)
    else:
        # Display background 1
        pygame.mixer.Sound.play(music2, -1)
        screen.blit(background1, (0, 0))

        # Display the correct answer for 2 seconds
        correct_answer_text = f"Correct Answer: {questions[current_question]['options'][questions[current_question]['correct']]}"
        draw_text(correct_answer_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, WHITE, center=True)
        pygame.display.flip()
        pygame.time.delay(2000)

    # Draw explanation text box with paragraph formatting
    max_width = SCREEN_WIDTH - 40
    max_height = SCREEN_HEIGHT // 2
    box_width = min(max_width, 500)  # Limit box width
    box_height = min(max_height, 400)  # Limit box height

    # Draw the text box on top of the background
    draw_text_box(20, SCREEN_HEIGHT // 4, box_width, box_height, explanation, DARK_COLOR)

    # Wait for a click to move on to the next question
    wait_for_click()

    pygame.mixer.Sound.stop(music2)
    pygame.mixer.Sound.play(music1, -1)

    # Clear the explanation text box
    pygame.draw.rect(screen, DARK_COLOR, (20, SCREEN_HEIGHT // 4, box_width, box_height))
    pygame.display.flip()

# Helper function to draw 3D text box with wrapped text
def draw_3d_text_box(x, y, width, height, text, background_color, border_color=DARK_COLOR, paragraph=True):
    # Create a transparent surface for the text box
    text_box_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(text_box_surface, background_color, (0, 0, width, height))  # Use the specified background color

    # Draw the border
    pygame.draw.rect(text_box_surface, border_color, (0, 0, width, height), 2)

    # Draw the wrapped text on the surface
    draw_wrapped_text(text_box_surface, text, (width // 2, height // 2), font, DARK_COLOR, paragraph)
#Pygame Rect Tutorial - Complete Guide - GameDev Academy

    # Calculate the position to center the text box on the screen
    screen.blit(text_box_surface, ((SCREEN_WIDTH - width) // 2, (SCREEN_HEIGHT - height) // 2))
    pygame.display.flip()

def draw_paragraph(x, y, width, height, text, color):
    font_size = 20
    font = pygame.font.SysFont(None, font_size)
    lines = text.split('\n')

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y + i * font_size)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
#Python enumerate(): Simplify Loops That Need Counters – Real Python

def draw_text_box(x, y, width, height, text, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    lines = textwrap.wrap(text, width=50)  # Adjust the width as needed
    font_size = 30  # Adjust the font size as needed
    font = pygame.font.Font(None, font_size)

    # Draw each line of text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x + width // 2, y + height // 2 + i * font_size)
        screen.blit(text_surface, text_rect)
#Python enumerate(): Simplify Loops That Need Counters – Real Python
#Pygame Rect Tutorial - Complete Guide - GameDev Academy

    pygame.display.flip()

# Helper function to draw wrapped text
def draw_wrapped_text(surface, text, position, font, color, paragraph=True, offset=(0, 0)):
    lines = textwrap.wrap(text, width=MAX_LINE_LENGTH) if paragraph else [text]

    total_height = len(lines) * 25

    # Create a transparent surface for the text box
    text_box_surface = pygame.Surface((surface.get_width(), total_height), pygame.SRCALPHA)

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(text_box_surface.get_width() // 2, i * 25 + text_surface.get_height() // 2))
        text_box_surface.blit(text_surface, (text_rect.x, i * 25))
#How to make a Text Input Box in Pygame - CodersLegacy

    # Calculate the y-coordinate for centering the text vertically
    y_coordinate = position[1] - total_height // 2 + (surface.get_height() - total_height) // 2
    box_position = (position[0] + offset[0], y_coordinate + offset[1])

    surface.blit(text_box_surface, box_position)
    pygame.display.flip()  # Making sure the text is rendered on the screen
#How to make a Text Input Box in Pygame - CodersLegacy

# Helper function to draw text with a 3D effect
def draw_text_3d(text, x, y, color, border_color):
    # Draw the text with a border
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))

    # Draw the border
    border_rect = pygame.Rect(text_rect.x - 2, text_rect.y - 2, text_rect.width + 4, text_rect.height + 4)
    pygame.draw.rect(screen, border_color, border_rect)

    # Draw the main text
    screen.blit(text_surface, text_rect)

# Credits screen
def credits_screen():
    screen.blit(background6, (0, 0))  # Change to background6
    draw_text("We are inspired", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, DARK_COLOR, font_size=33)

    # Credits
    credits_list = ["Malik, A. (January 4, 2023). Displaying FPS. Geeks for Geeks.",
        "Python - Displaying real-time FPS at which webcam/video file is processed using OpenCV - GeeksforGeeks",
        "(November 18, 2023). Python sys. Geeks for Geeks.",
        "Python sys Module - GeeksforGeeks",
        "Ramos, L. (May 15, 2023). Global. Real Python",
        "Using and Creating Global Variables in Your Python Functions – Real Python",
        "(December 8, 2022). Time.Clock. Geeks for Geeks.",
        "Python | time.clock() method - GeeksforGeeks",
        "Tray, R. Pygame, drawing shapes. Ryan’s Tutorial.",
        "Pygame Drawing Shapes - PyGame Tutorial (ryanstutorials.net)",
        "(November 8, 2023). Rect Tutorial. Game Dev Academy.",
        "Pygame Rect Tutorial - Complete Guide - GameDev Academy",
        "Weber, B. (November 18, 2020). Python Enumerate(). Real Python.",
        "Python enumerate(): Simplify Loops That Need Counters – Real Python",
        "Pygame Rect. Pygame",
        "pygame.Rect — pygame v2.6.0 documentation",
        "Text Box. Coders Legacy.",
        "How to make a Text Input Box in Pygame - CodersLegacy",
        "Gruppetta, S. (October 20, 2021). Len(). Real Python",
        "Using the len() Function in Python – Real Python",
        "(June 27, 2015). Center Text. Stack Overflow.",
        "python - How to Center Text in Pygame - Stack Overflow",
        "Python Range(). W3schools.",
        "Python range() Function (w3schools.com)",
        "(April 19, 2021). Adding scrolling. Stack Overflow.",
        "python - Add scrolling to a platformer in pygame - Stack Overflow"
]

    # Set up the text box
    text_box = pygame.Rect(50, 120, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 200)

    # Draw orange text box
    pygame.draw.rect(screen, ORANGE, text_box)

    # Calculate vertical space for centering
    total_height = len(credits_list) * 14  # Adjust font size here
    starting_y = text_box.y + (text_box.height - total_height) // 2
#Using the len() Function in Python – Real Python

    # Draw each line of the credits text centered inside the text box
    for i, credit_line in enumerate(credits_list):
        draw_text(credit_line, text_box.x + text_box.width // 2, starting_y + i * 14, DARK_COLOR, center=True, font_size=14)

    draw_back_button(RED)
    pygame.display.flip()
    wait_for_click()

# Instructions screen
def instructions_screen():
    # Start playing music 4
    pygame.mixer.Sound.stop(music1)
    pygame.mixer.Sound.play(music4, -1)

    screen.blit(background5, (0, 0))  # Change to background5

    # Updated instructions text with line breaks
    instructions_text = """
        Welcome to Security Savagery, where you can test your knowledge and skills.
        You will face 15 questions relating to online security terms and questions.
        It’s a multiple-choice game where you will have to choose the best answer.
        If you reach over 1000 points you will win the game.
        But if you get under 1000 points, you will lose the game.
    """

    # Split text into sentences
    sentences = instructions_text.split('.\n')

    # Create a font
    font = pygame.font.Font(None, 26)

    # Set up the text box
    text_box = pygame.Rect(50, 100, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 300)

    # Draw orange text box
    pygame.draw.rect(screen, ORANGE, text_box)

    # Draw each sentence on a new line
    for i, sentence in enumerate(sentences):
        text_surface = font.render(sentence, True, (255, 255, 255))
        text_position = (text_box.left + 10, text_box.top + 10 + i * 40)
        screen.blit(text_surface, text_position)
#Python enumerate(): Simplify Loops That Need Counters – Real Python

    draw_back_button(RED)
    pygame.display.flip()
    wait_for_click()

    # Stop playing music 4 when the instructions screen is exited
    pygame.mixer.Sound.stop(music4)

# Function to get an unasked question
def get_unasked_question():
    for i, question in enumerate(questions):
        if not question["asked"]:
            questions[i]["asked"] = True
            return question
    return None

# Game loop
def game_loop():
    global current_question, score
    pygame.mixer.Sound.stop(music1)
    pygame.mixer.Sound.play(music1, -1)

    start_time = time.time()
    clock = pygame.time.Clock()  # Create a clock object

    while current_question < len(questions):
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(TIME_LIMIT - elapsed_time, 0)

        if remaining_time == 0:
            # Time is up, mark the answer as incorrect
            is_correct = False
            selected_option = -1
            score -= 100
            display_explanation(questions[current_question]['explanation'])

            # Move to the next question
            current_question += 1
            start_time = time.time()

        else:
            question = questions[current_question]
            screen.blit(background4, (0, 0))

            draw_text(f" Time left: {remaining_time} seconds", 140, 15, ORANGE)
            draw_text(f"Score: {score}", 660, 7, WHITE, center=False)

            draw_question(question["question"], question["options"], QUESTION_BOX_COLOR, OPTION_BOX_COLOR)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    is_correct, selected_option = handle_answer_click(event.pos)

                    if is_correct:
                        score += 200
                        current_question += 1
                        start_time = time.time()
                    else:
                        score -= 100
                        pygame.mixer.Sound.stop(music1)
                        pygame.mixer.Sound.play(music3, -1)
                        screen.blit(background1, (0, 0))

                        # Display the correct answer for 2 seconds
                        draw_text(f"Correct Answer: {question['options'][question['correct']]}",
                                  SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, DARK_COLOR)
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        # Display the explanation on screen after getting an answer incorrect
                        display_explanation(question['explanation'])

                        pygame.mixer.Sound.stop(music3)
                        pygame.mixer.Sound.play(music1, -1)

                        # Move to the next question even if answered incorrectly
                        current_question += 1
                        start_time = time.time()

        clock.tick(FPS)  # Limit the loop to a fixed frame rate

    end_game()

# Display explanation screen
def display_explanation(explanation):
    screen.blit(background6, (0, 0))
    pygame.display.flip()

    # Stop playing music 2 and 3 before displaying the explanation
    pygame.mixer.Sound.stop(music2)
    pygame.mixer.Sound.stop(music3)

    max_width = SCREEN_WIDTH - 40
    max_height = SCREEN_HEIGHT // 2
    box_width = min(max_width, 500)
    box_height = min(max_height, 400)

    draw_text_box(20, SCREEN_HEIGHT // 4, box_width, box_height, explanation, DARK_COLOR)

    pygame.display.flip()  # Make sure the explanation text is rendered

    # Use a timer for the delay before moving on to the next question
    start_time = pygame.time.get_ticks()
    delay_time = 4000  # 5 seconds in milliseconds
#https://www.geeksforgeeks.org/how-to-add-time-delay-in-python/
    while pygame.time.get_ticks() - start_time < delay_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.Clock().tick(FPS)

    pygame.mixer.Sound.stop(music2)
    pygame.mixer.Sound.play(music1, -1)

    # Clear the explanation text box
    pygame.draw.rect(screen, DARK_COLOR, (20, SCREEN_HEIGHT // 4, box_width, box_height))
    pygame.display.flip()

# Draw score box on the screen
def draw_score_box(x, y, width, height, text, background_color, text_color):
    pygame.draw.rect(screen, background_color, (x, y, width, height))
    font_size = 36  # Adjust the font size as needed
    font = pygame.font.Font(None, font_size)

    # Draw the score text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

# End game screen
def end_game():
    if score < 1000:
        pygame.mixer.Sound.play(music3, -1)
        screen.blit(background2, (0, 0))  # Switch to background 2
        draw_text(f"Your Score: {score}", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, WHITE, font_size=60)
    else:
        pygame.mixer.Sound.play(music2, -1)
        screen.blit(background3, (0, 0))  # Switch to background 3
        draw_text(f"Your Score: {score}", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, WHITE, font_size=60)

    draw_back_button(RED)
    draw_reset_button(RED)  # Draw reset button inside the game
    pygame.display.flip()
    wait_for_reset_or_click()

# Helper function to draw text on the screen
def draw_text(text, x, y, color, center=True, font_size=24):
    font = pygame.font.Font(pygame.font.get_default_font(), font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)

    screen.blit(text_surface, text_rect)
#pygame.Rect — pygame v2.6.0 documentation

# Helper function to draw the question and options on the screen
def draw_question(question, options, question_box_color, option_box_color):
    # Draw the question box
    question_box = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 150, 600, 100)
    pygame.draw.rect(screen, question_box_color, question_box)

    # Draw the centered question text
    draw_text(question, question_box.centerx, question_box.centery - 15, DARK_COLOR)

    # Adjusted vertical spacing for options
    vertical_spacing = 60
    starting_y = SCREEN_HEIGHT // 2 + vertical_spacing * (len(options) - 1) // 2

    # Draw the option boxes with a more 3D appearance
    for i, option in enumerate(options):
        option_box = pygame.Rect(SCREEN_WIDTH // 2 - 250, starting_y + i * vertical_spacing, 500, 50)
        pygame.draw.rect(screen, option_box_color, option_box)
#Python enumerate(): Simplify Loops That Need Counters – Real Python

        # Draw shaded border
        pygame.draw.rect(screen, DARK_COLOR, option_box, 2)

        # Draw the stylized option text
        draw_text_3d(f"{chr(65 + i)}. {option}", option_box.centerx, option_box.centery, DARK_COLOR, ORANGE)
#python - How to Center Text in Pygame - Stack Overflow

# Helper function to draw the back button on the screen
def draw_back_button(color):
    pygame.draw.rect(screen, color, button_back)
    draw_text("Back", button_back.centerx, button_back.centery, DARK_COLOR)

# Helper function to draw the reset button on the screen
def draw_reset_button(color):
    pygame.draw.rect(screen, color, button_reset)
    draw_text("Reset", button_reset.centerx, button_reset.centery, DARK_COLOR)

# Helper function to handle answer click
def handle_answer_click(position):
    vertical_spacing = 60
    starting_y = SCREEN_HEIGHT // 2 + vertical_spacing * (len(questions[current_question]["options"]) - 1) // 2
#https://stackoverflow.com/questions/35754511/manipulation-on-vertical-space-in-matplotlib-subplots

    option_rects = [pygame.Rect(SCREEN_WIDTH // 2 - 250, starting_y + i * vertical_spacing, 500, 30) for i in range(3)]
#Python range() Function (w3schools.com)
    for i, option_rect in enumerate(option_rects):
        if option_rect.collidepoint(position):
            selected_option = i
            correct_option = questions[current_question]["correct"]

            # Check if the click position is within the green line (correct answer)
            if i == correct_option:
                return True, selected_option
            else:
                return False, selected_option

    return False, -1

# Helper function to wait for a click event
def wait_for_click():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.time.Clock().tick(FPS)

# Helper function to wait for a reset or click event
def wait_for_reset_or_click():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint(event.pos):
                    pygame.mixer.stop()
                    main_menu()
                elif button_reset.collidepoint(event.pos):
                    pygame.mixer.stop()
                    reset_game()
                    game_loop()

        pygame.time.Clock().tick(FPS)

# Run the main menu loop
main_menu()
