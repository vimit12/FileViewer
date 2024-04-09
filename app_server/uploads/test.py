import json
import pandas as pd

def main():
    # Load JSON data
    with open('./output22.json') as f:
        json_data = json.load(f)

    print(len(json_data))
    

    print("SUCCESS")

if __name__ == '__main__':
    main()