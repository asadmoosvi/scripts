#!/usr/bin/env python3

import requests
import click
import subprocess
import os


@click.command()
@click.argument("word")
@click.option(
    "-p", "--play", is_flag=True, help="play pronunciation using mpv"
)
@click.option("-s", "--save", is_flag=True, help="save pronunciation to file")
def main(word, play, save):
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

    if save:
        filename = os.path.basename(pronunciation)
        click.echo(f"\n:: saving pronunciation to external file {filename!r}")
        with open(filename, "wb") as fout:
            pronunciation_data = requests.get(pronunciation)
            pronunciation_data.raise_for_status()
            for chunk in pronunciation_data.iter_content(1024):
                if chunk:
                    fout.write(chunk)


if __name__ == "__main__":
    main()
