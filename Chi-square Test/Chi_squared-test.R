test = read.csv("/Users/jch/Documents/github/Statistics-for-Archaeologists/Chi_squared_Test.csv") #분석할 데이터를 불러옴

test$RorL = as.factor(test$RorL) #factor형으로 변경
test$Sex = as.factor(test$Sex) #factor형으로 변경

x = test$RorL #리코딩
y = test$Sex #리코딩

table(x, y) #교차분할표 생성

chisq.test(x, y)

#####

test = read.csv("/Users/jch/Desktop/Test.csv") #분석할 데이터를 불러옴

table(test)

F_LHS = 33
F_RHS = 14
M_LHS = 11
M_RHS = 29

T_T = F_LHS + F_RHS + M_LHS + M_RHS

#Marginal total
F_T = F_LHS + F_RHS
M_T = M_LHS + M_RHS
LHS_T = F_LHS + M_LHS
RHS_T = F_RHS + M_RHS

#Expected value
F_LHS_EV = (F_T * LHS_T)/T_T
F_RHS_EV = (F_T * RHS_T)/T_T
M_LHS_EV = (M_T * LHS_T)/T_T
M_RHS_EV = (M_T * RHS_T)/T_T

xx = ((F_LHS-F_LHS_EV)^2/F_LHS_EV)+((F_RHS-F_RHS_EV)^2/F_RHS_EV)+((M_LHS-M_LHS_EV)^2/M_LHS_EV)+((M_RHS-M_RHS_EV)^2/M_RHS_EV)
xx