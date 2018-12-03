women <- read.csv("WOMEN.csv")

women_lpm <- lm(formula = work ~ age + married + children + education, data = women)
summary(women_lpm)

woemn_logit <- glm (formula = work ~ age + 
                    married + children + 
                    education, family = #SPECIFY THE LOGIT MODEL
                    binomial(link = logit), data = women)
summary(women_logit)
xb_logit <- women_logit$coefficients*c(1, mean(women$age), 
                                 mean(women$married), 
                                 mean(women$children), 
                                 mean(women$education))
#Marginal Effect
MgEft_logit <- dlogis(xb_logit)*c(1, mean(women$age), 
                                  mean(women$married), 
                                  mean(women$children), 
                                  mean(women$education))

woemn_probit <- glm (formula = work ~ age + 
                      married + children + 
                      education, family = #SPECIFY THE LOGIT MODEL
                      binomial(link = probit), data = women)
summary(women_probit)
xb_logit <- women_probit$coefficients*c(1, mean(women$age), 
                                       mean(women$married), 
                                       mean(women$children), 
                                       mean(women$education))

women_probit_1 <- glm (formula = work ~ married + children, 
                       family = binomial(link = probit), data = women)
summary(women_probit_1)
