#!/bin/bash
Rscript -e "library(plumber); pr <- plumb('r_api/api.R'); pr$run(port=8000)"
