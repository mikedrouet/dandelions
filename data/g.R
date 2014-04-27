


library(ggplot2)
data <- read.csv("/home/mdrouet/gpl.csv", header = TRUE,sep=",")
starttimes <- strptime(data$Start,"%M-%d-%Y %H:%M:%OS")
endtimes <- strptime(data$End, "%M-%d-%Y %H:%M:%OS")
pdata <- data.frame(data$AppName, starttimes, endtimes)
p <- ggplot(pdata, aes(colour=data.AppName))
p <- p + geom_segment(aes(x=starttimes,
            xend=endtimes,
            y=data.AppName,
            yend=data.AppName),
            size=2)
p <- p + geom_point(aes(x=starttimes,
              y=data.AppName), size=5)
p <- p + geom_point(aes(x=endtimes,y=data.AppName),
              size=5)
p <- p + xlab("Duration")
p
setwd("/home/mdrouet")
ggsave(p, file="kdnight.png", height=7, width=17)