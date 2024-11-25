gender <- factor(c("male","females","male","trans","males"))
print("Original List")
print(gender)

levels = factor((c("male","females","male","trans","males")))
print("Levels are:")
print(levels(gender))

gender[3] #access

gender[2]<-"female" #modify