vec1 <-  c(1,2,3)
vec2 <- c(TRUE,FALSE)
vec <- c(1+3i)
lst = list(vec1,vec2)
print("Original List")
print(lst)
lst[[2]] <- NULL
print("MOdified List")
print(lst)

lst[[2]] <- c("TEACH","CODING")
print("MOdified List")
print(lst)
