library(ggplot2)
library(reshape2)

dat = read.csv("~/work/justin/misc/backsquat(1).csv")

# remove the "id" column
dat = dat[-c(1)]

random.imp = function (a) {
  missing = is.na(a)
  n.missing = sum(missing)
  a.obs = a[!missing]
  imputed = a
  imputed[missing] = sample(a.obs, n.missing, replace=TRUE)
  return (imputed)
}

dat
ggplot(data=melt(dat), aes(variable, value)) + geom_point()

imp = random.imp(dat)
boxplot(imp)

plot.imp = ggplot(data=melt(imp), aes(variable, value)) 
plot.imp + geom_point()
plot.imp + geom_violin()

