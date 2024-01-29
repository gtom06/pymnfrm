from import_utils import execute
INPUT_FILE_PATH = 'data/portfolioFromGSheets.csv'
OUTPUT_FILE_PATH = 'data/portfolio.csv'

def main():
    execute(INPUT_FILE_PATH, OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()