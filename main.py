import pygame, math, time

pygame.init()
pygame.font.init()  # Make sure to initialize the font module

surfaceWidth, surfaceHeight = (700, 1200)
surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))


# Button Class - Handles button creation and drawing
class Button:
    def __init__(self, x, y, w, h, text, color, text_color, font, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.action = action
        self.txt_surface = self.font.render(self.text, True, self.text_color)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0, 15)
        text_rect = self.txt_surface.get_rect(center=self.rect.center)
        surface.blit(self.txt_surface, text_rect)


# Calculator Class - Manages all UI elements
class Calculator:
    def __init__(self):
        self.__surface = surface
        self.__width = 700
        self.__height = 1200
        self.__state = False
        self.__precedence = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}
        self.__operators = ['(', ')', '+', '-', '*', '/', '^']
        self.__vividYellow = '#FEE715'
        self.__richBlack = '#101820'
        self.__salmonRed = '#ED6F63'
        self.__deepNavy = '#00203F'
        self.__paleAqua = '#ADEFD1'
        self.__font = pygame.font.Font('LEMONMILK-Medium.otf', 120)

        self.__buttons = []
        self.createButtons()

        # Display box for calculator input/output
        self.__displayBox = pygame.Rect(50, 25, 600, 150)
        self.__displayText = ""
        self.__displayFont = pygame.font.Font('LEMONMILK-Medium.otf', 80)

    def createButtons(self):
        # Buttons and their attributes are stored in lists in a dictionary for easier access
        button_data = [
            # Numbers
            {'text': '0', 'rect': (25, 1025, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('0')},
            {'text': '1', 'rect': (25, 850, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('1')},
            {'text': '2', 'rect': (200, 850, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('2')},
            {'text': '3', 'rect': (375, 850, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('3')},
            {'text': '4', 'rect': (25, 675, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('4')},
            {'text': '5', 'rect': (200, 675, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('5')},
            {'text': '6', 'rect': (375, 675, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('6')},
            {'text': '7', 'rect': (25, 500, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('7')},
            {'text': '8', 'rect': (200, 500, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('8')},
            {'text': '9', 'rect': (375, 500, 150, 150), 'color': self.__vividYellow,
             'action': lambda: self.handle_input('9')},

            # Operators
            {'text': 'X', 'rect': (550, 500, 125, 150), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('x')},
            {'text': '÷', 'rect': (550, 675, 125, 150), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('÷')},
            {'text': '+', 'rect': (550, 850, 125, 150), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('+')},
            {'text': '-', 'rect': (550, 1025, 125, 150), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('-')},
            {'text': '(', 'rect': (200, 360, 150, 125), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('(')},
            {'text': ')', 'rect': (375, 360, 150, 125), 'color': self.__salmonRed,
             'action': lambda: self.handle_input(')')},
            {'text': '^', 'rect': (25, 360, 150, 125), 'color': self.__salmonRed,
             'action': lambda: self.handle_input('^')},

            # Utility
            {'text': 'C', 'rect': (200, 1025, 150, 150), 'color': self.__deepNavy, 'text_color': self.__paleAqua,
             'action': self.clear_display},
            {'text': 'D', 'rect': (375, 1025, 150, 150), 'color': self.__deepNavy, 'text_color': self.__paleAqua,
             'action': self.delete_char},
            {'text': '=', 'rect': (50, 200, 600, 150), 'color': self.__deepNavy, 'text_color': self.__paleAqua,
             'action': self.evaluate_expression},
        ]

        # Create Button objects and add to the list
        for data in button_data:
            self.__buttons.append(Button(
                x=data['rect'][0], y=data['rect'][1], w=data['rect'][2], h=data['rect'][3],
                text=data['text'],
                color=data['color'],
                text_color=data.get('text_color', self.__richBlack),
                font=self.__font,
                action=data['action']
            ))

    def handle_input(self, value):
        if self.__state:
            self.clear_display()
            self.__state = False

        self.__displayText += value

    def clear_display(self):
        self.__displayText = ""

    def delete_char(self):
        self.__displayText = self.__displayText[:-1]

    def evaluate_expression(self):

        try:
            result = self.__displayText
            expression = self.tokenize(result)
            self.clear_display()
            RPNExpression = self.convertToRpn(expression)
            rpnCalculation = self.calculateRpn(RPNExpression)
            self.__displayText = str(rpnCalculation)
            self.__state = True

        except:
            self.__displayText = "Error"
            self.__state = True

    def convertToRpn(self, expression):
        inputInRpn = []
        operators = []

        for token in expression:
            if token.isdigit():
                inputInRpn.append(token)

            elif token == '(':
                operators.append(token)

            elif token == ')':
                while operators and operators[-1] != '(':
                    inputInRpn.append(operators.pop())

                if operators and operators[-1] == '(':
                    operators.pop()
                else:
                    raise ValueError("Mismatched parentheses")

            elif token in self.__operators:
                while operators and operators[-1] != '(' and self.__precedence[operators[-1]] >= self.__precedence[
                    token]:
                    inputInRpn.append(operators.pop())
                operators.append(token)

        while operators:
            op = operators.pop()
            if op == '(':
                raise ValueError("Mismatched parentheses")
            inputInRpn.append(op)


        print(inputInRpn)
        return inputInRpn

    def calculateRpn(self, RPNExpression):
        operand = []
        operator = []

        for i in RPNExpression:
            if i.isdigit():
                operand.append(float(i))

            elif i in self.__operators:
                number2 = operand.pop()
                number1 = operand.pop()

                if i == '+':
                    operand.append(number1 + number2)

                if i == '-':
                    operand.append(number1 - number2)

                if i == '/':
                    operand.append(number1 / number2)

                if i == '*':
                    operand.append(number1 * number2)

                if i == '^':
                    operand.append(number1 ** number2)

                operator.append(i)

        return operand[0]

    def tokenize(self, result):
        tokens = []
        i = 0
        while i < len(result):
            char = result[i]
            if char == 'x':
                char = '*'
            if char == '÷':
                char = '/'
            if char.isdigit():
                numString = ''
                while i < len(result) and result[i].isdigit():
                    numString += result[i]
                    i += 1
                tokens.append(numString)

            elif char in self.__operators:
                tokens.append(char)
                i += 1

            else:
                i += 1

        return tokens


    def draw(self):
        self.__surface.fill(self.__richBlack)

        # Draw the display box
        pygame.draw.rect(self.__surface, 'white', self.__displayBox, 0, 10)
        display_text_surface = self.__displayFont.render(self.__displayText, True, self.__richBlack)
        text_rect = display_text_surface.get_rect(right=self.__displayBox.right - 20, centery=self.__displayBox.centery)
        self.__surface.blit(display_text_surface, text_rect)

        # Draw all buttons
        for button in self.__buttons:
            button.draw(self.__surface)

        pygame.display.flip()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.__buttons:
                        if button.rect.collidepoint(event.pos):
                            if button.action:
                                button.action()

            self.draw()
            pygame.display.update()


instance = Calculator()
instance.run()

pygame.quit()