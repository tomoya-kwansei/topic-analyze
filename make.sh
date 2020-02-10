#!/usr/bin/env bash

DATA=data/
DIST=dist/
TMP=tmp/
VENV=venv/
CLUSTERS=clusters/
PICKLE=pickle/
TF_IDF=tf_idf/
DATA_ZIP=data.zip

if [[ -ne VENV ]]; then
    python -m venv VENV
fi

if [[ -ne DATA ]]; then
    unzip DATA_ZIP
fi

if [[ -ne DIST ]]; then
    mkdir DIST
fi

if [[ -ne TMP ]]; then
    mkdir TMP
    mkdir TMP + CLUSTERS
    mkdir TMP + PICKLE
    mkdir TMP + TF_IDF
fi
