netflix_data <- C:\Users\check\OneDrive\Desktop\netflix_data.csv

netflix_data <- read.csv("C:\Users\Ogbemudia\Music\OneDrive\Desktop\netflix_titles.csv")

# Create a bar plot for ratings distribution
ggplot(netflix_data, aes(x=rating)) +
  geom_bar(fill="skyblue", color="black") +
  labs(title="Ratings Distribution on Netflix", x="Rating", y="Number of Shows/Movies") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


