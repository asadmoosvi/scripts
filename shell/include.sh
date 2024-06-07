#!/usr/bin/env bash

# general functions all shell programs can make use of

ensure_installed() {
  for program in "$@"; do
    command -v "$program" >/dev/null 2>&1 || {
      echo >&2 "$program is required but not installed. Aborting."
      exit 1
    }
  done
}
