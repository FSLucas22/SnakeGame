from io import TextIOWrapper

def get_high_score_file() -> TextIOWrapper:
    try:
        rfile = open('snakeHighScores.txt', 'r')

    except:
        wfile = open('snakeHighScores.txt', 'w')
        for i in range(10):
            wfile.write('0\n')
        wfile.close()
        rfile = open('snakeHighScores.txt', 'r')

    return rfile


def update_highscore(score: int) -> None:
    read_file = get_high_score_file()
    score_list = read_file.readlines()
    read_file.close()
    write_file = open('snakeHighScores.txt', 'w')
    for i in range(len(score_list)):
        if score > int(score_list[i]):
            score_list.pop()
            score_list.insert(i, str(score) + '\n')
            break

    for i in range(len(score_list)):
        write_file.write(score_list[i])
    write_file.close()
