rm(list = ls())
library(lme4)
library(lmerTest)

base_dir  = "C:\\My Drive\\Projects\\SBMD tolerance\\codebase\\data"
file_name = 'tolerance_all_md.csv'
file_path = paste(base_dir, file_name, sep='/')
df = read.csv(file_path)
df$isGuessCorrect = as.logical(df$isGuessCorrect)
df$sex = as.factor(df$sex)
df <- within(df, sex <- relevel(sex, ref='male'))
df$education = as.factor(df$education)
df <- within(df, education <- relevel(education, ref='0'))
df$n_macro_exp = as.factor(df$n_macro_exp)
df <- within(df, n_macro_exp <- relevel(n_macro_exp, ref='1'))



# Model All drugs
model = lmer(
  formula = isGuessCorrect ~ (1|trial_id_int) + n_MD + acid_dose + suggestibility, 
  df)
summary(model)


# Model LSD 
model = lmer(
  formula = isGuessCorrect ~ (1|trial_id_int) + n_MD + acid_dose + suggestibility, 
  subset(df, df$drug_cat==1))
summary(model)


# Model Shroom MDs 
model = lmer(
  formula = isGuessCorrect ~ (1|trial_id_int) + n_MD + acid_dose + suggestibility, 
  subset(df, df$drug_cat==2))
summary(model)
