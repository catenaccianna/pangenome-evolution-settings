library(ggplot2)       # For plotting
library(tidyverse)     # For data wrangling
library(knitr)         # For making nice rmarkdown documents
library(cowplot)       # For theme
library(viridis)       # For color scale
library(RColorBrewer)  # For more color scales
library(rstatix)
library(ggsignif)      # For adding pairwise significance to plots
library(Hmisc)         # For bootstrapping confidence intervals
library(kableExtra)    # For displaying nice tables

#setwd("../Desktop/fitness")
fit <- as.data.frame(data.table::fread(file="C:/Users/Anna Catenacci/Desktop/fitness/fitness_all.csv", header=TRUE))

ggplot(fit,
       ggplot2::aes(x = `Num Unique Genotypes`, y = `Dominant Fitness`, color=`Condition`, fill=`Condition`))+

        ggplot2::stat_summary(geom="line", fun=mean)+
        ggplot2::stat_summary(
          geom="ribbon",
          fun.data="mean_cl_boot",
          fun.args=list(conf.int=0.95),
          alpha=0.2,
          linetype=0,
          se = TRUE
        )

