sample_data <- data.frame(
  name = c("Alice", "Bob", "Charlie", "David"),
  roll = c(101, 102, 103, 104),
  year = c(2023, 2023, 2024, 2024),
  dept = c("CS", "Math", "Physics", "Biology")
)

print("The first 2 rows are:")
res = sample_data[1:2,]
print(res)