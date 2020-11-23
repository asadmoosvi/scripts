#!/usr/bin/env python3

import requests
import click


@click.command()
@click.argument("word")
def main(word):
    """
    Lookup meaning of WORD.
    """

    endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(endpoint)
    response.raise_for_status()

    result = response.json()[0]
    pronunciation = result["phonetics"][0]["audio"]
    meanings = result["meanings"]
    print(f"word: {word}")
    print(f"pronunciation: {pronunciation}")
    print("=" * 80)

    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        definitions = meaning["definitions"]

        print(f"{part_of_speech}s:")
        for definition in definitions:
            for k, v in definition.items():
                if k == "synonyms":
                    v = ", ".join(v)
                if k == "definition":
                    print("- ", end="")
                else:
                    print("  ", end="")
                print(f"{k}: {v}")
            print()

        print("-" * 80)


if __name__ == "__main__":
    main()
