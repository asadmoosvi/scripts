#!/usr/bin/env python3

import requests
import click
import subprocess
import os
import sys


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
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        click.echo(f":: word {word!r} not found", err=True)
        sys.exit(1)

    result = response.json()[0]
    pronunciation = result["phonetics"][0]["audio"]
    meanings = result["meanings"]
    click.secho("word: ", fg="cyan", bold=True, nl=False)
    click.secho(f"{word}", fg="bright_green")
    click.secho("pronunciation: ", fg="cyan", bold=True, nl=False)
    click.secho(f"{pronunciation}", fg="bright_green")
    click.secho("=" * click.get_terminal_size()[0], fg="magenta")

    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        definitions = meaning["definitions"]

        click.secho(f"{part_of_speech}s:", fg="cyan", bold=True)
        for definition in definitions:
            for k, v in definition.items():
                if k == "synonyms":
                    v = ", ".join(v)
                if k == "definition":
                    click.echo("- ", nl=False)
                else:
                    click.echo("  ", nl=False)
                click.secho(f"{k}: ", bold=True, nl=False)
                click.secho(f"{v}", fg="bright_green")
            click.echo()

        click.secho("-" * click.get_terminal_size()[0], fg="magenta")

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
