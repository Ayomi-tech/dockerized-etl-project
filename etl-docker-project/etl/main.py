from extract import extract
from transform import transform
from load import load

def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()

