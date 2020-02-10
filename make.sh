#!/usr/bin/env bash

DATA=data/
DIST=dist/
TMP=tmp/
VENV=venv/
CLUSTERS=clusters/
PICKLE=pickle/
TF_IDF=tf_idf/
DATA_ZIP=data.zip

if [[ -d VENV ]]; then
    echo "${VENV}は存在します"
else:
    python -m venv VENV
fi

if [[ -d DATA ]]; then
    echo "${DATA}は存在します"
else:
    unzip DATA_ZIP
fi

if [[ -d DIST ]]; then
    echo "${DIST}は存在します"
else:
    mkdir DIST
fi

if [[ -d TMP ]]; then
    echo "${TMP}は存在します"
else:
    mkdir TMP
    mkdir TMP + CLUSTERS
    mkdir TMP + PICKLE
    mkdir TMP + TF_IDF
fi
