# ============================================
# Independent Study Analysis – AI Tool Usage
# Date: 2026-03-31
# ============================================



library(readxl)     # for reading Excel files
library(dplyr)      # data manipulation
library(ggplot2)    # plotting
library(corrplot)   # correlation heatmap

data <- read_excel("ai_adoption_students.xlsx")
head(data)

data$PE_mean <- rowMeans(data[, paste0("PE", 1:20)], na.rm = TRUE)
data$CU_mean <- rowMeans(data[, paste0("CU", 1:4)], na.rm = TRUE)
data$ATU_mean <- rowMeans(data[, paste0("ATU", 1:5)], na.rm = TRUE)
data$AUP_mean <- rowMeans(data[, paste0("AUP", 1:5)], na.rm = TRUE)
data$MIUA_mean <- rowMeans(data[, paste0("MIUA", 1:5)], na.rm = TRUE)

head(data[, c("PE_mean", "CU_mean", "ATU_mean", "AUP_mean", "MIUA_mean")])
summary(data[, c("PE_mean", "CU_mean", "ATU_mean", "AUP_mean", "MIUA_mean")])

cor_matrix <- cor(data[, c("PE_mean", "CU_mean", "ATU_mean", "AUP_mean", "MIUA_mean")], use = "complete.obs")
cor_matrix

#visualize with a heatmap
corrplot(cor_matrix, method = "color", addCoef.col = "black", number.cex = 0.7)

# Scatterplot matrix
pairs(data[, c("PE_mean", "CU_mean", "ATU_mean", "AUP_mean", "MIUA_mean")])

#histogram of MIUA_mean
hist(data$MIUA_mean, main = "Distribution of MIUA_mean", xlab = "MIUA_mean", col = "skyblue")

model <- lm(MIUA_mean ~ PE_mean + CU_mean + ATU_mean + AUP_mean, data = data)
summary(model)





