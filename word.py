#!/usr/bin/env python3

import requests
import click
import subprocess


@click.command()
@click.argument("word")
@click.option(
    "-p", "--play", is_flag=True, help="play pronunciation using mpv"
)
def main(word, play):
    """
    Lookup meaning of WORD.
    """

    endpoint = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(endpoint)
    response.raise_for_status()

    result = response.json()[0]
    pronunciation = result["phonetics"][0]["audio"]
    meanings = result["meanings"]
    click.echo(f"word: {word}")
    click.echo(f"pronunciation: {pronunciation}")
    click.echo("=" * 80)

    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        definitions = meaning["definitions"]

        click.echo(f"{part_of_speech}s:")
        for definition in definitions:
            for k, v in definition.items():
                if k == "synonyms":
                    v = ", ".join(v)
                if k == "definition":
                    click.echo("- ", nl=False)
                else:
                    click.echo("  ", nl=False)
                click.echo(f"{k}: {v}")
            click.echo()

        click.echo("-" * 80)

    if play:
        click.echo("\n:: playing pronunciation...\n")
        subprocess.run(["mpv", pronunciation])


if __name__ == "__main__":
    main()
