#imalirezapy
def draw():

    # Letters to ascii art
    letters ={
    'A': ['..###..', '.#...#.', '.#####.', '.#...#.', '.#...#.'],
    'B': ['.####..', '.#...#.', '.####..', '.#...#.', '.####..'],
    'C': ['..####.', '.#.....', '.#.....', '.#.....', '..####.'],
    'D': ['.####..', '.#...#.', '.#...#.', '.#...#.', '.####..'],
    'E': ['.#####.', '.#.....', '.#####.', '.#.....', '.#####.'],
    'F': ['.#####.', '.#.....', '.###...', '.#.....', '.#.....'],
    'G': ['..####.', '.#.....', '.#..##.', '.#...#.', '..####.'],
    'H': ['.#...#.', '.#...#.', '.#####.', '.#...#.', '.#...#.'],
    'I': ['.#####.', '...#...', '...#...', '...#...', '.#####.'],
    'J': ['.#####.', '.....#.', '.....#.', '.#...#.', '..###..'],
    'K': ['.#...#.', '.#..# .', '.##....', '.#..# .', '.#...#.'],
    'L': ['.#.....', '.#.....', '.#.....', '.#.....', '.#####.'],
    'M': ['.#...#.', '.##.##.', '.#.#.#.', '.#...#.', '.#...#.'],
    'N': ['.#...#.', '.##..#.', '.#.#.#.', '.#..##.', '.#...#.'],
    'O': ['..###..', '.#...#.', '.#...#.', '.#...#.', '..###..'],
    'P': ['.####..', '.#...#.', '.####..', '.#.....', '.#.....'],
    'Q': ['..###..', '.#...#.', '.#...#.', '.#..##.', '..##.#.'],
    'R': ['.####..', '.#...#.', '.####..', '.#..#..', '.#...#.'],
    'S': ['..####.', '.#.....', '.####..', '.....#.', '.####..'],
    'T': ['.#####.', '...#...', '...#...', '...#...', '...#...'],
    'U': ['.#...#.', '.#...#.', '.#...#.', '.#...#.', '..###..'],
    'V': ['.#...#.', '.#...#.', '.#...#.', '..#.#..', '...#...'],
    'W': ['.#...#.', '.#...#.', '.#.#.#.', '.##.##.', '.#...#.'],
    'X': ['.#...#.', '..#.#..', '...#...', '..#.#..', '.#...#.'],
    'Y': ['.#...#.', '..#.#..', '...#...', '...#...', '...#...'],
    'Z': ['.#####.', '....#..', '...#...', '..#....', '.#####.'],
    '!': [' | ', ' | ', ' | ', '   ', ' * ', '   .    '],
    ' ': ['  ',  '  ', '  ', '  ', '  ']}

    # takes your name
    name = input("Enter name: ").upper()
    print()

    # we have 5 row
    for row in range(5):
        string = ""

        # for exaple add ascii chars on row one and then print
        for letter in name:
            string += letters[letter][row]
        print(string)
draw()

