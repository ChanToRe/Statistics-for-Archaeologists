require(graphics)

df <-
    rbind(c(25, 21, 13),
          c(14, 19, 15),
          c(12, 18, 17))
rownames(df) = c("simple pit", "wooden chamber", "stone chamber")
colnames(df) = c("<21", "21-40", ">40")

med.d <- medpolish(df)

print(df)
print(med.d)

png("/Users/jch/Desktop/plot.png", width=500, height=500, res=100)
plot(med.d)

dev.off()