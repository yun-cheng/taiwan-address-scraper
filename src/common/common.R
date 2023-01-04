library(data.table)
library(magrittr)
library(stringr)
library(stringi)
library(fst)
library(glue)
library(readxl)

transformers <- tidyverse_style()
transformers$token$fix_quotes <- NULL

styler:::set_style_transformers()
