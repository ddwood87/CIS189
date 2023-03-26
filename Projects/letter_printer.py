import pickle

class char:
      def __init__(self, character):
            self.name = character
      def set_4_lines(self, lines):
            self.lines_4 = lines
      def set_dot_matrix(self, lines):
          self.lines_dot = lines
      def get_lines(self, count):
            if count == 4:
                  return self.lines_4
      def set_dot_lines(self, lines):
          self.lines_dot = lines
      def get_dot_lines(self):
          return self.lines_dot
        
class printer:
    def __init__(self, file_name): 
        self.file = file_accessor(file_name)

    def get_chars(self, text):
        chars = list()
        for c in str(text):
            chars.append(self.file.get_character(c))
        return chars
    
    def print_large_text(self, text: str):
        chars = self.get_chars(text)
        output = ""
        for i in range(line_height):
            for c in chars:
                output += c.get_lines(line_height)[i]
                output += "  "
            output += "\n"
        print(output)

class file_accessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.chars = list()
        self.load()
    def load(self):
        with open(self.file_name, 'rb') as char_file:
            self.chars = pickle.load(char_file)
    def add_char(self, char):
        self.chars.append(char)
    def save(self):
        with open(self.file_name, 'wb') as char_file:   
            pickle.dump(self.chars, char_file)
    def get_character(self, character):
        for char in self.chars:
            if char.name == character:
                return char

class build_chars:
    
    chars = {
        " ": ["    ",
              "    ",
              "    ",
              "    "],
        "0": [" ** ",
              "*  *",
              "*  *",
              " ** "],
        "1": [" *  ",
              "**  ",
              " *  ",
              "*** "],
        "2": ["*** ",
              "   *",
              " ** ",
              "****"],
        "3": ["*** ",
              " __*",
              "   *",
              "*** "],
        "4": ["*  *",
              "*__*",
              "   *",
              "   *"],
        "5": ["****",
              "*__ ",
              "   *",
              "___*"],
        "6": [" ***",
              "*__ ",
              "*  *",
              " ** "],
        "7": ["****",
              "  * ",
              " *  ",
              "*   "],
        "8": [" ** ",
              "*__*",
              "*  *",
              " ** "],
        "9": [" ** ",
              "*__*",
              "   *",
              "*** "],
        "A": [" /\ ",
              "|__|",
              "|  |",
              "|  |"],
        "B": ["|** ",
              "|__*",
              "|  *",
              "|__*"],
        "C": [" ***",
              "*   ",
              "*   ",
              " ***"],
        "D": ["|** ",
              "|  |",
              "|  |",
              "|_* "],
        "E": ["|***",
              "|__ ",
              "|   ",
              "|___"],
        "F": ["|***",
              "|__ ",
              "|   ",
              "|   "],
        "G": [" **=",
              "* _ ",
              "*  *",
              " ** "],
        "H": ["|  |",
              "|__|",
              "|  |",
              "|  |"],
        "I": ["____",
              " |  ",
              " |  ",
              "_|__"],
        "J": ["____",
              "  | ",
              "  | ",
              "*_*"],
        "K": ["| / ",
              "|/  ",
              "| \ ",
              "|  \\"],
        "L": ["|   ",
              "|   ",
              "|   ",
              "|___"],
        "M": ["|  |",
              "|\/|",
              "|  |",
              "|  |"],
        "N": ["|  |",
              "|\ |",
              "| \|",
              "|  |"],
        "O": [" ** ",
              "*  *",
              "*  *",
              " ** "],
        "P": ["|**\\",
              "|__*",
              "|   ",
              "|   "],
        "Q": [" ** ",
              "*  *",
              "*  *",
              " **\\"],
        "R": ["|**\\",
              "|__*",
              "| \\ ",
              "|  \\"],
        "S": [" **-",
              "*__ ",
              "   *",
              "-__*"],
        "T": ["____",
              "  | "
              "  | ",
              "  | ",],
        "U": ["|  |",
              "|  |",
              "|  |",
              "*__*"],
        "V": ["|  |",
              "|  |",
              "\  /",
              " \/ "],
        "W": ["|  |",
              "|  |",
              "|/\|",
              "*  *"],
        "X": ["\  /",
              " \/ ",
              " /\ ",
              "/  \\"],
        "Y": ["\  /",
              " \/ ",
              " /  ",
              "/  "],
        "Z": ["****",
              "  / ",
              " /  ",
              "/___"]

    }
    def __init__(self, file_name):
        self.file = file_accessor(file_name)
    def build_file(self):
        for r in self.chars:
            c = char(r)
            c.set_4_lines(self.chars[r])
            self.file.add_char(c)
        self.file.save()

if __name__ == '__main__':
      display_number = '235SCFAS SFY'
      line_height = 4
      file_name = str(line_height) + '_line_chars.bin'
      build_chars(file_name).build_file()
      p = printer(file_name)
      p.print_large_text(display_number)