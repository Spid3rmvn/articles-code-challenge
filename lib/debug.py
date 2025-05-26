from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def main():
    # Create authors
    author1 = Author("Alice")
    author2 = Author("Bob")

    # Create magazines
    mag1 = Magazine("Tech Monthly", "Technology")
    mag2 = Magazine("Health Today", "Health")

    # Author1 writes articles
    article1 = author1.write_article(mag1, "AI in 2025")
    article2 = author1.write_article(mag2, "Healthy Living Tips")

    # Author2 writes an article
    article3 = author2.write_article(mag1, "Cybersecurity Essentials")

    # Print author's articles
    print(f"{author1.name} wrote these articles:")
    for article in author1.articles():
        print(f"- {article.title} in {article.magazine.name}")

    # Print magazines author1 contributed to
    print(f"\n{author1.name} contributed to magazines:")
    for mag in author1.magazines():
        print(f"- {mag.name}")

    # Print contributors to mag1
    print(f"\nContributors to {mag1.name}:")
    for contributor in mag1.contributors():
        print(f"- {contributor.name}")

    # Print article titles in mag1
    print(f"\nArticles in {mag1.name}:")
    for title in mag1.article_titles():
        print(f"- {title}")

if __name__ == "__main__":
    main()
